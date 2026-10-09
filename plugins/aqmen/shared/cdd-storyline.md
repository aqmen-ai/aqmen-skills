# The CDD storyline: four parts, one answer

The standard aqmen commercial-due-diligence deliverable (specified by Miguel,
23 Sep 2026): structured the way a top-tier CDD is, **top-down, every slide
answering a so-what, the whole serving one question** — is there an
opportunity here, and what do you need to believe for it to be real?

> Canonical in `shared/`, synced into `cdd` and `storyline`. The storyline
> skill plans these slides before the work; the deliver step builds them as a
> deck in the workspace. Each part's detail — what to cover, which exhibits,
> the module rules — is in the cdd skill's `workstream-*.md` files; the slide
> mechanics (elements, sources, the house look) are the platform's `decks`
> topic.

The four parts are fixed. Write the **executive summary last**, from the
headlines of the slides.

## How an exhibit reaches a slide

Every slide below names its exhibit and how it gets there. The platform's
`decks` topic is the contract; in short:

| Marked | Means |
| --- | --- |
| **chart** (bar, line, pie, waterfall, table, number) | a saved chart, added by source |
| **cell / range / field** | a model cell (a KPI), a model range (a table), one field of a chart's result |
| **insight** | a validated insight, as the slide's headline or a bullet |
| **rebuilt** | an exhibit a slide cannot draw (driver tree, marimekko, scatter, heatmap, harvey balls): shapes and lines, every number a sourced cell or field; or a sourceable cut of the same data |
| **typed** | words only — scope, method, rationale; a figure in a sentence carries a deck `check` |

## Part 0 · Context (2–3 slides)

- **Objective and scope** — typed: the question, the decision it informs,
  who asked; in and out of scope, geography, horizon, currency. From the
  brief.
- **Data landscape** — typed, with a watch-out: what exists, what is thin,
  what had to be estimated. From the sources register.
- Optional: **The situation** — typed: the client's position and why now.

## Part 1 · Market (8–11 slides)

The demand-side build aqmen is strongest at; supply is Part 2.

1. **Market definition** — typed: what is in and out; the entity that
   spends (a person, a household, a company, a car).
2. **Method and driver tree** — rebuilt: market expression → variables →
   leaf drivers, each box's value a sourced cell of the model's summary,
   confidence shown per leaf. The methods: volume only, price × quantity,
   or attachment rate (a share of a wider spend).
3. **Headline size, TAM → SAM** — a KPI (cell) plus a stacked or 100%
   stacked bar chart by the most relevant dimension (the sourceable cut of a
   TAM/SAM marimekko; whitespace as its own series).
4. **The SAM today, by the cuts that matter** — chart: stacked bar by
   segment, or a range table when two dimensions matter.
5. **Trends** — typed table (Trend · Driver hit · Direction · Rationale),
   grouped macro / regulatory / consumer. Each trend names the driver it
   moves; where it is a modelled hypothesis, the sizing is a cell.
6. **Trajectory** — chart: stacked bar or line, five years back and five
   forward; CAGR as a KPI (cell) or in the insight headline.
7. **Growth by segment** — chart: bar of CAGR by segment.
8. **Driver detail** — one or two charts: how the key drivers evolve.
9. **Sensitivity** — chart: horizontal bar (tornado) over the model's
   sensitivity block, or its range.
10. **Scenarios** — range: the scenario summary block side by side, Base
    first; the hypotheses in words beside it.
11. **Appendix — triangulation** — chart: bar of our size against the
    published top-down figures (loaded as a dataset), the adjustment stated.
12. **Appendix — sanity checks** — range: the sanity-check rows of the
    `Believe` block (`modeling`), PASS/FLAG computed — never typed.

## Part 2 · Competition (5–7 slides)

1. **Player set and archetypes** — typed, with the tier rule; counts as
   fields of the landscape.
2. **Revenue build** — table chart (or range) over the landscape: revenue ×
   % addressable = market revenue per player, summed; reconciles to Part 1.
3. **Archetype map** — rebuilt 2×2 (shapes for each archetype's box, player
   points as fields), or the sourceable cut: a bar of market revenue by
   archetype.
4. **Competitive trends** — typed: consolidation, integration, new formats,
   and what each implies per archetype.
5. **Key buying factors** — a table chart with the ratings as text (the
   harvey matrix rebuilt), plus the criteria importance where interviews
   exist.
6. **Positioning and implications** — typed, insight headline: where each
   archetype wins; the whitespace for the client.
7. **Reliability review** — typed with a watch-out, or a chart of coverage by
   confidence: strong / moderate / weak.

## Part 3 · Company (5–8 slides)

Description, business lines and
shareholding (typed); revenue, EBITDA, net income over time (chart);
operating KPIs (chart or cells); margin bridge (waterfall chart); cash flow
(chart); WACC build (rebuilt tree of cells); DCF value range (chart or
range); WACC × g sensitivity (range); scenarios (range).

## What you need to believe (after the executive summary)

Range: the `Believe` rows of each workstream's model (`modeling`) —
assumption, implied metric, reference, verdict, break-even — one slide, or
one per workstream in a full readout. The verdict travels as its word; the
headline names the demanding or implausible rows the answer rests on. Pushed
to the appendix only when the client asks; it is the IC's first page.

## Executive summary (first content slide, written last)

Rows **Context · Market · Competition · Company** (+ **What you need to
believe**, from the slide above), three to five bullets each, every bullet a
finding with its number taken from the slides' headlines — validated
insights by source where they exist. The bottom line is one sentence: the
answer and the decision it informs. Three or four KPI tiles (market size,
growth, the client's key number), each a sourced cell or field.

## Appendix

Sources and confidence (a table built from the datasets' citations and
confidence), triangulation and sanity checks if pushed out of Part 1, and
hidden backup slides.

## Length and pacing

A demo deck runs **25–35 slides**; a full CDD readout 40–55. One headline
that states a finding, one exhibit, and a Key-takeaways rail of two or three
bullets per slide. If a takeaway does not change what the reader believes,
cut it. A directional exhibit says so in its exhibit title ("illustrative");
a modelled shape is never presented as measured.
