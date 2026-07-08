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
| 5 | `content_slide` | Comparison framework — the criteria and why each matters |
| 6 | `harvey_matrix_slide` | **Player × criteria benchmark** — the flagship harvey-ball matrix (relative standing 0–1), optional `row_desc` |
| 7 | `chart_slide` (bar) | Quantitative comparison — a key measured field across players |
| 8 | `content_slide` | Positioning — where each archetype wins |
| 9 | `content_slide` | Reliability review — coverage strong/moderate/weak, gaps named |
| 10 | `content_slide` | So-what / implications — whitespace, threats |
| 11+ | `content_slide` per scenario | Scenarios (if any) — Base first |
| last | `content_slide` | Sources & confidence |

## Chart mapping (native `aqmen_deck` charts)

- **Player × criteria benchmark** → `harvey_matrix_slide`: `columns` = players,
  each `HarveyRow` = a criterion with one 0–1 fill per player; use `row_desc` for
  a short definition column.
- **Measured field across players** → `chart_slide(kind="bar")` (horizontal reads
  well with player names) or `"column"`.
- **Share / mix over time** → `chart_slide(kind="stacked_column")`.

_Content, module rules (apples-to-apples, tiering, mandatory reliability review,
relative-not-absolute harvey standing, `web` not `ai`, …), and what to gather
from aqmen: see `competitive-landscape-content.md`._
