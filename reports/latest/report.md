# Content audit: practice-site

Audited 8 pages on 2026-11-12_15-13. Found 39 issues: 10 high, 26 medium, 3 low.


AI model used: gemini-3.6-flash. AI calls: 12. Findings dropped for missing evidence: 0. Escalated to a human: 5.

## Top priorities

1. The page ends by directing users to cancel their plan, opposing the site's goal of converting readers to a monthly care plan. on beginner-guide.html
2. Soil preparation instructions use complex botanical jargon inappropriate for beginners. on beginner-guide.html
3. Potting instructions are written as one long run-on sentence without clear numbered steps. on beginner-guide.html

## Escalated to a human (no suggested fix)

- F002 (beginner-guide.html): The beginner guide instructs to water snake plants every 2-3 weeks letting the soil dry out completely, whereas the watering guide instructs to water once a week so the soil never dries out completely.. Reason: agent can't verify which statement is correct.
- F005 (faq.html): The monthly cost for the Basic plan is stated as $15 on the FAQ page but $12 on the pricing page.. Reason: involves pricing; agent can't verify which statement is correct.
- F006 (faq.html): The free shipping order threshold is listed as $75 on the FAQ page but $50 on the homepage.. Reason: involves pricing; agent can't verify which statement is correct.
- F009 (pricing.html): The page content does not effectively guide the reader toward the site's goal of converting to a monthly care plan.. Reason: involves pricing.
- F010 (pricing.html): No clear next action or call-to-action button for visitors to subscribe to a plan.. Reason: involves pricing.

## All issues

| ID | Severity | Page | Check | Issue | Evidence | Confidence | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F001 | high | beginner-guide.html | Content positioning | The page ends by directing users to cancel their plan, opposing the site's goal of converting readers to a monthly care plan. | Open your account page, choose Plans, then choose Cancel plan. | high | Replace cancellation instructions with a call-to-action inviting readers to sign up for a care plan. | draft |
| F002 | high | beginner-guide.html | Contradictory content | The beginner guide instructs to water snake plants every 2-3 weeks letting the soil dry out completely, whereas the watering guide instructs to water once a week so the soil never dries out completely. | beginner-guide.html: "Water your snake plant every two to three weeks, letting the soil dry out completely between waterings." / watering-guide.html: "Water snake plants once a week so the soil never dries out completely." | high | - | escalated |
| F003 | high | beginner-guide.html | User-friendliness | Soil preparation instructions use complex botanical jargon inappropriate for beginners. | Ensure substrate aeration via perlite amendment to optimise rhizosphere oxygenation, and calibrate the substrate's cation exchange capacity relative to your cultivar's edaphic requirements. | high | Rewrite using plain language suitable for absolute beginners. | draft |
| F004 | high | beginner-guide.html | User-friendliness | Potting instructions are written as one long run-on sentence without clear numbered steps. | first you get a pot that is a bit bigger than the plant and then you put some soil in the bottom and then you take the | high | Format instructions as a numbered list with one step per line. | draft |
| F005 | high | faq.html | Contradictory content | The monthly cost for the Basic plan is stated as $15 on the FAQ page but $12 on the pricing page. | faq.html: "The Basic plan costs $15 per month and includes one care guide each month plus email support." / pricing.html: "Basic plan: $12 per month. One care guide per month and email support." | high | - | escalated |
| F006 | high | faq.html | Contradictory content | The free shipping order threshold is listed as $75 on the FAQ page but $50 on the homepage. | faq.html: "Yes, shipping is free on orders over $75." / index.html: "Enjoy free shipping on all orders over $50." | high | - | escalated |
| F007 | high | faq.html | Traditional SEO | Missing page title | (no <title> element) | rule | Add a <title> that names the page topic and the site, e.g. 'FAQ / Leafline'. | draft |
| F008 | high | index.html | Traditional SEO | Broken internal link | shop.html | rule | Create shop.html or point the link to an existing page. | draft |
| F009 | high | pricing.html | Content positioning | The page content does not effectively guide the reader toward the site's goal of converting to a monthly care plan. | Basic plan: $12 per month. One care guide per month and email support. | high | - | escalated |
| F010 | high | pricing.html | User-friendliness | No clear next action or call-to-action button for visitors to subscribe to a plan. | Premium plan: $25 per month. Everything in Basic, plus a seasonal fertilizer box and video calls with a plant expert. | high | - | escalated |
| F011 | medium | about.html | Duplicate content | Paragraph is 100% identical to one on index.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F012 | medium | about.html | Missing images and alt text | Image has no alt text | images/team.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F013 | medium | about.html | Outdated content | The page promotes summer 2021 internships as currently available. | We are currently hiring for summer 2021 internships. Apply before the end of May! | high | Ask the page owner to verify current internship openings and update or remove the expired hiring notice. | draft |
| F014 | medium | about.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F015 | medium | about.html | User-friendliness | The section header 'Stay up to date' lacks a clear next action, link, or subscription form. | ## Stay up to date | high | Add a clear call to action, such as a newsletter sign-up form or a link to subscribe to plant-care updates. | draft |
| F016 | medium | beginner-guide.html | Duplicate content | Paragraph is 99% identical to one on watering-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F017 | medium | beginner-guide.html | Missing images and alt text | Image has no alt text | images/snake-plant.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F018 | medium | beginner-guide.html | Outdated content | Page describes 2020 as 'this year's top pick' when current date is in 2026. | Our 2020 Plant of the Year is the snake plant, and it is this year's top pick for new plant owners. | high | Ask the page owner to verify and update the current year's recommendation. | draft |
| F019 | medium | index.html | Content positioning | The headline 'Stuff about plants' fails to state the page's value or tell readers what Leafline provides. | Stuff about plants | high | Update the headline to clearly state the value offered to the reader. | draft |
| F020 | medium | index.html | Duplicate content | Paragraph is 100% identical to one on about.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F021 | medium | index.html | Missing images and alt text | Image has no alt text | images/hero.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F022 | medium | index.html | Outdated content | The page presents a March 2022 mobile app launch date as an upcoming event, which is outdated. | Our new mobile app launches next month (March 2022)! Sign up to be the first to try it. | high | Verify the current status of the mobile app release and update or remove this announcement. | draft |
| F023 | medium | news.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F024 | medium | news.html | User-friendliness | Missing a clear next action or link for booking the workshop. | Our autumn repotting workshop is open for booking. | high | Add a link, button, or clear instruction on how readers can sign up for the workshop. | draft |
| F025 | medium | pest-guide.html | Content positioning | The page does not move the reader toward the site's goal of converting to a monthly care plan. | This guide is for experienced growers who already know basic plant care and want a systematic approach to pests. | high | Include a section or banner explaining how Leafline's monthly care plan offers advanced pest consultation and specialized treatments for experienced growers. | draft |
| F026 | medium | pest-guide.html | Missing images and alt text | The text references a photo showing spider mite damage, but no photo is present on the page. | Identify spider mites by the fine webbing and stippling pattern shown in the photo below. | high | Add the missing photo of spider mite webbing and stippling, or update the sentence to describe the symptoms without referring to a photo. | draft |
| F027 | medium | pest-guide.html | Traditional SEO | Missing meta description | (no meta description) | rule | Add a one-sentence meta description (under 160 characters) summarising the page. | draft |
| F028 | medium | pest-guide.html | User-friendliness | The page lacks a clear next action or call to action at the end. | Quarantine new plants for two weeks and keep humidity steady. | high | Add a clear call to action at the end of the guide leading readers to a related topic or to sign up for Leafline's plant care services. | draft |
| F029 | medium | pricing.html | Content positioning | Headline does not state what value the page offers to the reader. | # Welcome | high | Update the headline to clearly describe the page content and value. | draft |
| F030 | medium | pricing.html | Content positioning | The page spends most of its content on houseplant history rather than answering the intent of a pricing page. | Houseplants have a long history. The Victorians built glass cases called Wardian cases to carry ferns across oceans, and by the late nineteenth century | high | Remove or shorten the historical background paragraph and focus on subscription features and pricing. | draft |
| F031 | medium | watering-guide.html | Content positioning | The content does not support the site goal of converting readers into monthly care plan subscribers. | # The watering guide | high | Include a section or callout showing how Leafline's monthly care plan helps automate and personalize watering schedules for subscribers. | draft |
| F032 | medium | watering-guide.html | Duplicate content | Paragraph is 99% identical to one on beginner-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F033 | medium | watering-guide.html | GEO readiness | The guide does not provide a direct, concise summary answer to plant watering near the top of the page. | # The watering guide | high | Add a 2-3 sentence overview block right under the title summarizing the golden rule of watering plants. | draft |
| F034 | medium | watering-guide.html | User-friendliness | The introductory section is formatted as a single long block of text with one 170+ word sentence, making it difficult to scan. | Watering is something every plant owner thinks about and there are a lot of different opinions about it, which can make it confusing, because | high | Break the paragraph into short sentences of 4 sentences or fewer, using bullet points for factors like pot material and foliage. | draft |
| F035 | medium | watering-guide.html | User-friendliness | Drainage instructions are presented as paragraph text rather than numbered steps. | Always choose a pot with a hole in the bottom, empty the saucer about thirty minutes after watering, and never let the roots sit | high | Format the drainage instructions into clear, numbered steps. | draft |
| F036 | medium | watering-guide.html | User-friendliness | The page lacks a clear next action, leaving the reader with no direction after finishing the content. | never let the roots sit in standing water, because soggy soil is the most common cause of root rot in indoor plants. | high | Add a prominent call to action button or link at the end of the guide leading to related articles or subscription plans. | draft |
| F037 | low | faq.html | Accessibility basics | Vague link text | click here | rule | Rewrite the link text to describe the destination, e.g. 'See how to cancel your plan'. | draft |
| F038 | low | faq.html | GEO readiness | FAQ page has no FAQ structured data | (no FAQPage schema) | rule | Add FAQPage JSON-LD listing each question and answer. | draft |
| F039 | low | watering-guide.html | Accessibility basics | Heading level skipped (H1 to H4) | <h4>Why watering is tricky</h4> | rule | Change this heading to H2, or add the missing level above it. | draft |

## Rubric scores (1 = clearly fails, 5 = excellent)

| Page | Scannable | Plain language | Clear steps | Next action | Audience | Headline | Answers visit | Site goal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| about.html | 5 | 5 | 5 | 1 | 5 | 5 | 5 | 4 |
| beginner-guide.html | 2 | 1 | 1 | 1 | 1 | 5 | 2 | 1 |
| faq.html | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 |
| index.html | 5 | 5 | 5 | 4 | 4 | 1 | 4 | 4 |
| news.html | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 4 |
| pest-guide.html | 5 | 5 | 4 | 1 | 5 | 5 | 5 | 2 |
| pricing.html | 4 | 5 | 5 | 1 | 4 | 1 | 2 | 2 |
| watering-guide.html | 1 | 5 | 2 | 1 | 4 | 4 | 3 | 1 |
