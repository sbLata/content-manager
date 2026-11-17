"""
Content Manager - eval scorer.

Usage (from the content-manager folder, with .venv turned on):
    python evals/score.py

Compares reports/latest/report.json with evals/answer_key.json and prints
catches, misses and false alarms per check. Results are saved to evals/results/.
"""
import json, re, os, datetime
from collections import defaultdict

report = json.load(open("reports/latest/report.json"))
key = json.load(open("evals/answer_key.json"))
findings = report["findings"]
checks_run = {f["check"] for f in findings} | set(report.get("checks_run", []))
methods_run = set(report.get("methods_run", ["rule"]))


def tested(item):
    # An item is in scope if the agent ran a method that can detect it.
    m = item["method"].lower()
    return ("rule" in m and "rule" in methods_run) or ("ai" in m and "ai" in methods_run)


def matches(f, item):
    if f["check"] != item["check"]:
        return False
    pages = item["pages"]
    if "all pages" not in pages and f["page"] not in pages:
        return False
    token = item.get("match", "")
    text = f"{f['issue']} {f['evidence']}".lower()
    return not token or re.search(token, text) is not None


issues = [i for i in key["items"] if i["type"] == "issue"]
traps = [i for i in key["items"] if i["type"] == "trap"]
used, per_check = set(), defaultdict(lambda: {"in_scope": 0, "caught": 0, "missed": [], "false_alarms": 0})
caught_ids, missed_ids, not_tested = [], [], []

for item in issues:
    if not tested(item):
        not_tested.append(item["id"]);
        continue
    hits = [i for i, f in enumerate(findings) if matches(f, item)]
    pc = per_check[item["check"]]; pc["in_scope"] += 1
    if hits:
        used.update(hits); caught_ids.append(item["id"]); pc["caught"] += 1
    else:
        missed_ids.append(item["id"]); pc["missed"].append(item["id"])

trap_alarms = []
for item in traps:
    hits = [i for i, f in enumerate(findings) if i not in used and matches(f, item)]
    if hits:
        used.update(hits); trap_alarms.append(item["id"]); per_check[item["check"]]["false_alarms"] += len(hits)

other_alarms = [findings[i] for i in range(len(findings)) if i not in used]
for f in other_alarms:
    per_check[f["check"]]["false_alarms"] += 1

in_scope = len(caught_ids) + len(missed_ids)
false_alarms = sum(v["false_alarms"] for v in per_check.values())
detect = round(100 * len(caught_ids) / in_scope) if in_scope else 0
fa_rate = round(100 * false_alarms / len(findings)) if findings else 0

print(f"\nEval results for {report['site']} (run {report['run_at']})\n")
print(f"{'Check':32} {'Caught':>8} {'False alarms':>14}  Missed")
for check in sorted(per_check):
    v = per_check[check]
    print(f"{check:32} {str(v['caught']) + '/' + str(v['in_scope']):>8} {v['false_alarms']:>14}  {', '.join(v['missed']) or '-'}")
print(f"\nDetection rate: {len(caught_ids)}/{in_scope} = {detect}% of the issues these checks can find")
print(f"False alarms: {false_alarms} of {len(findings)} findings = {fa_rate}%")
print(f"Traps wrongly flagged: {', '.join(trap_alarms) or 'none'}")
print(f"Not tested yet (need AI checks): {len(not_tested)} issues ({', '.join(not_tested)})")

os.makedirs("evals/results", exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
json.dump({"run_at": stamp, "report_run": report["run_at"], "caught": caught_ids, "missed": missed_ids,
           "not_tested": not_tested, "false_alarms": false_alarms, "trap_alarms": trap_alarms,
           "detection_rate": detect, "false_alarm_rate": fa_rate},
          open(f"evals/results/{stamp}.json", "w"), indent=2)
print(f"\nSaved to evals/results/{stamp}.json")
