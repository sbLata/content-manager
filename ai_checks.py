"""
Content Manager - Phase 5: AI-judged checks (Gemini).

Used by audit.py when you run:  python audit.py practice-site --ai
Needs GEMINI_API_KEY in the .env file. Optional: GEMINI_MODEL in .env to choose a model.
"""
import os, re, json, time, datetime

ALLOWED_CHECKS = {"Outdated content", "User-friendliness", "Content positioning",
                  "GEO readiness", "Missing images and alt text"}
RISK_TOPICS = {"pricing", "legal", "medical", "financial"}
FALLBACK_MODELS = ["gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.6-flash"]
PAUSE_SECONDS = 15         # wait between AI calls, to stay under the free per-minute limit
MAX_AI_CALLS = 40          # hard cap per audit (cost and quota guard)

_client, _calls = None, 0

try:  # read .env first, so GEMINI_MODEL and GEMINI_API_KEY are known before any AI call
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _get_client():
    global _client
    if _client is None:
        from dotenv import load_dotenv
        from google import genai
        load_dotenv()
        key = os.environ.get("GEMINI_API_KEY")
        if not key:
            raise SystemExit("GEMINI_API_KEY is missing. Add it to the .env file in the content-manager folder.")
        _client = genai.Client(api_key=key)
    return _client


def ask_model(prompt):
    """Send one prompt, return parsed JSON. Retries on limits and falls back to other models."""
    global _calls
    if _calls >= MAX_AI_CALLS:
        raise RuntimeError("AI call cap reached for this audit")
    from google.genai import types
    preferred = os.environ.get("GEMINI_MODEL", "").strip() or None
    models = ([preferred] if preferred else []) + [m for m in FALLBACK_MODELS if m != preferred]
    last_error = None
    for model in models:
        for attempt in range(3):
            try:
                _calls += 1
                resp = _get_client().models.generate_content(
                    model=model, contents=prompt,
                    config=types.GenerateContentConfig(response_mime_type="application/json", temperature=0.2))
                time.sleep(PAUSE_SECONDS)
                text = (resp.text or "").strip()
                text = re.sub(r"^```(json)?|```$", "", text).strip()
                return json.loads(text), model
            except json.JSONDecodeError as e:
                last_error = e
                break  # bad output from this model: try the next model
            except Exception as e:
                last_error = e
                msg = str(e)
                if "PerDay" in msg or "per day" in msg.lower():
                    print(f"   (daily free limit used up on {model}, switching model...)")
                    break  # waiting won't help with a daily limit: try the next model
                if "429" in msg or "RESOURCE_EXHAUSTED" in msg or "503" in msg or "UNAVAILABLE" in msg:
                    wait = 30 * (attempt + 1)
                    print(f"   (limit reached on {model}, waiting {wait}s...)")
                    time.sleep(wait)
                    continue
                if "404" in msg or "NOT_FOUND" in msg:
                    break  # model not available: try the next one
                raise
    raise RuntimeError(f"All models failed. Last error: {last_error}")


# ---------- page text the AI sees ----------
def page_text(soup):
    main = soup.find("main") or soup.body or soup   # header, menu and footer are left out
    lines = []
    for el in main.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "img"]):
        if el.name == "img":
            lines.append(f"[IMAGE src={el.get('src', '')} alt={el.get('alt', '(none)')!r}]")
        elif el.name.startswith("h"):
            lines.append("#" * int(el.name[1]) + " " + el.get_text(" ", strip=True))
        else:
            lines.append(el.get_text(" ", strip=True))
    return "\n".join(lines)


def _norm(s):
    s = s.lower().replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\s+", " ", s)
    return s.strip(" \"'.,;:!?")


def evidence_found(quote, text):
    """R3: a finding must quote real text from the page, or it is discarded."""
    q = _norm(quote)
    if len(q) < 4:
        return False
    t = _norm(text)
    if q in t:
        return True
    q = re.sub(r"\.\.\.|…", " ", q)
    parts = [p.strip() for p in q.split("  ") if len(p.strip()) > 8]
    return bool(parts) and all(p in t for p in parts)


# ---------- prompts ----------
PAGE_PROMPT = """You are Content Manager, an AI content auditor. Today's date is {today}.

SITE CONTEXT AND SCORING RUBRIC:
{rubric}

Audit ONE page: {page}. Page content (headings start with #, images appear as [IMAGE ...]):
---
{text}
---

Check only these five things:
1. "Outdated content": statements presented as current or upcoming that are clearly out of date compared with today's date. Historical facts that are correctly described as past are NOT problems.
2. "User-friendliness": score the 4 user-friendliness rubric criteria from 1 to 5 (use 5 if a criterion does not apply). Report a problem for each criterion scoring 2 or lower.
3. "Content positioning": score the 4 positioning rubric criteria from 1 to 5, judging against the audience the page states. Report a problem for each criterion scoring 2 or lower. Technical language on a page stated to be for experienced readers is fine.
4. "GEO readiness": for guide or FAQ pages only, report a problem if the page does not give a short, direct answer to its main question near the top, so AI search tools can quote it. Short news updates do not need this.
5. "Missing images and alt text": report only when the text refers to an image, photo or diagram that is not on the page. Do NOT report missing alt attributes; another check does that.

RULES:
- "evidence" must be an exact quote copied from the page content above (at most 25 words). If the problem is something missing, quote the text closest to where it is missing.
- Never state new facts. For outdated content, the suggested fix asks the owner to verify and update; do not supply current facts yourself.
- "risk_topic" is "pricing", "legal", "medical", "financial" or "none".
- "confidence" is "high", "medium" or "low".
- "rewrite" is replacement text for the quoted evidence when a direct rewrite fixes the problem; otherwise "".
- Only report real problems. If there are none, return an empty findings list.

Return JSON only, in exactly this shape:
{{"rubric_scores": {{"scannable": 0, "plain_language": 0, "clear_steps": 0, "clear_next_action": 0, "audience_match": 0, "headline_clarity": 0, "answers_the_visit": 0, "fits_site_goal": 0}},
 "findings": [{{"check": "", "issue": "", "evidence": "", "why_it_matters": "", "severity": "high|medium|low", "confidence": "high|medium|low", "risk_topic": "none", "suggested_fix": "", "rewrite": ""}}]}}
"""

SITE_PROMPT = """You are Content Manager, an AI content auditor. Below are all pages of one website.

{pages}

Find CONTRADICTIONS: the same fact stated differently on two pages (prices, limits, schedules, instructions, dates).
Different values for clearly different things (for example two different plans) are NOT contradictions.
Each quote must be copied exactly from its page (at most 25 words).

Return JSON only:
{{"contradictions": [{{"page_a": "", "quote_a": "", "page_b": "", "quote_b": "", "issue": "", "confidence": "high|medium|low", "risk_topic": "pricing|legal|medical|financial|none"}}]}}
"""


def _base(check, page, issue, evidence, why, severity, confidence, risk, fix, rewrite, related=None):
    f = {"check": check, "severity": severity if severity in ("high", "medium", "low") else "medium",
         "page": page, "related_pages": related or [], "issue": issue, "evidence": evidence,
         "why_it_matters": why, "suggested_fix": fix, "rewrite": rewrite, "method": "ai",
         "confidence": confidence if confidence in ("high", "medium", "low") else "low",
         "risk_topic": risk if risk in RISK_TOPICS else "none", "status": "draft", "escalation_reason": ""}
    # R4: escalation rules
    reasons = []
    if f["risk_topic"] != "none":
        reasons.append(f"involves {f['risk_topic']}")
    if f["confidence"] == "low":
        reasons.append("low confidence")
    if check == "Contradictory content":
        reasons.append("agent can't verify which statement is correct")
    if reasons:
        f.update(status="escalated", suggested_fix="", rewrite="", escalation_reason="; ".join(reasons))
    return f


def review_page(name, soup, rubric):
    text = page_text(soup)
    data, model = ask_model(PAGE_PROMPT.format(today=datetime.date.today().isoformat(),
                                               rubric=rubric, page=name, text=text))
    out, dropped = [], 0
    for item in data.get("findings", []) or []:
        check = item.get("check", "")
        ev = item.get("evidence", "")
        if check not in ALLOWED_CHECKS or not evidence_found(ev, text):
            dropped += 1
            continue
        out.append(_base(check, name, item.get("issue", ""), ev, item.get("why_it_matters", ""),
                         item.get("severity", "medium"), item.get("confidence", "low"),
                         item.get("risk_topic", "none"), item.get("suggested_fix", ""), item.get("rewrite", "")))
    return out, data.get("rubric_scores", {}), dropped, model


def find_contradictions(pages):
    texts = {n: page_text(s) for n, s in pages.items()}
    joined = "\n\n".join(f"=== PAGE: {n} ===\n{t}" for n, t in texts.items())
    data, model = ask_model(SITE_PROMPT.format(pages=joined))
    out, dropped = [], 0
    for c in data.get("contradictions", []) or []:
        a, b = c.get("page_a", ""), c.get("page_b", "")
        qa, qb = c.get("quote_a", ""), c.get("quote_b", "")
        if a not in texts or b not in texts or not evidence_found(qa, texts[a]) or not evidence_found(qb, texts[b]):
            dropped += 1
            continue
        out.append(_base("Contradictory content", a, c.get("issue", ""), f"{a}: \"{qa}\" / {b}: \"{qb}\"",
                         "Readers get conflicting information and stop trusting the site.", "high",
                         c.get("confidence", "low"), c.get("risk_topic", "none"), "", "", [b]))
    return out, dropped, model


def run_ai_checks(pages, rubric_path="docs/rubric.md"):
    rubric = open(rubric_path, encoding="utf-8").read() if os.path.exists(rubric_path) else ""
    findings, scores, dropped, models, errors = [], {}, 0, set(), []
    for name in sorted(pages):
        print(f"   AI reviewing {name}...")
        try:
            f, s, d, m = review_page(name, pages[name], rubric)
            findings += f; scores[name] = s; dropped += d; models.add(m)
        except Exception as e:  # one failed AI call never stops the audit
            errors.append(f"{name}: AI review skipped ({str(e)[:160]})")
    print("   AI comparing pages for contradictions...")
    try:
        f, d, m = find_contradictions(pages)
        findings += f; dropped += d; models.add(m)
    except Exception as e:
        errors.append(f"contradiction check skipped ({str(e)[:160]})")
    # remove repeats of the same finding
    seen, unique = set(), []
    for f in findings:
        k = (f["check"], f["page"], _norm(f["evidence"])[:60])
        if k not in seen:
            seen.add(k); unique.append(f)
    return unique, scores, dropped, sorted(models), errors, _calls
