# Content audit: practice-site

Audited 8 pages on 2026-11-11_18-07. Found 39 issues: 10 high, 25 medium, 4 low.

AI model used: gemini-3.5-flash. AI calls: 23. Findings dropped for missing evidence: 0. Escalated to a human: 3.

## Top priorities

1. Directs readers to cancel their subscription plan, contradicting the site goal of converting readers to monthly care plans. on beginner-guide.html
2. Uses technical jargon ('rhizosphere oxygenation', 'cation exchange capacity', 'edaphic requirements') unsuited for complete beginners. on beginner-guide.html
3. Missing page title on faq.html

## Escalated to a human (no suggested fix)

- F002 (beginner-guide.html): beginner-guide.html says to water snake plants every 2-3 weeks and let soil dry out completely, while watering-guide.html advises watering once a week and never letting soil dry out completely.. Reason: agent can't verify which statement is correct.
- F004 (faq.html): The monthly price of the Basic plan is listed as $15 on faq.html but $12 on pricing.html.. Reason: involves pricing; agent can't verify which statement is correct.
- F005 (faq.html): The threshold for free shipping is stated as $75 on faq.html but $50 on index.html.. Reason: involves pricing; agent can't verify which statement is correct.

## All issues

| ID | Severity | Page | Check | Issue | Evidence | Confidence | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F001 | high | beginner-guide.html | Content positioning | Directs readers to cancel their subscription plan, contradicting the site goal of converting readers to monthly care plans. | Open your account page, choose Plans, then choose Cancel plan. | high | Replace cancellation instructions with a call to action promoting Leafline's monthly plant care plans. | draft |
| F002 | high | beginner-guide.html | Contradictory content | beginner-guide.html says to water snake plants every 2-3 weeks and let soil dry out completely, while watering-guide.html advises watering once a week and never letting soil dry out completely. | beginner-guide.html: "Water your snake plant every two to three weeks, letting the soil dry out completely between waterings." / watering-guide.html: "Water snake plants once a week so the soil never dries out completely." | high | - | escalated |
| F003 | high | beginner-guide.html | User-friendliness | Uses technical jargon ('rhizosphere oxygenation', 'cation exchange capacity', 'edaphic requirements') unsuited for complete beginners. | Ensure substrate aeration via perlite amendment to optimise rhizosphere oxygenation, and calibrate the substrate's cation exchange capacity relative to your cultivar's edaphic requirements. | high | Rewrite soil preparation instructions using everyday language. | draft |
| F004 | high | faq.html | Contradictory content | The monthly price of the Basic plan is listed as $15 on faq.html but $12 on pricing.html. | faq.html: "The Basic plan costs $15 per month and includes one care guide each month plus email support." / pricing.html: "Basic plan: $12 per month. One care guide per month and email support." | high | - | escalated |
| F005 | high | faq.html | Contradictory content | The threshold for free shipping is stated as $75 on faq.html but $50 on index.html. | faq.html: "Yes, shipping is free on orders over $75." / index.html: "Enjoy free shipping on all orders over $50." | high | - | escalated |
| F006 | high | faq.html | Traditional SEO | Missing page title | (no <title> element) | rule | Add a <title> that names the page topic and the site, e.g. 'FAQ / Leafline'. | draft |
| F007 | high | index.html | Outdated content | The app launch is presented as an upcoming event in March 2022, which is years in the past relative to today's date (2026-11-11). | Our new mobile app launches next month (March 2022)! | high | Verify the current availability of the app and ask the site owner to update or remove the announcement. | draft |
| F008 | high | index.html | Traditional SEO | Broken internal link | shop.html | rule | Create shop.html or point the link to an existing page. | draft |
| F009 | high | pricing.html | User-friendliness | The page lacks a clear next action for readers to select or purchase a subscription plan. | Premium plan: $25 per month. Everything in Basic, plus a seasonal fertilizer box and video calls with a plant expert. | high | Add sign-up buttons or clear action links beneath each plan description. | draft |
| F010 | high | watering-guide.html | Content positioning | The page fails to support the site goal of converting readers to a monthly care plan. | soggy soil is the most common cause of root rot in indoor plants. | high | Include a section or banner inviting readers to sign up for Leafline's monthly plant care plan. | draft |
| F011 | medium | about.html | Duplicate content | Paragraph is 100% identical to one on index.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F012 | medium | about.html | Missing images and alt text | Image has no alt text | images/team.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F013 | medium | about.html | Outdated content | The page promotes summer 2021 internships as currently available, which is out of date. | We are currently hiring for summer 2021 internships. Apply before the end of May! | high | Verify current hiring needs and update or remove the internship announcement. | draft |
| F014 | medium | about.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F015 | medium | about.html | User-friendliness | The 'Stay up to date' section contains no clear next action or subscription method for the reader. | ## Stay up to date | high | Add an input form, link, or instruction explaining how readers can stay up to date. | draft |
| F016 | medium | beginner-guide.html | Duplicate content | Paragraph is 99% identical to one on watering-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F017 | medium | beginner-guide.html | GEO readiness | The guide lacks a direct summary answer to basic beginner plant care near the top. | This guide is written for complete beginners who have never kept a plant alive. | high | Add a short summary at the start explaining the core rules of beginner plant care (light, watering, and soil). | draft |
| F018 | medium | beginner-guide.html | Missing images and alt text | Image has no alt text | images/snake-plant.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F019 | medium | beginner-guide.html | Outdated content | Refers to 2020 as 'this year's top pick', which is outdated given today's date of 2026-11-11. | Our 2020 Plant of the Year is the snake plant, and it is this year's top pick for new plant owners. | high | Verify and update the plant recommendation to reflect the current year. | draft |
| F020 | medium | beginner-guide.html | User-friendliness | Potting instructions are presented in a single run-on sentence without clear numbered steps. | first you get a pot that is a bit bigger than the plant and then you put some soil in the bottom and then | high | Format the potting instructions as a numbered list with one distinct action per step. | draft |
| F021 | medium | faq.html | User-friendliness | Clear steps: Instructions for cancelling a plan are not presented as direct numbered steps, requiring the user to click away. | To see the steps, click here . | high | Replace the generic link text with clear, numbered inline cancellation steps. | draft |
| F022 | medium | index.html | Content positioning | Headline clarity scored 1 because the main heading is vague and does not convey the value of the page or brand. | # Stuff about plants | high | Rewrite the main heading to clearly reflect Leafline's core offering of practical plant care guides and subscriptions. | draft |
| F023 | medium | index.html | Duplicate content | Paragraph is 100% identical to one on about.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F024 | medium | index.html | Missing images and alt text | Image has no alt text | images/hero.svg | rule | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F025 | medium | news.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | rule | Give each page a unique title that names its topic. | draft |
| F026 | medium | news.html | User-friendliness | The page states that the workshop is open for booking but provides no clear next step, link, or instructions on how to book. | Our autumn repotting workshop is open for booking. | high | Add a link, button, or explicit instructions telling readers where and how to reserve their spot. | draft |
| F027 | medium | pest-guide.html | Missing images and alt text | The page text references a photo to help identify spider mites, but no photo is provided. | shown in the photo below. Compare your leaves with it | high | Add an image showing spider mite webbing and stippling directly below the section heading, or update the text if no image is available. | draft |
| F028 | medium | pest-guide.html | Traditional SEO | Missing meta description | (no meta description) | rule | Add a one-sentence meta description (under 160 characters) summarising the page. | draft |
| F029 | medium | pricing.html | Content positioning | The main headline 'Welcome' does not explain the page's purpose or value. | # Welcome | high | Update the headline to clearly indicate care plans and pricing. | draft |
| F030 | medium | pricing.html | Content positioning | The page opens with historical commentary about houseplants instead of focusing on pricing and plans. | Houseplants have a long history. The Victorians built glass cases called Wardian cases to carry ferns across oceans, and by the late nineteenth century | high | Remove or condense the introductory history paragraph to bring plan pricing to the top. | draft |
| F031 | medium | watering-guide.html | Duplicate content | Paragraph is 99% identical to one on beginner-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | rule | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F032 | medium | watering-guide.html | GEO readiness | The guide does not offer a concise direct summary at the top answering how to water indoor plants. | #### Why watering is tricky | high | Add a 1-2 sentence direct summary under the main headline explaining the core rule of plant watering. | draft |
| F033 | medium | watering-guide.html | User-friendliness | Text under 'Why watering is tricky' is a single long run-on paragraph, making the content hard to scan. | Watering is something every plant owner thinks about and there are a lot of different opinions about it, which can make it confusing, because | high | Break the section into short paragraphs of 4 sentences or fewer with bullet points for key factors like light and pot material. | draft |
| F034 | medium | watering-guide.html | User-friendliness | Watering and drainage instructions are buried in long sentences rather than presented as sequential steps. | Always choose a pot with a hole in the bottom, empty the saucer about thirty minutes after watering, and never let the roots sit | high | Format instructions as a numbered list with one distinct action per step. | draft |
| F035 | medium | watering-guide.html | User-friendliness | The page ends without providing any clear next step or call to action. | soggy soil is the most common cause of root rot in indoor plants. | high | Add a prominent link or button at the bottom directing readers to related guides or care plans. | draft |
| F036 | low | faq.html | Accessibility basics | Vague link text | click here | rule | Rewrite the link text to describe the destination, e.g. 'See how to cancel your plan'. | draft |
| F037 | low | faq.html | GEO readiness | FAQ page has no FAQ structured data | (no FAQPage schema) | rule | Add FAQPage JSON-LD listing each question and answer. | draft |
| F038 | low | pest-guide.html | User-friendliness | The page ends without a clear next action or call to action for the reader. | Quarantine new plants for two weeks and keep humidity steady. | high | Add a clear next action at the bottom of the page linking readers to related guides or Leafline care subscriptions. | draft |
| F039 | low | watering-guide.html | Accessibility basics | Heading level skipped (H1 to H4) | <h4>Why watering is tricky</h4> | rule | Change this heading to H2, or add the missing level above it. | draft |

## Rubric scores (1 = clearly fails, 5 = excellent)

| Page | Scannable | Plain language | Clear steps | Next action | Audience | Headline | Answers visit | Site goal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| about.html | 4 | 5 | 5 | 2 | 4 | 4 | 4 | 4 |
| beginner-guide.html | 3 | 1 | 1 | 1 | 1 | 5 | 3 | 1 |
| faq.html | 5 | 5 | 2 | 4 | 5 | 5 | 5 | 5 |
| index.html | 4 | 5 | 5 | 4 | 4 | 1 | 4 | 4 |
| news.html | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 4 |
| pest-guide.html | 5 | 5 | 3 | 2 | 5 | 5 | 5 | 3 |
| pricing.html | 4 | 5 | 5 | 1 | 4 | 1 | 2 | 3 |
| watering-guide.html | 1 | 5 | 1 | 1 | 4 | 4 | 3 | 2 |
