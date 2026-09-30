# The CDD storyline: four parts, one answer

This is the standard aqmen deliverable Miguel specified (23 Sep 2026): the
output a client or prospect sees at the end of a demo or a CDD, structured the
way a McKinsey-style commercial due diligence is structured. **Top-down, every
page answers a so-what, and the whole thing serves one question**: is there an
opportunity here, and what do you need to believe for it to be real?

The four parts are fixed. The exhibits inside each part are chosen from the
kinds in `content-format.md`; the mapping below says which kind carries which
topic. The three module content specs (`market-sizing-content.md`,
`competitive-landscape-content.md`, `company-analysis-content.md`) remain the
source of truth for analytical rules and for what to gather from aqmen; this
file only says how they combine into one document.

Write the **executive summary last**, from the headlines of the exhibits.

---

## Part 0 · Context (2–3 exhibits)

- **Objective & scope** (`content`): the question, the decision it informs, who
  asked. In/out of scope, geography, horizon, currency.
- **Data landscape** (`content`, with a `watchout`): what exists, what is thin,
  what had to be estimated.
- Optional: **The situation** (`content`): the client's position and why now
  (e.g. Moeve has just opened its flagship car wash and must decide how many to
  roll out).

## Part 1 · Market (8–11 exhibits)

The demand-side build aqmen is strongest at; supply is covered in Part 2.

1. **Market definition** (`content`): the scope; what is in and what is out;
   the underlying entity that spends (a person, a household, a company, a car).
2. **Methodology & driver tree** (`driver_tree`): market expression → variables
   → leaf drivers with certainty dots. The three sizing methods to choose from:
   volume only (how many buy), price × quantity (how many buy × how much), or
   attachment rate (share of a wider spend). Demand side: underlying market ×
   penetration/capture rate × behavioural variables (frequency, ticket) ×
   allocation.
3. **Headline size / whitespace, TAM → SAM** (`mekko`): width = the most
   relevant dimension (usually geography), height = SAM solid + Whitespace
   hatched. TAM is theoretical potential; SAM is the actual market used for
   share.
4. **The SAM today, by the cuts that matter** (`mekko` or `chart`
   stacked): which segments are large. Mekko when two dimensions matter.
5. **Trends** (`table`, columns Trend · Driver hit · Direction · Rationale;
   or `content`): grouped as macro, regulatory, consumer habits. Each trend
   names the driver it moves and whether it helps or hurts.
6. **Trajectory** (`chart` stacked_column or line): five years back, five
   forward, total and by the key dimension, CAGR in the headline.
7. **Growth by segment** (`chart`): which segments are attractive; where the
   opportunity sits.
8. **Driver detail** (one or two `chart`s): how the key drivers evolve
   (penetration, frequency, ticket) and what moves them.
9. **Appendix — triangulation** (`chart` column, two series): our size vs
   public sources, like-for-like or adjusted, with the adjustment stated.
10. **Appendix — sanity check** (`content`): quick back-of-envelope tests that
    ground the number (units per capita, revenue per site, minutes per wash).
11. **Sensitivity** (`chart` bar, Low/High series) and **scenarios**
    (`scenario`, base first).

## Part 2 · Competition (5–7 exhibits)

1. **Player set & archetypes** (`content`): who is in, tiered; the archetypes
   and why economics differ between them.
2. **Revenue build** (`revenue_build`): revenue × % addressable = market
   revenue per player, summed bottom-up; reconcile with Part 1.
3. **Archetype map** (`positioning`): a 2×2 (e.g. reach × breadth of offer,
   forecourt vs standalone × automated vs manual). Archetypes matter because
   they predict behaviour; names live in the revenue build.
4. **Competitive trends** (`content`): consolidation, integration, entry of
   new formats, and what each implies for each archetype.
5. **Key buying factors** (`harvey` matrix players × criteria, plus a
   `table` of criteria with importance scores where interviews exist).
6. **Positioning / implications** (`content`): where each archetype wins;
   whitespace for the client.
7. **Reliability review** (`content` with `watchout`): coverage strong /
   moderate / weak.

## Part 3 · Company (5–8 exhibits) — two variants

**Corporate variant** (an operating business): follow
`company-analysis-content.md`: description, business lines and shareholding
(`content`), financials revenue/EBITDA/net income (`chart`), operating KPIs
(`content` or `chart`), margin bridge (`waterfall`), cash flow (`chart`), WACC
(`driver_tree`), DCF valuation range (`chart` bar), sensitivity (`heatmap`),
scenarios.

**Project-economics variant** (a new site, format or investment case, e.g. one
more car wash): follow `project-economics-content.md`: investment case
(`content`), unit-economics tree (`driver_tree`), ramp-up and P&L per site
(`chart`), cash flow and payback (`chart` cumulative), break-even (`chart` or
`content`), sensitivity (`heatmap` volume × price → payback/IRR), **what you
need to believe** (`content`), scenarios.

## Executive summary (first page, written last)

`exec_summary` rows: **Context** · **Market** · **Competition** · **Company**
(+ **What you need to believe** for project cases). Three to five bullets each,
every bullet a finding with a number, taken from exhibit headlines. The
`bottom_line` is one sentence: the answer and the decision it informs.
`kpis`: three to four tiles (market size, growth, the client's key number).

## Appendix

Sources & confidence (auto-generated from `sources`), plus triangulation and
sanity checks if they were pushed out of Part 1.

---

## Length and pacing

A demo deck runs **25–35 slides**; a full CDD readout 40–55. Each slide has one
headline that states a finding, one exhibit, and a Key Takeaways rail with two
or three bullets. If a takeaway does not change what the reader believes, cut
it. Mark directional exhibits `illustrative: true`; never present a modelled
shape as measured.
