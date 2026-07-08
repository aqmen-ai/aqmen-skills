# Market Sizing Deck — structure (PPTX)

How to render the market sizing **content** as an editable `.pptx` deck.
`market-sizing-content.md` is the single source of truth for *what* to cover, the
module rules, and what to gather from aqmen — read it first. This file covers
only *how* to stage that content as slides. Also read `report-standards.md`
(voice, sources, confidence) and `deck-style.md` (design system + builder); build
with `aqmen_deck.py`.

## Slide order

Stage the content topics as this slide sequence (omit one only if it genuinely
doesn't apply, and say so):

| # | Builder method | Slide (content topic) |
| --- | --- | --- |
| 1 | `title_slide` | Cover — title, subtitle, current year |
| 2 | `agenda` | Agenda (highlight the sizing section) |
| 3 | `executive_summary` | The one-page answer — headline TAM/SAM/SOM + so-whats |
| 4 | `content_slide` | Objective & scope |
| 5 | `content_slide` | Data landscape |
| 6 | `content_slide` | Segmentation & driver tree (levers that matter) |
| 7 | `marimekko_slide` | **Headline TAM view** — the flagship Mekko (width = one dimension, height = SAM/whitespace or sub-segments) |
| 8 | `chart_slide` (line/column) | Trajectory — base year + projection, CAGR called out |
| 9 | `chart_slide` (stacked) | Segmentation breakdown |
| 10 | `chart_slide` (grouped) | Triangulation — bottom-up vs top-down |
| 11 | `chart_slide` (bar/tornado) | Sensitivity |
| 12+ | `content_slide` per scenario | Scenarios — Trend thesis in words, then overrides vs Base (Base first) |
| last | `content_slide` | Sources & confidence |

## Chart mapping (native `aqmen_deck` charts)

- **TAM by region/segment** → `marimekko_slide` (one `MekkoColumn` per
  region/segment; `width` = size, `segments` = SAM/whitespace or sub-splits).
- **Trajectory** → `chart_slide(kind="line")` or `"column"`.
- **Segmentation breakdown** → `chart_slide(kind="stacked_column")`.
- **Triangulation** → `chart_slide(kind="column")` with two series.
- **Sensitivity** → `chart_slide(kind="bar")` ranked, or a diverging tornado.

_Content, module rules (TAM/SAM/SOM distinct, label estimates, …), and what to
gather from aqmen: see `market-sizing-content.md`._
