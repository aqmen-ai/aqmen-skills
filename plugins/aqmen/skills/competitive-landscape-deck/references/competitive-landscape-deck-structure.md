# Competitive Landscape Deck — structure (PPTX)

How to render the competitive landscape **content** as an editable `.pptx` deck.
`competitive-landscape-content.md` is the single source of truth for *what* to
cover, the module rules, and what to gather from aqmen — read it first. This file
covers only *how* to stage that content as slides. Also read
`report-standards.md` (voice, sources, confidence) and `deck-style.md` (design
system + builder); build with `aqmen_deck.py`.

## Slide order

Stage the content topics as this slide sequence (omit one only if it genuinely
doesn't apply, and say so):

| # | Builder method | Slide (content topic) |
| --- | --- | --- |
| 1 | `title_slide` | Cover — title, subtitle, current year |
| 2 | `agenda` | Agenda (highlight the landscape section) |
| 3 | `executive_summary` | The one-page answer — who wins where, and the so-what |
| 4 | `content_slide` | Player set, tiering & archetypes |
| 5 | `revenue_build_slide` | **Revenue build** — THE flagship: each player's `revenue × % addressable = market revenue`, summed bottom-up to the market. Lead with this |
| 6 | `positioning_matrix_slide` | **Archetype map** — each archetype as the bounding box of its players' `points`; dots per player, names live in the revenue build |
| 7 | `content_slide` | Comparison framework — the criteria and why each matters |
| 8 | `harvey_matrix_slide` | **Player × criteria benchmark** — harvey-ball matrix (relative standing 0–1), optional `row_desc` |
| 9 | `chart_slide` (bar) | Quantitative comparison — a key measured field across players |
| 10 | `content_slide` | Positioning — where each archetype wins |
| 11 | `content_slide` | Reliability review — coverage strong/moderate/weak, gaps named |
| 12 | `content_slide` | So-what / implications — whitespace, threats |
| 13+ | `content_slide` per scenario | Scenarios (if any) — Base first |
| last | `content_slide` | Sources & confidence |

## Chart mapping (native `aqmen_deck` charts)

- **Revenue build** → `revenue_build_slide`: `groups` = (archetype, [player dicts])
  where each player has `revenue`, `pct` (% addressable) and `market_rev`; pass the
  bottom-up `total`. THE central competitive-landscape exhibit — lead with it.
- **Archetype map** → `positioning_matrix_slide`: each `MatrixItem` gives the
  archetype `points` (player x/y in 0–1); the box is their bounding rectangle.
  Names are omitted — they live in the revenue build.
- **Player × criteria benchmark** → `harvey_matrix_slide`: `columns` = players,
  each `HarveyRow` = a criterion with one 0–1 fill per player; use `row_desc` for
  a short definition column.
- **Measured field across players** → `chart_slide(kind="bar")` or `"column"`.
- **Share / mix over time** → `chart_slide(kind="stacked_column")`.

_Content, module rules (apples-to-apples, tiering, mandatory reliability review,
relative-not-absolute harvey standing, `web` not `ai`, …), and what to gather
from aqmen: see `competitive-landscape-content.md`._
