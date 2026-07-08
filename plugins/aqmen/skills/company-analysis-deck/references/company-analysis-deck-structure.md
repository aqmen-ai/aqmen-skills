# Company Analysis Deck — structure (PPTX)

How to render the company analysis **content** as an editable `.pptx` deck.
`company-analysis-content.md` is the single source of truth for *what* to cover,
the module rules, and what to gather from aqmen — read it first. This file covers
only *how* to stage that content as slides. Also read `report-standards.md`
(voice, sources, confidence) and `deck-style.md` (design system + builder); build
with `aqmen_deck.py`.

## Slide order

Stage the content topics as this slide sequence (omit one only if it genuinely
doesn't apply, and say so):

| # | Builder method | Slide (content topic) |
| --- | --- | --- |
| 1 | `title_slide` | Cover — target, subtitle, current year |
| 2 | `agenda` | Agenda (highlight the company-analysis section) |
| 3 | `executive_summary` | The one-page answer — the **valuation range** + value-creation so-whats |
| 4 | `content_slide` | Business & scope |
| 5 | `chart_slide` (column/line) | Revenue trajectory — historicals + forecast |
| 6 | `chart_slide` (stacked) | Margin / EBITDA bridge |
| 7 | `content_slide` | Operating drivers & KPIs — inputs vs computed flagged |
| 8 | `content_slide` | Working capital & cash flow |
| 9 | `chart_slide` (bar) | **DCF valuation** — EV as a **range**; terminal-value share as a sanity check; WACC stated |
| 10 | `chart_slide` (bar/tornado) | Sensitivity — value vs WACC / growth / margin |
| 11+ | `content_slide` per scenario | Scenarios — Initiative thesis in words, then overrides vs Base (Base first) |
| last | `content_slide` | Sources & confidence |

## Chart mapping (native `aqmen_deck` charts)

- **Revenue trajectory** → `chart_slide(kind="column")` or `"line"`.
- **Margin / EBITDA bridge** → `chart_slide(kind="stacked_column")` approximating
  a waterfall (start, +/– driver bars, end), or a grouped column by period.
- **DCF valuation range** → `chart_slide(kind="bar")` with low/base/high, or a
  stacked bar splitting explicit-period vs terminal value.
- **Sensitivity** → `chart_slide(kind="bar")` ranked, or a diverging tornado.

_Content, module rules (valuation as a range + terminal-value sanity check,
inputs vs computed, …), and what to gather from aqmen: see
`company-analysis-content.md`._
