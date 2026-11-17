# Content Manager

Content Manager is an AI-assisted website content auditor. It reads a folder of HTML pages, finds SEO, accessibility, duplicate-content, outdated-content and positioning problems, and writes a prioritised report with evidence and a suggested fix for each issue. A human reviews every fix before anything changes, and risky findings (pricing, legal, medical, financial, or contradictions it can't resolve) go to a person instead of getting an automatic fix.

The repo includes **Leafline**, a fictional 8-page plant-care site with 26 planted issues and 8 traps, plus an answer key and a scorer so you can measure how well the auditor does.

## How it works

```
practice-site/  ──►  audit.py  ──►  reports/latest/report.md + report.json
                     (rules, plus Gemini with --ai)        │
                                                           ├──►  evals/score.py   (compare with the answer key)
                                                           └──►  review.py        (you approve, edit or reject each fix)
                                                                    │
                                                                    ├──►  fixed-site/                        (copy with approved rewrites applied)
                                                                    └──►  reports/latest/approved_fixes.md   (to-do list)
```

1. **Audit** (`audit.py`): runs rule-based checks on every page, and AI checks too if you add `--ai`.
2. **Score** (`evals/score.py`), optional: compares the report with `evals/answer_key.json`.
3. **Review** (`review.py`): steps through each suggested fix so you can approve, edit, reject or skip it.

## Checks

| Check | Method | What it looks for |
| --- | --- | --- |
| Traditional SEO | Rule | Missing or duplicate `<title>`, missing or duplicate meta description, missing H1, broken internal and external links |
| Missing images and alt text | Rule + AI | `<img>` without an `alt` attribute (`alt=""` counts as deliberately decorative); text that mentions an image that isn't there |
| Accessibility basics | Rule | Missing `lang` on `<html>`, skipped heading levels, vague link text such as "click here" |
| Duplicate content | Rule | Paragraphs of 25+ words that are at least 90% identical across pages (header and footer are ignored) |
| GEO readiness | Rule + AI | FAQ pages without `FAQPage` structured data; guides and FAQs with no short, direct answer near the top |
| Outdated content | AI | Statements presented as current or upcoming that are out of date |
| User-friendliness | AI | Scored with the rubric: scannable, plain language, clear steps, clear next action |
| Content positioning | AI | Scored with the rubric: audience match, headline clarity, answers the visit, fits the site goal |
| Contradictory content | AI | The same fact stated differently on two pages (prices, limits, schedules, instructions) |

The rubric and the site context the AI judges against are in [docs/rubric.md](docs/rubric.md). A rubric criterion scoring 2 or lower becomes a finding.

### Safeguards on AI findings

- **Evidence or it's dropped.** Each AI finding must quote text that really appears on the page. If the quote can't be found, the finding is thrown away, and the report shows how many were dropped.
- **No made-up facts.** For outdated content, the fix asks the site owner to check and update the text. The AI never supplies new facts.
- **Escalation.** A finding goes to a human with no suggested fix when it involves pricing, legal, medical or financial content, when the AI's confidence is low, or when it's a contradiction (the agent can't know which version is right).
- **Limits.** The audit makes at most 40 AI calls and waits 15 seconds between calls to stay under free-tier rate limits. If a model hits its quota, the audit retries or moves to a fallback model. If an AI check fails on one page, the audit carries on and lists the skipped check at the top of the report.

## Setup

You need Python 3.10 or later (it was developed on 3.14). The `--ai` checks also need a [Gemini API key](https://aistudio.google.com/apikey).

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
cp .env.example .env
```

Then open `.env` and add your key:

```
GEMINI_API_KEY=your-key-here
GEMINI_MODEL=            # optional; leave blank to use the built-in fallback list
```

`.env` is in `.gitignore`, so your key is never committed.

## Usage

Run every command from the project root with the virtual environment turned on.

**1. Run the audit**

Rule-based checks only. This takes a few seconds and doesn't need an API key:

```bash
python audit.py practice-site
```

Rule-based and AI checks. This takes a few minutes because of the pause between AI calls:

```bash
python audit.py practice-site --ai
```

Each run saves `report.md` (for people) and `report.json` (for the scripts) to `reports/<timestamp>/` and `reports/latest/`. The report starts with the top three priorities, then lists escalated issues, then shows every issue in a table with its severity, evidence, confidence and suggested fix. AI runs also include each page's rubric scores.

**2. Score against the answer key** (optional)

```bash
python evals/score.py
```

This prints how many planted issues each check caught, the overall detection rate, the false-alarm rate, and which traps were wrongly flagged. Results are saved to `evals/results/`.

**3. Review the fixes**

```bash
python review.py practice-site
```

For each suggested fix, type `a` to approve, `e` to edit, `r` to reject, `s` to skip, or `q` to save and quit. When you finish:

- Approved AI rewrites are applied to a fresh copy of the site in `fixed-site/`. **This folder is deleted and rebuilt on every run.** Your original site folder is never changed.
- Every other approved fix, and every escalated issue, is listed in `reports/latest/approved_fixes.md` as a to-do list.
- Nothing is ever published.

### Auditing your own site

Point `audit.py` at any folder of `.html` files. It audits up to 30 pages. Before you use `--ai`, update the "Site context" section of [docs/rubric.md](docs/rubric.md) with your own site, audience and goal. `evals/score.py` only works with the Leafline answer key.

## Latest results

From the AI-enabled run on 12 November 2026 against `practice-site/`:

| Metric | Result |
| --- | --- |
| Planted issues caught | 26 / 26 (100%) |
| False alarms | 5 of 39 findings (13%) |
| Traps wrongly flagged | 2 of 8 (UT1, PT1) |

## Project structure

```
content-manager/
├── audit.py               # Rule-based checks, report writer, entry point
├── ai_checks.py           # Gemini-powered checks, evidence checking, escalation rules
├── review.py              # Interactive human approval step
├── requirements.txt
├── .env.example           # Template for your API key settings
├── docs/
│   └── rubric.md          # Scoring rubric and site context for the AI checks
├── evals/
│   ├── answer_key.json    # 26 planted issues and 8 traps in practice-site
│   ├── score.py           # Compares the latest report with the answer key
│   └── results/           # Saved scoring runs
├── practice-site/         # The fictional Leafline site, with planted issues
├── fixed-site/            # Output of review.py: the site with approved rewrites
└── reports/               # Audit reports by timestamp, plus latest/
```

To see the practice site, open `practice-site/index.html` in a browser.
