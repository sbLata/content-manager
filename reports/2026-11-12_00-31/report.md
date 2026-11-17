# Content audit: practice-site

Audited 8 pages on 2026-11-12_00-31. Found 29 issues: 8 high, 17 medium, 4 low.


**AI checks skipped this run (rerun to complete):**

- index.html: AI review skipped (All models failed. Last error: Expecting ',' delimiter: line 3 column 9 (char 749))
- pricing.html: AI review skipped (All models failed. Last error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usual)
- watering-guide.html: AI review skipped (All models failed. Last error: Expecting ',' delimiter: line 3 column 12 (char 733))
- contradiction check skipped ('list' object has no attribute 'get')

AI model used: gemini-3.5-flash, gemini-3.5-flash-lite, gemini-3.6-flash. AI calls: 26. Findings dropped for missing evidence: 0. Escalated to a human: 0.

## Top priorities

1. The 'Preparing the soil' section uses advanced technical language unsuitable for the stated complete beginner audience. on beginner-guide.html
2. The 'Potting your plant' section is a single extremely long sentence with no punctuation or breaks. on beginner-guide.html
3. The 'Preparing the soil' section uses dense jargon without explanation for a beginner audience. on beginner-guide.html

## All issues

| ID | Severity | Page | Check | Issue | Evidence | Confidence | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F001 | high | beginner-guide.html | Content positioning | The 'Preparing the soil' section uses advanced technical language unsuitable for the stated complete beginner audience. | Ensure substrate aeration via perlite amendment to optimise rhizosphere oxygenation, and calibrate the | high | Simplify the soil preparation instructions to match the beginner audience level. | draft |
| F002 | high | beginner-guide.html | User-friendliness | The 'Potting your plant' section is a single extremely long sentence with no punctuation or breaks. | first you get a pot that is a bit bigger than the plant and then you put some soil in the bottom | high | Break the text into short sentences and clear paragraphs. | draft |
| F003 | high | beginner-guide.html | User-friendliness | The 'Preparing the soil' section uses dense jargon without explanation for a beginner audience. | Ensure substrate aeration via perlite amendment to optimise rhizosphere oxygenation | high | Rewrite the section using plain language appropriate for complete beginners. | draft |
| F004 | high | beginner-guide.html | User-friendliness | The page ends abruptly with account cancellation instructions instead of a clear next action for a beginner plant care site. | Open your account page, choose Plans, then choose Cancel plan. | high | Replace the account cancellation instructions with a call to action or link to join the monthly care plan. | draft |
| F005 | high | faq.html | Traditional SEO | Missing page title | (no <title> element) | rule | Add a <title> that names the page topic and the site, e.g. 'FAQ / Leafline'. | draft |
| F006 | high | index.html | Traditional SEO | Broken internal link | shop.html | rule | Create shop.html or point the link to an existing page. | draft |
| F007 | high | pest-guide.html | Content positioning | The page does not support the site goal of converting readers to a monthly care plan. | Quarantine new plants for two weeks and keep humidity steady. | high | Include a call to action or link offering the monthly care plan to help manage ongoing pest prevention. | draft |
| F008 | high | pest-guide.html | Missing images and alt text | The text refers to a photo that is not present on the page. | Compare your leaves with it before choosing a treatment. | high | Add the referenced photo or remove the mention of the photo. | draft |
| F009 | medium | about.html | Duplicate content | Paragraph is 100% identical to one on index.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F010 | medium | about.html | Missing images and alt text | Image has no alt text | images/team.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F011 | medium | about.html | Outdated content | The page promotes an internship opportunity with a deadline in the past. | We are currently hiring for summer 2021 internships. Apply before the end of May! | high | Verify whether this information is still current or update/remove the outdated hiring notice. | draft |
| F012 | medium | about.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F013 | medium | about.html | User-friendliness | Clear next action scores 1 because the page ends with no links, buttons, or instructions on what the reader should do next. | ## Stay up to date | high | Add a clear call to action, such as a link to sign up for the monthly care subscription or newsletter. | draft |
| F014 | medium | beginner-guide.html | Content positioning | The page includes instructions on how to cancel a plan, which does not support the site goal of converting readers to a monthly care plan. | Managing your account
Open your account page, choose Plans, then choose Cancel plan. | high | Remove the account cancellation instructions or replace them with a subscription sign-up prompt. | draft |
| F015 | medium | beginner-guide.html | Duplicate content | Paragraph is 99% identical to one on watering-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F016 | medium | beginner-guide.html | GEO readiness | The guide does not provide a short, direct answer to its main question near the top for AI search tools to quote. | Houseplants for complete beginners
This guide is written for complete beginners who have never kept a plant alive. | high | Add a short, direct summary paragraph immediately under the main heading defining the best beginner plant and basic care. | draft |
| F017 | medium | beginner-guide.html | Missing images and alt text | Image has no alt text | images/snake-plant.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F018 | medium | beginner-guide.html | Outdated content | The page references an old year as current/top pick, which conflicts with the current date of 2026. | Our 2020 Plant of the Year is the snake plant, and it is this year's top pick for new plant owners. | high | Verify and update the plant recommendation year to reflect current offerings. | draft |
| F019 | medium | index.html | Duplicate content | Paragraph is 100% identical to one on about.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F020 | medium | index.html | Missing images and alt text | Image has no alt text | images/hero.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F021 | medium | news.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F022 | medium | news.html | User-friendliness | No clear next action or link provided to book the workshop. | Our autumn repotting workshop is open for booking. | high | Add a direct link, button, or contact instructions for booking. | draft |
| F023 | medium | pest-guide.html | Traditional SEO | Missing meta description | (no meta description) | rule | Add a one-sentence meta description (under 160 characters) summarising the page. | draft |
| F024 | medium | pest-guide.html | User-friendliness | The page lacks a clear next action or call to action for the reader. | Quarantine new plants for two weeks and keep humidity steady. | high | Add a link, button, or instruction telling the reader what to do next, such as exploring the subscription care plan. | draft |
| F025 | medium | watering-guide.html | Duplicate content | Paragraph is 99% identical to one on beginner-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F026 | low | about.html | Content positioning | Fits the site goal scores 2 because the page fails to guide readers toward the site's goal of subscribing to the monthly care plan. | Today we help thousands of home gardeners keep their plants healthy with practical guides and a monthly care subscription. | high | Include a link or button inviting readers to learn more about the monthly care subscription. | draft |
| F027 | low | faq.html | Accessibility basics | Vague link text | click here | rule | Rewrite the link text to describe the destination, e.g. 'See how to cancel your plan'. | draft |
| F028 | low | faq.html | GEO readiness | FAQ page has no FAQ structured data | (no FAQPage schema) | rule | Add FAQPage JSON-LD listing each question and answer. | draft |
| F029 | low | watering-guide.html | Accessibility basics | Heading level skipped (H1 to H4) | <h4>Why watering is tricky</h4> | rule | Change this heading to H2, or add the missing level above it. | draft |

## Rubric scores (1 = clearly fails, 5 = excellent)

| Page | Scannable | Plain language | Clear steps | Next action | Audience | Headline | Answers visit | Site goal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| about.html | 3 | 5 | 5 | 1 | 5 | 3 | 5 | 2 |
| beginner-guide.html | 2 | 2 | 2 | 1 | 2 | 4 | 3 | 2 |
| faq.html | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| news.html | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 5 |
| pest-guide.html | 4 | 5 | 3 | 1 | 5 | 5 | 5 | 1 |
