# Competitive landscape on the workspace

A landscape is a benchmark: the players in a market, systematically
compared on researchable fields, clustered into archetypes, and read for
who is winning and why. On the workspace the grid is a **dataset per
field family** joined by a **transformation** into one player table, and
the reading is **charts, a view and insights**. Read the MCP's `datasets`,
`sql` and `visualization` topics first.

## 1. The goal and the market

Ask what decisions the landscape informs (an acquisition shortlist,
positioning for a pitch, a threat assessment) and which questions it
answers ("who are the top five pure-play competitors?", "which
archetypes are winning share?"). They decide who belongs on the list and
which fields matter. Reuse a market sizing's definition if the workspace
has one; otherwise fix the market, the geography, the currency and the
base year in the brief.

## 2. The long list

Twenty to thirty players from research and market knowledge, inclusive
first, each with a one-line reason for inclusion. Load it as a
`players` dataset (`company, website, hq_country, inclusion_reason`),
citing where each came from. The user adds and removes; you reload.

## 3. Tiering

- **Tier 1**, core competitors: typically more than 25–30% of revenue
  addressable to this market.
- **Tier 2**, semi-direct or adjacent: 10–25%.
- **Tier 3**, peripheral: under 10%.

Give the reason for borderline cases and ask whether Tiers 2 and 3 are in
scope now. Tier is a column on the `players` dataset (or a small cited
mapping dataset), never typed into a chart.

## 4. Fields

First run a disclosure scan on two or three Tier 1 players: what filings,
databases and company sites actually publish. **A field more than half
empty across Tier 1 is a bad field**; drop or replace it. Then propose
the baseline, confirm it, and add up to five market-specific fields that
are researchable and tied to the questions:

| Field | Notes |
| --- | --- |
| Company, Tier, HQ, Year founded | Profile |
| Revenue | Latest fiscal year, the reporting currency converted at a cited rate |
| % addressable | Share of revenue in this market, with its reasoning |
| Market-specific revenue | Revenue × % addressable, computed in the transformation |
| Growth | Revenue growth, stating the period |
| Employees | As published |
| Archetype | Left empty until step 7 |

Every numeric field has its unit and scale in the column semantics.

## 5. Population

- Load the values as long datasets, `company, field, period, value`, one
  per source family (filings, a database export, the company sites), each
  citing its documents in `sources`. Where rows mix sources of different
  quality, add `source_url` and `confidence` columns.
- Source order: filings and annual reports → financial and business
  databases (Capital IQ, PitchBook, Crunchbase for private companies) →
  the company's releases and investor materials → major analysts → news,
  capped at 3.
- Tiers 1 and 2 in full; Tier 3 light-touch on the key fields.
- One transformation pivots and joins them into the **landscape table**:
  one row per player, one column per field, market-specific revenue
  computed, confidence carried as the minimum of the row's key fields.

## 6. Reliability

Summarise reliability for the user in reader-facing tiers: **Strong**
(4–5: filings, official data, major analysts), **Moderate** (3:
triangulated, or one non-news secondary source), **Weak** (1–2: sparse
disclosure, directional estimates). Name the hotspots: the players or
fields the conclusion leans on that sit in Weak.

## 7. Archetypes

Explain the purpose: clustering similar players to read trends and
predict behaviour. Propose two or three clustering lenses from the data
(business model, customer focus, scale × growth), then three to five
archetypes with their rationale. Once the user confirms, load the
assignment as a cited mapping dataset (`company, archetype, rationale`)
and join it into the landscape table.

## 8. So what

- Charts over the landscape table: a `bar` of market-specific revenue by
  player coloured by archetype, a `scatter` of scale against growth, a
  `table` of the Tier 1 profile. `show_chart` each.
- A **view** per question, read the way a partner reads a page.
- **Insights**, one claim each on the chart that shows it: who is winning
  and why, who is losing ground and why, the two or three trends
  underneath. Lead with the conclusion, back it with the strongest
  evidence, close with the implication. Separate fact, estimate and
  interpretation.

Scenarios, where asked, are alternative datasets or columns (an upside %
addressable) joined beside Base, never edits to Base.
