# Content audit: practice-site

Audited 8 pages on 2026-11-11_23-27. Found 30 issues: 7 high, 20 medium, 3 low.

Pages that could not be read: pest-guide.html: AI review failed (All models failed. Last error: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash-lite is no longer available to new users. Please update your code to use models/gemini-3.5-flash-lite for the latest features and improvements. We recommend you to use the Interactions API (https://aistudio.google.com/docs/get-started).', 'status': 'NOT_FOUND'}}), watering-guide.html: AI review failed (All models failed. Last error: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash-lite is no longer available to new users. Please update your code to use models/gemini-3.5-flash-lite for the latest features and improvements. We recommend you to use the Interactions API (https://aistudio.google.com/docs/get-started).', 'status': 'NOT_FOUND'}}), contradiction check failed (All models failed. Last error: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash-lite is no longer available to new users. Please update your code to use models/gemini-3.5-flash-lite for the latest features and improvements. We recommend you to use the Interactions API (https://aistudio.google.com/docs/get-started).', 'status': 'NOT_FOUND'}})
AI model used: gemini-3.5-flash. AI calls: 31. Findings dropped for missing evidence: 0. Escalated to a human: 1.

## Top priorities

1. Language and technical depth under soil preparation do not match the stated beginner audience. on beginner-guide.html
2. Directing users to cancel their plan conflicts directly with the site goal of converting readers to a care plan. on beginner-guide.html
3. Uses dense scientific jargon that fails the plain language requirement for beginners. on beginner-guide.html

## Escalated to a human (no suggested fix)

- F007 (pricing.html): The page does not provide a clear next action or call-to-action for users to select or sign up for a care plan.. Reason: involves pricing.

## All issues

| ID | Severity | Page | Check | Issue | Evidence | Confidence | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F001 | high | beginner-guide.html | Content positioning | Language and technical depth under soil preparation do not match the stated beginner audience. | Ensure substrate aeration via perlite amendment to optimise rhizosphere oxygenation, and calibrate the substrate's cation exchange capacity relative to your cultivar's edaphic requirements. | high | Simplify content depth to suit someone who has never kept a plant alive. | draft |
| F002 | high | beginner-guide.html | Content positioning | Directing users to cancel their plan conflicts directly with the site goal of converting readers to a care plan. | Open your account page, choose Plans, then choose Cancel plan. | high | Remove cancellation steps and replace with a call to action introducing Leafline's monthly care subscription. | draft |
| F003 | high | beginner-guide.html | User-friendliness | Uses dense scientific jargon that fails the plain language requirement for beginners. | Ensure substrate aeration via perlite amendment to optimise rhizosphere oxygenation, and calibrate the substrate's cation exchange capacity relative to your cultivar's edaphic requirements. | high | Rewrite the section in plain language explaining basic soil needs simply. | draft |
| F004 | high | faq.html | Traditional SEO | Missing page title | (no <title> element) | rule | Add a <title> that names the page topic and the site, e.g. 'FAQ / Leafline'. | draft |
| F005 | high | index.html | Outdated content | App launch announcement presents a past date (March 2022) as an upcoming event. | Our new mobile app launches next month (March 2022)! | high | Verify the current availability of the mobile app and update or remove the announcement. | draft |
| F006 | high | index.html | Traditional SEO | Broken internal link | shop.html | rule | Create shop.html or point the link to an existing page. | draft |
| F007 | high | pricing.html | User-friendliness | The page does not provide a clear next action or call-to-action for users to select or sign up for a care plan. | Premium plan: $25 per month. Everything in Basic, plus a seasonal fertilizer box and video calls with a plant expert. | high | - | escalated |
| F008 | medium | about.html | Duplicate content | Paragraph is 100% identical to one on index.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F009 | medium | about.html | Missing images and alt text | Image has no alt text | images/team.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F010 | medium | about.html | Outdated content | The page advertises summer 2021 internships as currently active, which is past compared to today's date. | We are currently hiring for summer 2021 internships. Apply before the end of May! | high | Verify current hiring status and remove or update the recruitment message. | draft |
| F011 | medium | about.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F012 | medium | about.html | User-friendliness | The section encouraging readers to stay up to date lacks a clear next action, link, or subscription form. | ## Stay up to date | high | Add an email newsletter sign-up form or a clear link enabling readers to subscribe. | draft |
| F013 | medium | beginner-guide.html | Duplicate content | Paragraph is 99% identical to one on watering-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F014 | medium | beginner-guide.html | GEO readiness | The guide lacks a direct, short answer summary at the top summarizing beginner houseplant care. | This guide is written for complete beginners who have never kept a plant alive. | high | Add a 2-3 sentence overview block near the top summarizing the core steps of beginner houseplant care. | draft |
| F015 | medium | beginner-guide.html | Missing images and alt text | Image has no alt text | images/snake-plant.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F016 | medium | beginner-guide.html | Outdated content | Refers to 2020 as 'this year', which is outdated given today's date of 2026-11-11. | Our 2020 Plant of the Year is the snake plant, and it is this year's top pick for new plant owners. | high | Verify current top recommendations with the content owner and update the year reference. | draft |
| F017 | medium | beginner-guide.html | User-friendliness | Potting instructions are buried in a single long run-on sentence without clear step-by-step formatting. | first you get a pot that is a bit bigger than the plant and then you put some soil in the bottom and then you take | high | Break the potting instructions into a numbered list with one clear action per step. | draft |
| F018 | medium | beginner-guide.html | User-friendliness | The page ends with instructions on how to cancel a plan rather than providing a clear next step for plant care. | Open your account page, choose Plans, then choose Cancel plan. | high | Replace the account cancellation text with a clear next step, such as signing up for a care plan or reading another guide. | draft |
| F019 | medium | index.html | Content positioning | The main headline is vague and does not convey the page's value to the reader. | # Stuff about plants | high | Update the main headline to clearly express Leafline's core offering and value. | draft |
| F020 | medium | index.html | Duplicate content | Paragraph is 100% identical to one on about.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F021 | medium | index.html | Missing images and alt text | Image has no alt text | images/hero.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F022 | medium | news.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F023 | medium | news.html | User-friendliness | No clear next action or link to book the workshop. | Our autumn repotting workshop is open for booking. | high | Add a call-to-action link or explicit instructions on how readers can book the workshop. | draft |
| F024 | medium | pest-guide.html | Traditional SEO | Missing meta description | (no meta description) | rule | Add a one-sentence meta description (under 160 characters) summarising the page. | draft |
| F025 | medium | pricing.html | Content positioning | The main headline does not describe the value or content of the pricing page. | # Welcome | high | Update the main heading to clearly reflect the page's purpose. | draft |
| F026 | medium | pricing.html | Content positioning | The page opens with historical background rather than delivering immediately on its purpose as a pricing page. | Houseplants have a long history. The Victorians built glass cases called Wardian cases to carry ferns across oceans, | high | Remove or relocate the historical text so subscription plan details appear immediately at the top. | draft |
| F027 | medium | watering-guide.html | Duplicate content | Paragraph is 99% identical to one on beginner-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F028 | low | faq.html | Accessibility basics | Vague link text | click here | rule | Rewrite the link text to describe the destination, e.g. 'See how to cancel your plan'. | draft |
| F029 | low | faq.html | GEO readiness | FAQ page has no FAQ structured data | (no FAQPage schema) | rule | Add FAQPage JSON-LD listing each question and answer. | draft |
| F030 | low | watering-guide.html | Accessibility basics | Heading level skipped (H1 to H4) | <h4>Why watering is tricky</h4> | rule | Change this heading to H2, or add the missing level above it. | draft |

## Rubric scores (1 = clearly fails, 5 = excellent)

| Page | Scannable | Plain language | Clear steps | Next action | Audience | Headline | Answers visit | Site goal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| about.html | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 5 |
| beginner-guide.html | 3 | 1 | 1 | 2 | 1 | 5 | 3 | 2 |
| faq.html | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 |
| index.html | 5 | 5 | 5 | 4 | 4 | 1 | 4 | 4 |
| news.html | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 5 |
| pricing.html | 4 | 5 | 5 | 1 | 4 | 1 | 2 | 3 |
