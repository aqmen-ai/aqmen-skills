# Company analysis on the workspace

A company model is a set of statements — income statement first, then
cash flow, then balance sheet, then a valuation only if the question
needs a value — built as spreadsheet sheets over cited datasets. This
guide adapts aqmen's company-analysis practice to datasets,
transformations and spreadsheets. Read the MCP's `modeling` and
`spreadsheets` topics first; the spreadsheets topic's **P&L recipe** is
the layout to imitate.

## Scope: the question bounds the model

- Ask what decisions the model informs and which statements the questions
  actually need. Operating performance alone needs only the income
  statement. Do not build all three statements by default.
- **Check the disclosure first.** Read the latest filings: which segments
  the company reports, how the MD&A splits costs, which KPIs management
  discusses. Disclosure is the upper bound on depth. If revenue is
  reported only in total, revenue stays one line with the gap noted; do
  not build a segment tree filled with invented splits.
- Record company, sector, business model, geography, fiscal year end,
  currency and period scope in the brief.

## Data: the reported figures are datasets

- **Historicals as published.** One dataset per statement or disclosure
  table, long format: `line_item, segment?, fiscal_year, value`, with the
  unit and scale in the column semantics. Cite each filing (the 10-K, the
  annual report, the page) in `sources`.
- **KPIs** management reports (customers, ARPU, stores, headcount) are
  their own datasets, cited the same way.
- **Market drivers** that feed a revenue build (a market size from a
  sizing, a share) come from their own datasets or another model's feed,
  never retyped.
- Source order for company data: filings (10-K, 10-Q, 20-F, annual
  reports) → financial databases (Capital IQ, PitchBook) → the company's
  own releases and investor materials → major analyst coverage → news,
  capped at 3.

## Structure: statements as sheets

- **One sheet per statement** (`IS`, `CF`, `BS`), line items as rows and
  fiscal years as columns, as the P&L recipe lays out. Historical columns
  read from the datasets through a connection or `SUMIFS` over a
  connected copy on an `Inputs` sheet; forecast columns are formulas.
- **Sibling order a reader expects:** revenue before cost of revenue,
  gross profit before operating expenses, operating expense detail (R&D,
  Sales & Marketing, G&A, unless the company's own order is clearer)
  before EBITDA or operating income, then D&A, interest, non-operating
  items and taxes before net income.
- **Keep revenue prominent** and each statement readable within three to
  four levels of indent. Go deeper only for disclosed, decision-relevant
  driver detail (a revenue build by segment × price × volume).
- **Prior-period logic** (growth, working-capital timing, cash-flow
  bridges) references the previous column, as Excel does.
- **Margins and ratios** (gross margin %, EBITDA margin %, churn) go in a
  KPI block on the statement sheet or a `KPIs` sheet, not inside the
  statement's rows. Pick the few that matter for this business.
- Style with roles: `input` for assumptions a person may change, `link`
  for data from datasets, `formula`, `subtotal` and `total`. A `note` on
  every input row says where the number came from.

## Forecasts

- Forecast drivers as hypotheses per the `modeling` topic, on a
  `Hypotheses` sheet with a scenario selector. Name each after its claim
  ("Pricing reset in 2026", "Hiring freeze"), not its mechanism.
- Base first, validated with the user, before any scenario.

## Valuation, only when the question needs a value

- Build it after the income statement and cash flow exist and are
  populated. A `DCF` sheet: NOPAT → FCFF (EBIT × (1 − tax) + D&A − capex −
  change in NWC) → discount factors → enterprise value, with a CAPM WACC
  block (risk-free rate, beta, equity risk premium, cost of debt, weights)
  and a terminal value (Gordon growth or exit multiple on EBITDA).
- Link the drivers to the statement rows by reference; never retype them.
  Rates as 0–1 ratios with a `%` format.
- Sanity checks as `checks`: WACC above terminal growth, and the terminal
  value's share of enterprise value stated. Bridge enterprise value to
  equity value (net debt, minorities) and per share where asked.

## Charts

A `waterfall` for the revenue or EBITDA bridge between two years, a
`driver-tree` over the revenue build, a `line` for margins over time. No
investment advice, and no precision beyond the evidence.
