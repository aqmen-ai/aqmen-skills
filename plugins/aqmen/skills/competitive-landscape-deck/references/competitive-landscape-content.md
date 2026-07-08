# Competitive Landscape — content (shared)

The **format-agnostic** spec of *what* an aqmen competitive landscape deliverable
covers: the narrative, the topics and their so-whats, the module rules, and what
to gather from the aqmen MCP. Both formats render **this** content and differ
only in presentation:

- **HTML report** → `competitive-landscape-structure.md` (document sections + ECharts)
- **PPTX deck** → `competitive-landscape-deck-structure.md` (slide sequence + `aqmen_deck.py`)

This file is the single source of truth for content, so the two formats never
drift. Read it alongside `report-standards.md` (voice, base-first, sources &
confidence) and `report-data.md` (how to pull the analysis). Build only once you
have the whole grid; never invent numbers or sources.

## Objective

Benchmark the players and locate where the target can win, to inform a specific
decision. State the question answered and the market definition/geography that
bound the player set. Lead the deliverable with the headline takeaway — who wins
where, and the so-what.

## What the deliverable must cover

Each topic below carries a so-what; the format docs decide how to render it (a
report section vs. one or more slides). The order mirrors how aqmen builds the
analysis. Omit a topic only if it genuinely doesn't apply, and say so.

1. **Objective & scope of use** — the question answered and the decision it
   informs; the market definition and geography bounding the player set. Headline
   takeaway stated up front.
2. **Data landscape** — the disclosure-quality scan (filings, investor materials,
   databases) and where data on players is thin.
3. **Player set, tiering & archetypes** — the companies covered, tiered by role
   (**main** = full coverage vs **other** = long-tail, revenue-only), and grouped
   into **archetypes** where the economics differ by group. Explain the long-list
   → shortlist logic.
4. **Comparison framework** — the fields/criteria collected and why each is
   decision-relevant (not decorative). Note units (percentages as rates).
5. **The benchmark** — the players × fields comparison itself: the measured grid
   plus a relative benchmark of the decision criteria. Highlight the standout
   figures; keep it readable.
6. **Positioning** — who's winning share, how players cluster, and points of
   differentiation; where each archetype wins.
7. **Reliability review** — coverage rated strong / moderate / weak, with sparse
   fields or rows **called out explicitly**. Never imply completeness.
8. **So-what / implications** — competitive relevance, whitespace, who's
   vulnerable, and the strategic implications for the decision.
9. **Scenarios** — if any: the focused assertion changes vs Base and what they
   imply. Base first.
10. **Sources & confidence** — attribution for every quantitative claim (source,
    confidence 1–5, note), per `report-standards.md`.

## Module rules (analytical non-negotiables)

- Compare **apples to apples** — same definition and period across players.
- Be explicit about **tiering**: don't present an `other` (revenue-only) player
  as if it had full coverage.
- Frame players by **archetype** before ranking; a benchmark of relative standing
  (weakest → strongest on each criterion) is not an absolute score — say so.
- Percentages/shares: **state the denominator** (share of what, over what period).
- The **reliability review is mandatory** — sparse cells and thin rows must be
  visible, not hidden behind a tidy-looking grid.
- Web-sourced figures use source type `web` with the URL; never `ai` for anything
  found online (see `report-standards.md`).

## What to gather from aqmen

See `report-data.md` for the shared flow. For competitive landscape, gather:

- the **dataset grid** — the fields (with format/unit) and the players, noting
  each player's **tier** (full-coverage vs revenue-only) and **archetype**;
- each cell's **value with its source, confidence (1–5), and note**;
- any **purchase criteria / KPC** weighting and how it varies by buyer or deal
  size;
- the **list of sources** used;
- the **scenarios** (competitive landscape has no qualitative levers).
