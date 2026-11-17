# Content audit: practice-site

Audited 8 pages on 2026-11-11_15-37. Found 15 issues: 2 high, 10 medium, 3 low.

## Top priorities

1. Missing page title on faq.html
2. Broken internal link on index.html
3. Paragraph is 100% identical to one on index.html on about.html

## All issues

| ID | Severity | Page | Check | Issue | Evidence | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F001 | high | faq.html | Traditional SEO | Missing page title | (no <title> element) | Add a <title> that names the page topic and the site, e.g. 'FAQ | Leafline'. | draft |
| F002 | high | index.html | Traditional SEO | Broken internal link | shop.html | Create shop.html or point the link to an existing page. | draft |
| F003 | medium | about.html | Duplicate content | Paragraph is 100% identical to one on index.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F004 | medium | about.html | Missing images and alt text | Image has no alt text | images/team.svg | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F005 | medium | about.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | Give each page a unique title that names its topic. | draft |
| F006 | medium | beginner-guide.html | Duplicate content | Paragraph is 99% identical to one on watering-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F007 | medium | beginner-guide.html | Missing images and alt text | Image has no alt text | images/snake-plant.svg | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F008 | medium | index.html | Duplicate content | Paragraph is 100% identical to one on about.html | Leafline started as a small notebook of care tips shared between neighbours. Today we help... | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F009 | medium | index.html | Missing images and alt text | Image has no alt text | images/hero.svg | Add alt text describing what the image shows, or alt="" if it is purely decorative. | draft |
| F010 | medium | news.html | Traditional SEO | Duplicate page title | <title>Leafline</title> | Give each page a unique title that names its topic. | draft |
| F011 | medium | pest-guide.html | Traditional SEO | Missing meta description | (no meta description) | Add a one-sentence meta description (under 160 characters) summarising the page. | draft |
| F012 | medium | watering-guide.html | Duplicate content | Paragraph is 99% identical to one on beginner-guide.html | Good drainage matters more than most people think. Always choose a pot with a hole in the ... | Keep the paragraph on the most relevant page and link to it from the other. | draft |
| F013 | low | faq.html | Accessibility basics | Vague link text | click here | Rewrite the link text to describe the destination, e.g. 'See how to cancel your plan'. | draft |
| F014 | low | faq.html | GEO readiness | FAQ page has no FAQ structured data | (no FAQPage schema) | Add FAQPage JSON-LD listing each question and answer. | draft |
| F015 | low | watering-guide.html | Accessibility basics | Heading level skipped (H1 to H4) | <h4>Why watering is tricky</h4> | Change this heading to H2, or add the missing level above it. | draft |
