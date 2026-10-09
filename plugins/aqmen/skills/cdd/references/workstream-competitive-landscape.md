# Workstream: Competition (competitive landscape)

What the Competition part of a CDD deliverable covers, how each exhibit
reaches the deck, how the HTML report lays it out, and what to gather. The
**method** — the long list, tiering in SQL, fields and coverage, population,
reliability, archetypes, the so-what, the critics' checklist — is the
platform's `competitive-landscape` topic (after `modeling`). Read it before
building the landscape.

## Objective

Benchmark the players and locate where the target can win. State the
question answered and the market definition and geography that bound the
player set (the Market workstream's, unless the brief says otherwise). Lead
with who wins where, and the so-what.

## What the part must cover

Omit a topic only if it genuinely does not apply, and say so.

1. **Objective and scope of use** — the question, the decision, the market
   and geography bounding the set. Headline takeaway up front.
2. **Data landscape** — the disclosure scan and where player data is thin.
3. **Player set, tiering and archetypes** — the long list → tiers by
   addressable share (the platform's rule), archetypes where economics
   differ.
4. **Comparison framework** — the fields and why each is decision-relevant;
   units stated.
5. **The benchmark** — players × fields, the standout figures highlighted;
   a relative benchmark of the buying criteria.
6. **Positioning** — who is winning share, how players cluster, where each
   archetype wins.
7. **Reliability review** — strong / moderate / weak coverage, sparse
   fields and rows **called out**. Mandatory.
8. **So-what** — whitespace, who is vulnerable, the implications for the
   decision.
9. **Scenarios** — if any, Base first.
10. **Sources and confidence.**

## The slides — elements and sources

The platform's `competitive-landscape` topic ends with the sourceable
exhibits and the ones a slide cannot draw; follow it. In the storyline:

| Slide | Exhibit | How it reaches the slide |
| --- | --- | --- |
| Player set and archetypes | tiers, archetypes, rationale | typed; counts as `field`s of a chart over the landscape |
| Revenue build | revenue × % addressable = market revenue, by archetype, summed | `table` chart over the landscape transformation (or a horizontal `bar` of market revenue by player) |
| Share of the sized market | top players and the rest | `pie` or 100%-stacked `bar` chart; the top-five share as a `number` chart or `field` |
| Archetype map | archetypes on two axes | **rebuilt** 2×2: shapes per archetype, player positions as `field`s; or the sourceable cut — a `bar` by archetype |
| Benchmark / key buying factors | players × criteria | `table` chart with the ratings as text (the harvey matrix rebuilt), or a sourced `range` |
| A measured field across players | e.g. growth, margin | horizontal `bar` chart |
| Tier 1 profile | the core competitors | `table` chart |
| Reliability review | coverage by confidence | `bar` chart of fields by confidence, or typed with a watch-out |
| Implications | where the target wins | typed, validated insight headline |

## The HTML report — sections

1. Objective and scope of use — the headline takeaway in one line.
2. Data landscape.
3. Player set, tiering and archetypes — the long list → shortlist logic.
4. Comparison framework.
5. The benchmark — the revenue build (`table.rbuild`) first, then the
   harvey-ball table or a sorted bar.
6. Positioning — the archetype map (`.pmatrix`).
7. Reliability review.
8. So-what and implications.
9. Scenarios — if any, Base first.
10. Sources and confidence.

## Module rules

- **Apples to apples**: same definition, period and currency across
  players, or labelled.
- **Tiering explicit**: a light-touch Tier 3 player is never shown as if
  fully covered.
- **Archetypes before ranking**; a relative benchmark is not an absolute
  score — say so.
- Shares **state their denominator** (share of what, over what period).
- The **reliability review is mandatory**: sparse cells visible, never
  hidden behind a tidy grid.
- A private company's revenue estimate is labelled an estimate.

## What to gather

- The **brief**: decision, questions, market definition, geography,
  currency.
- The **landscape table** (the transformation's output): one row per
  player, the fields with unit and scale, tier, archetype, market revenue,
  the row's confidence.
- The **players**, **addressable_share** and **archetypes** datasets, with
  the rationale per assignment.
- Per field, the **datasets** its values come from: sources,
  `confidence` and `source_url` columns.
- The **charts** and **views** over the landscape.
- The **insights**: who is winning and why, who is losing ground, the
  trends underneath.
