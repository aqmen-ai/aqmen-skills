# Aqmen Report Standards (shared)

These analytical standards apply to **every** aqmen output report (market sizing,
company analysis, competitive landscape). They exist so reports read as one
house voice and are trustworthy for real commercial-diligence decisions.

> This file is shared verbatim across all three aqmen report skills. Keep it in
> sync if you change it.

## Voice & standard

- **Decision-grade.** The audience is expert consultants making real
  commercial-diligence calls. Match top-tier consulting/diligence quality.
- **So-what first.** Lead every report — and every section — with the
  conclusion, then support it. The executive summary states the answer and the
  decision it informs before any methodology.
- **Concise, signal over volume.** Plain language. No filler, no restating the
  obvious, no raw event logs. If a sentence doesn't change a reader's decision,
  cut it.
- **Facts vs. estimates, always labelled.** Distinguish observed data from
  modelled estimates. Call out assumptions and uncertainty explicitly.
- **Justified complexity.** Prefer the structure the economics actually require;
  simplify only when it preserves the decision logic. Don't dumb down a real
  model, and don't manufacture complexity either.
- **Honesty / no implied completeness.** Surface gaps, sparse coverage, and
  missing values openly. Never present a partial picture as complete.

## Base-first discipline

- Present a **validated Base case** before any scenario.
- Keep the **qualitative scenario thesis** (Trends / Initiatives) separate from
  the **quantitative overrides** that implement it. State the thesis in words,
  then show the numbers that change vs. Base.

## Sources & confidence (required closing section)

Every report ends with a **Sources & confidence** section. Every quantitative
claim in the body must be attributable to a source with a confidence score.

### Confidence scale (integer 1–5, identical across all reports)

| Score | Meaning |
| --- | --- |
| 5 | Primary source — public filings, official statistics, regulatory disclosures, user-provided data |
| 4 | Credible secondary — major analyst reports, reputable industry databases, entity press releases |
| 3 | Triangulated / partially corroborated. **Ceiling for news articles and blog posts.** |
| 2 | Single weak source, or rough directional estimate |
| 1 | Pure estimate, no supporting data |

Caps: **news ≤ 3** (never 4–5); government / international-org data typically
4–5; major analyst firms (Gartner, Statista, Euromonitor, IBISWorld) typically 4.

### Source types (the type is the audit trail)

- `web` — URL-based; **always include the URL.** Anything derived from web
  search or web pages is `web`, never `ai`.
- `file` — an uploaded document.
- `human` — a user-provided value.
- `ai` — a model estimate with **no** external reference. Last resort only; note
  what was searched for and not found.

### Citing rule

Never state a number without attribution. Each value carries a source,
confidence, and a short explanatory note. If the only source is a news article,
flag it and prefer better data where it exists.

### Primary-source hierarchy (research priority)

- **Market sizing:** official/institutional statistics (census, regulators,
  Eurostat, World Bank, OECD, UN, BLS, IBGE, INSEE, ONS…) → analyst
  reports/databases (Statista, Gartner, Euromonitor, IBISWorld) → company
  filings (bottom-up validation) → news (last resort, cap 3).
- **Company analysis:** company filings first (10-K/10-Q/20-F, annual report,
  investor decks, earnings; MD&A, segment & KPI disclosures, non-GAAP bridges) →
  reputable databases & analyst coverage (PitchBook, Capital IQ) → news (last
  resort, cap 3).
- **Competitive landscape:** filings & annual reports → investor materials &
  company sites → reputable financial/business databases → analyst/industry
  sources → news (last resort, cap 3).
