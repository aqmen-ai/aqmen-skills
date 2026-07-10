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
| 6 | `driver_tree_slide` | **Market expression & drivers** — expression tree (market expression → variables w/ formulas → leaf drivers) + certainty dots; note segmentation, don't explode it |
| 7 | `marimekko_slide` | **Headline TAM view** — flagship Mekko: width = region size, height = `SAM` (solid) + `Whitespace` (hatched) |
| 8 | `marimekko_slide` | **SAM by region × dimension** — a second Mekko splitting the served market (e.g. by deal size) |
| 9 | `chart_slide` (stacked) | Trajectory by region — market evolution split by a dimension, CAGR called out |
| 10 | `chart_slide` (grouped) | Triangulation — bottom-up vs top-down |
| 11 | `chart_slide` (bar/tornado) | Sensitivity |
| 12+ | `content_slide` per scenario | Scenarios — Trend thesis in words, then overrides vs Base (Base first) |
| last | `content_slide` | Sources & confidence |

## Chart mapping (native `aqmen_deck` charts)

- **Market structure** → `driver_tree_slide` — the market **expression** → its
  **variables** (with `expr` formulas) → leaf **drivers**, per-parent ×/+
  operators, certainty dots. Keep it to variables/expressions; put "estimated per
  segment (…)" in `note`, don't draw a box per segment.
- **TAM by region** → `marimekko_slide` (one `MekkoColumn` per region; `width` =
  size, `segments` = `SAM` + `Whitespace` — the latter renders hatched). Use a
  **second** Mekko to split the SAM by another dimension (e.g. deal size).
- **Trajectory** → `chart_slide(kind="stacked_column")` split by region (evolution
  by dimension), or `"line"`/`"column"` for a single series.
- **Triangulation** → `chart_slide(kind="column")` with two series.
- **Sensitivity** → `chart_slide(kind="bar")` ranked, or a diverging tornado.

_Content, module rules (TAM/SAM/SOM distinct, label estimates, …), and what to
gather from aqmen: see `market-sizing-content.md`._
