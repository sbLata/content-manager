"""
Content Manager - Phase 4: rule-based content audit.

Usage (from the content-manager folder, with .venv turned on):
    python audit.py practice-site          rule-based checks only (no AI)
    python audit.py practice-site --ai     rule-based checks plus AI-judged checks

Reads every .html page in the folder, runs the rule-based checks, and saves
a report to reports/latest/ (report.md for people, report.json for the scorer).
"""
import sys, os, re, json, difflib, datetime
from bs4 import BeautifulSoup

try:
    import requests
except ImportError:
    requests = None

MAX_PAGES = 30
VAGUE_LINK_TEXT = {"click here", "here", "read more", "more", "link", "this link"}
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def finding(check, severity, page, issue, evidence, why, fix, related_pages=None):
    return {
        "check": check, "severity": severity, "page": page,
        "related_pages": related_pages or [], "issue": issue,
        "evidence": evidence, "why_it_matters": why,
        "suggested_fix": fix, "rewrite": "", "method": "rule", "confidence": "", "risk_topic": "none",
        "status": "draft", "escalation_reason": "",
    }


# ---------- R1: read the site ----------
def read_site(folder):
    pages, errors = {}, []
    files = sorted(f for f in os.listdir(folder) if f.endswith(".html"))
    skipped = files[MAX_PAGES:]
    for name in files[:MAX_PAGES]:
        try:
            with open(os.path.join(folder, name), encoding="utf-8") as fh:
                pages[name] = BeautifulSoup(fh.read(), "html.parser")
        except Exception as e:  # one bad page never stops the audit
            errors.append(f"{name}: {e}")
    return pages, skipped, errors


# ---------- R2: traditional SEO ----------
def check_seo(pages, folder):
    out, titles, metas = [], {}, {}
    for name, s in pages.items():
        title = s.title.get_text(strip=True) if s.title else ""
        if not title:
            out.append(finding("Traditional SEO", "high", name, "Missing page title",
                "(no <title> element)", "Search engines and browser tabs show the title; without it the page is hard to find.",
                "Add a <title> that names the page topic and the site, e.g. 'FAQ | Leafline'."))
        else:
            titles.setdefault(title, []).append(name)
        meta = s.find("meta", attrs={"name": "description"})
        desc = (meta.get("content") or "").strip() if meta else ""
        if not desc:
            out.append(finding("Traditional SEO", "medium", name, "Missing meta description",
                "(no meta description)", "Search results show this text; without it the snippet is picked at random.",
                "Add a one-sentence meta description (under 160 characters) summarising the page."))
        else:
            metas.setdefault(desc, []).append(name)
        if not s.find("h1"):
            out.append(finding("Traditional SEO", "high", name, "Missing H1 heading",
                "(no <h1>)", "The H1 tells readers and search engines what the page is about.",
                "Add one H1 that states the page's main topic."))
        for a in s.find_all("a", href=True):
            href = a["href"].strip()
            if href.startswith(("mailto:", "tel:", "#")):
                continue
            if href.startswith(("http://", "https://")):
                if requests is None:
                    continue
                try:
                    r = requests.head(href, timeout=5, allow_redirects=True)
                    ok = r.status_code < 400
                except Exception:
                    ok = False
                if not ok:
                    out.append(finding("Traditional SEO", "high", name, "Broken external link", href,
                        "Broken links frustrate readers and signal a neglected site.",
                        "Update the link to a working address or remove it."))
                continue
            target = href.split("#")[0]
            if target and not os.path.exists(os.path.join(folder, target)):
                out.append(finding("Traditional SEO", "high", name, "Broken internal link", href,
                    "Readers hit a 'page not found' error.",
                    f"Create {target} or point the link to an existing page."))
    for title, names in titles.items():
        if len(names) > 1:
            for n in names:
                out.append(finding("Traditional SEO", "medium", n, "Duplicate page title",
                    f"<title>{title}</title>", "Pages with the same title compete in search and confuse readers.",
                    "Give each page a unique title that names its topic.", [x for x in names if x != n]))
    for desc, names in metas.items():
        if len(names) > 1:
            for n in names:
                out.append(finding("Traditional SEO", "low", n, "Duplicate meta description", desc,
                    "Identical descriptions make pages look interchangeable in search results.",
                    "Write a unique description for each page.", [x for x in names if x != n]))
    return out


# ---------- R2: images and alt text ----------
def check_images(pages):
    out = []
    for name, s in pages.items():
        for img in s.find_all("img"):
            if not img.has_attr("alt"):  # alt="" is a deliberate decorative image: not flagged
                out.append(finding("Missing images and alt text", "medium", name, "Image has no alt text",
                    img.get("src", "(no src)"), "Screen readers can't describe the image and search engines can't read it.",
                    "Add alt text describing what the image shows, or alt=\"\" if it is purely decorative."))
    return out


# ---------- R2: accessibility basics ----------
def check_accessibility(pages):
    out = []
    for name, s in pages.items():
        if not (s.html and s.html.get("lang")):
            out.append(finding("Accessibility basics", "medium", name, "Missing page language",
                "<html> has no lang attribute", "Screen readers may read the page in the wrong language.",
                "Add lang=\"en\" to the <html> tag."))
        heads = s.find_all(re.compile(r"^h[1-6]$"))
        prev = None
        for h in heads:
            level = int(h.name[1])
            if prev is not None and level - prev > 1:
                out.append(finding("Accessibility basics", "low", name, f"Heading level skipped (H{prev} to H{level})",
                    f"<{h.name}>{h.get_text(strip=True)}</{h.name}>",
                    "Skipped levels break the page outline that screen-reader users navigate by.",
                    f"Change this heading to H{prev + 1}, or add the missing level above it."))
            prev = level
        for a in s.find_all("a"):
            text = a.get_text(" ", strip=True).lower()
            if text in VAGUE_LINK_TEXT and not a.get("aria-label"):
                out.append(finding("Accessibility basics", "low", name, "Vague link text",
                    a.get_text(strip=True), "Out of context, the link doesn't say where it goes.",
                    "Rewrite the link text to describe the destination, e.g. 'See how to cancel your plan'."))
    return out


# ---------- R2: duplicate content ----------
def main_paragraphs(soup):
    main = soup.find("main") or soup.body or soup  # header and footer are ignored
    return [p.get_text(" ", strip=True) for p in main.find_all("p")]


def check_duplicates(pages, threshold=0.9, min_words=25):
    out, names = [], sorted(pages)
    paras = {n: [p for p in main_paragraphs(pages[n]) if len(p.split()) >= min_words] for n in names}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            for pa in paras[a]:
                for pb in paras[b]:
                    ratio = difflib.SequenceMatcher(None, pa, pb).ratio()
                    if ratio >= threshold:
                        snippet = pa[:90] + "..."
                        for page, other in ((a, b), (b, a)):
                            out.append(finding("Duplicate content", "medium", page,
                                f"Paragraph is {round(ratio * 100)}% identical to one on {other}", snippet,
                                "Repeated text makes pages compete with each other and wastes the reader's time.",
                                "Keep the paragraph on the most relevant page and link to it from the other.", [other]))
    return out


# ---------- R2: GEO readiness (rule part) ----------
def check_geo_rules(pages):
    out = []
    for name, s in pages.items():
        h1 = (s.find("h1").get_text(" ", strip=True).lower() if s.find("h1") else "")
        questions = [h for h in s.find_all(["h2", "h3"]) if h.get_text(strip=True).endswith("?")]
        is_faq = "faq" in name.lower() or "question" in h1 or len(questions) >= 3
        if not is_faq:
            continue
        schemas = " ".join(t.get_text() for t in s.find_all("script", attrs={"type": "application/ld+json"}))
        if "FAQPage" not in schemas:
            out.append(finding("GEO readiness", "low", name, "FAQ page has no FAQ structured data",
                "(no FAQPage schema)", "Structured data helps search engines and AI answer tools quote your answers.",
                "Add FAQPage JSON-LD listing each question and answer."))
    return out


# ---------- R5: report ----------
def write_report(site, findings, pages, skipped, errors, ai_info=None):
    findings.sort(key=lambda f: (SEVERITY_ORDER[f["severity"]], f["page"], f["check"]))
    for i, f in enumerate(findings, 1):
        f["id"] = f"F{i:03d}"
    counts = {s: sum(f["severity"] == s for f in findings) for s in ("high", "medium", "low")}
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    ai_info = ai_info or {}
    data = {"site": site, "run_at": stamp, "pages_audited": sorted(pages), "pages_skipped": skipped,
            "errors": errors, "counts": counts, "methods_run": ["rule", "ai"] if ai_info else ["rule"],
            "ai": ai_info, "findings": findings}
    for folder in (f"reports/{stamp}", "reports/latest"):
        os.makedirs(folder, exist_ok=True)
        json.dump(data, open(f"{folder}/report.json", "w"), indent=2)
        lines = [f"# Content audit: {site}", "",
                 f"Audited {len(pages)} pages on {stamp}. Found {len(findings)} issues: "
                 f"{counts['high']} high, {counts['medium']} medium, {counts['low']} low.", ""]
        if not findings:
            lines.append("No issues found by the rule-based checks.")
        if skipped:
            lines.append(f"Page limit reached; not audited: {', '.join(skipped)}")
        read_errors = [e for e in errors if "skipped" not in e]
        ai_errors = [e for e in errors if "skipped" in e]
        if read_errors:
            lines += ["", f"Pages that could not be read: {', '.join(read_errors)}"]
        if ai_errors:
            lines += ["", "**AI checks skipped this run (rerun to complete):**", ""] + [f"- {e}" for e in ai_errors]
        lines.append("")
        if ai_info:
            esc = sum(f["status"] == "escalated" for f in findings)
            lines.append(f"AI model used: {', '.join(ai_info.get('models', []))}. AI calls: {ai_info.get('calls')}. "
                         f"Findings dropped for missing evidence: {ai_info.get('dropped')}. Escalated to a human: {esc}.")
            lines.append("")
        top = [f for f in findings if f["status"] != "escalated"][:3]
        if top:
            lines += ["## Top priorities", ""] + [f"{i}. {f['issue']} on {f['page']}" for i, f in enumerate(top, 1)] + [""]
        esc = [f for f in findings if f["status"] == "escalated"]
        if esc:
            lines += ["## Escalated to a human (no suggested fix)", ""]
            lines += [f"- {f['id']} ({f['page']}): {f['issue']}. Reason: {f['escalation_reason']}." for f in esc] + [""]
        lines += ["## All issues", "", "| ID | Severity | Page | Check | Issue | Evidence | Confidence | Suggested fix | Status |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for f in findings:
            ev = f["evidence"].replace("|", "/")
            conf = f.get("confidence") or "rule"
            fix = (f["suggested_fix"] or "-").replace("|", "/")
            lines.append(f"| {f['id']} | {f['severity']} | {f['page']} | {f['check']} | {f['issue']} | {ev} | {conf} | {fix} | {f['status']} |")
        if ai_info.get("rubric_scores"):
            lines += ["", "## Rubric scores (1 = clearly fails, 5 = excellent)", "",
                      "| Page | Scannable | Plain language | Clear steps | Next action | Audience | Headline | Answers visit | Site goal |",
                      "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
            keys = ["scannable", "plain_language", "clear_steps", "clear_next_action", "audience_match",
                    "headline_clarity", "answers_the_visit", "fits_site_goal"]
            for p, sc in sorted(ai_info["rubric_scores"].items()):
                lines.append(f"| {p} | " + " | ".join(str(sc.get(k, "-")) for k in keys) + " |")
        open(f"{folder}/report.md", "w").write("\n".join(lines) + "\n")
    return counts


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    use_ai = "--ai" in sys.argv
    if not args:
        print("Usage: python audit.py <folder-with-html-files> [--ai]")
        sys.exit(1)
    folder = args[0]
    pages, skipped, errors = read_site(folder)
    print(f"Running rule-based checks on {len(pages)} pages...")
    findings = (check_seo(pages, folder) + check_images(pages) + check_accessibility(pages)
                + check_duplicates(pages) + check_geo_rules(pages))
    ai_info = None
    if use_ai:
        import ai_checks
        print("Running AI checks (this takes a minute or two)...")
        ai_f, scores, dropped, models, ai_errors, calls = ai_checks.run_ai_checks(pages)
        findings += ai_f
        errors += ai_errors
        ai_info = {"models": models, "calls": calls, "dropped": dropped, "rubric_scores": scores}
    counts = write_report(os.path.basename(os.path.normpath(folder)), findings, pages, skipped, errors, ai_info)
    print(f"Audited {len(pages)} pages. Found {len(findings)} issues "
          f"({counts['high']} high, {counts['medium']} medium, {counts['low']} low).")
    skipped_ai = [e for e in errors if "skipped" in e]
    if skipped_ai:
        print(f"Warning: {len(skipped_ai)} AI check(s) were skipped. See the top of the report.")
    print("Report saved to reports/latest/report.md")


if __name__ == "__main__":
    main()
