"""
Content Manager - Phase 5: human approval step.

Usage (from the content-manager folder, with .venv turned on):
    python review.py practice-site

Shows each suggested fix from reports/latest/report.json and asks you to
approve, edit, reject or skip it. Nothing changes without your approval.
Approved rewrites are applied to a COPY of the site (fixed-site/); your
original files are never changed. Everything else you approve is listed in
reports/latest/approved_fixes.md as a to-do list. Nothing is ever published.
"""
import sys, os, re, json, shutil

REPORT = "reports/latest/report.json"


def apply_rewrite(html, evidence, new_text):
    """Replace the quoted text in the HTML, allowing for line breaks inside it."""
    words = [re.escape(w) for w in evidence.split()]
    if not words:
        return html, False
    pattern = r"\s+".join(words)
    new_html, n = re.subn(pattern, new_text.replace("\\", "\\\\"), html, count=1)
    return new_html, n == 1


def main():
    if len(sys.argv) < 2:
        print("Usage: python review.py <site-folder>")
        sys.exit(1)
    site = sys.argv[1]
    data = json.load(open(REPORT))
    findings = data["findings"]
    to_review = [f for f in findings if f["status"] == "draft"]
    escalated = [f for f in findings if f["status"] == "escalated"]

    print(f"\n{len(to_review)} suggested fixes to review. {len(escalated)} issues were escalated to you (no fix suggested).")
    print("For each fix type:  a = approve   e = edit   r = reject   s = skip for now   q = save and quit\n")

    for f in to_review:
        print("-" * 70)
        print(f"{f['id']}  [{f['severity']}]  {f['page']}  |  {f['check']}")
        print(f"Issue:     {f['issue']}")
        print(f"Evidence:  {f['evidence']}")
        if f.get("confidence"):
            print(f"Confidence: {f['confidence']}")
        if f.get("rewrite"):
            print(f"Rewrite:   {f['rewrite']}")
        print(f"Fix:       {f['suggested_fix']}")
        while True:
            choice = input("Your decision (a/e/r/s/q): ").strip().lower()
            if choice in ("a", "e", "r", "s", "q"):
                break
        if choice == "q":
            break
        if choice == "a":
            f["status"] = "approved"
        elif choice == "r":
            f["status"] = "rejected"
        elif choice == "e":
            new_text = input("Type your version of the fix (or the replacement text): ").strip()
            f["suggested_fix"] = new_text
            if f.get("rewrite"):
                f["rewrite"] = new_text
            f["status"] = "approved"
            f["edited_by_human"] = True

    # apply approved rewrites to a copy of the site
    out_dir = "fixed-site"
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    shutil.copytree(site, out_dir)
    applied, todo = [], []
    for f in findings:
        if f["status"] != "approved":
            continue
        if f.get("rewrite") and f["method"] == "ai":
            path = os.path.join(out_dir, f["page"])
            html = open(path, encoding="utf-8").read()
            new_html, ok = apply_rewrite(html, f["evidence"], f["rewrite"])
            if ok:
                open(path, "w", encoding="utf-8").write(new_html)
                applied.append(f)
                continue
        todo.append(f)

    json.dump(data, open(REPORT, "w"), indent=2)
    counts = {s: sum(f["status"] == s for f in findings) for s in ("approved", "rejected", "draft", "escalated")}
    edited = sum(1 for f in findings if f.get("edited_by_human"))
    lines = ["# Approved fixes", "",
             f"Approved {counts['approved']} (of which you edited {edited}), rejected {counts['rejected']}, "
             f"not yet reviewed {counts['draft']}, escalated {counts['escalated']}.", "",
             f"## Applied automatically to fixed-site/ ({len(applied)})", ""]
    lines += [f"- {f['id']} {f['page']}: {f['issue']}" for f in applied] or ["- none"]
    lines += ["", f"## To do by hand ({len(todo)})", ""]
    lines += [f"- {f['id']} {f['page']}: {f['issue']}. Fix: {f['suggested_fix']}" for f in todo] or ["- none"]
    lines += ["", "## Escalated: needs your judgment", ""]
    lines += [f"- {f['id']} {f['page']}: {f['issue']} ({f.get('escalation_reason', '')})" for f in escalated] or ["- none"]
    open("reports/latest/approved_fixes.md", "w").write("\n".join(lines) + "\n")

    reviewed = counts["approved"] + counts["rejected"]
    rate = round(100 * counts["approved"] / reviewed) if reviewed else 0
    print("\n" + "=" * 70)
    print(f"Approved {counts['approved']}, rejected {counts['rejected']}, still to review {counts['draft']}.")
    print(f"Fix acceptance rate: {rate}% of reviewed fixes.")
    print(f"Applied {len(applied)} rewrites to fixed-site/. Your original {site}/ is unchanged.")
    print("Summary saved to reports/latest/approved_fixes.md")


if __name__ == "__main__":
    main()
