# Competitive Landscape Report — structure

The fixed section order for a competitive landscape output report. It mirrors how
aqmen builds a competitive landscape (goal → research → player set → fields →
grid → positioning → reliability → implications), so the report reads as the
conclusion of that build. Omit a section only if it genuinely doesn't apply, and
say so.

Read `report-standards.md` (tone, sources, confidence) and `report-style.md`
(design) first. Use `report-template.html` as the skeleton.

## Sections

1. **Objective & scope of use** — the question the landscape answers and the
   decision it informs; the market definition and geography that bound the
   player set. Lead with the headline takeaway in one line.
2. **Data landscape** — the disclosure-quality scan (filings, investor materials,
   databases) and where data on players is thin.
3. **Player set & tiering** — the companies covered, tiered by role: **main**
   (full coverage) vs **other** (long-tail, revenue-only). Explain the long-list
   → shortlist logic.
4. **Comparison framework** — the fields collected (metrics/attributes) and why
   each is decision-relevant. Note units (percentages as rates).
5. **The landscape grid** — the players × fields comparison itself: a table of
   the key metrics. Keep it readable; highlight the standout figures.
6. **Positioning & archetypes** — who's winning share, how players cluster,
   points of differentiation. A positioning chart (e.g. scatter on two axes) if
   it clarifies.
7. **Reliability review** — coverage rated strong / moderate / weak, with sparse
   fields or rows **called out explicitly**. Do not imply completeness.
8. **So-what** — competitive relevance, who's vulnerable, and the strategic
   implications for the decision.
9. **Scenarios** — if any: the focused assertion changes vs Base and what they
   imply. Base first.
10. **Sources & confidence** — the shared closing table (see `report-standards.md`).

## Competitive-landscape specifics

- Be explicit about **tiering**: don't present `other` (revenue-only) players as
  if they had full coverage.
- Percentages/shares: state the denominator (share of what, over what period).
- The reliability review is not optional — sparse cells and thin rows must be
  visible, not hidden behind a tidy-looking grid.
- Web-sourced figures use source type `web` with the URL; never `ai` for
  anything found online (see `report-standards.md`).

## Suggested charts (ECharts)

- **Positioning** — a **scatter** on two decision-relevant axes (e.g. scale vs
  growth), bubble size for a third metric; label the main players.
- **Share / ranking** — a sorted horizontal **bar** of the key metric across
  players.
- **Benchmarking grid** — the players × fields **table** (sortable if useful);
  highlight standout cells.
- **Archetypes** — grouped bar or scatter clustering by strategy.

## What to gather from aqmen

See `report-data.md` for the shared flow. For a competitive landscape report,
gather:

- the **dataset grid** — the fields (with format/unit) and the players, noting
  each player's **tier** (full-coverage vs revenue-only — don't present a
  revenue-only player as fully covered);
- each cell's **value with its source, confidence (1–5), and note**;
- the **list of sources** used;
- the **scenarios** (competitive landscape has no qualitative levers).
