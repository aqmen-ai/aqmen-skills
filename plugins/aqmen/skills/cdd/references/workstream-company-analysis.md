# Workstream: Company (company analysis)

What the Company part of a CDD deliverable covers for an operating business,
how each exhibit reaches the deck, how the HTML report lays it out, and
what to gather. The **method** — statements as sheets over the reported
figures, tie-outs, the driver forecast, the DCF, the critics' checklist — is
the platform's `company-analysis` topic (after `modeling`). Read it before
modeling.

## Objective

Assess the target's financial trajectory, and value it when the question
needs a value. State which statements are in scope and why. Lead with the
so-what: the **valuation range** or the key margin or value-creation
finding.

## What the part must cover

Omit a topic only if it genuinely does not apply, and say so.

1. **Objective and scope of use** — the question, the decision, the
   statements in scope, the precision. Headline conclusion up front.
2. **Data landscape** — what is disclosed (line items, segments, non-GAAP
   bridges), whether cash flow and balance sheet are observable, what had
   to be estimated.
3. **Operating performance** — the revenue build where disclosed, the
   margin bridge as named steps (gross profit → EBITDA → EBIT → net income),
   the cost structure; revenue, growth, key margins.
4. **Cash generation** — if in scope: net income → CFO → FCF; cash
   conversion.
5. **Balance sheet and working capital** — if decision-relevant: NWC,
   leverage, the days levers.
6. **KPIs and margins** — the few that matter for this business.
7. **Valuation** — FCFF → enterprise value; the WACC build; the terminal
   method with its **share of EV**; EV → equity → per share; a WACC × g
   sensitivity.
8. **Scenarios** — the hypotheses in words, then the input changes against
   Base. Base first.
9. **Sources and confidence.**

## The slides — elements and sources

The platform's `company-analysis` topic ends with the sourceable exhibits
and the ones a slide cannot draw; follow it. In the storyline:

| Slide | Exhibit | How it reaches the slide |
| --- | --- | --- |
| Business and scope | description, lines, shareholding | typed |
| Revenue and margins over time | historicals + forecast | `line` or `bar` chart over a small block referencing the statement |
| Margin / EBITDA bridge | named steps | `waterfall` chart |
| P&L summary | the statement as read | `range` over the statement's summary rows |
| Operating KPIs | the business's own KPIs | `bar`/`line` chart, or `cell`s as KPI tiles |
| Cash flow | FCF, conversion | `bar` chart over a block referencing the cash flow |
| WACC build | WACC = wE·Ke + wD·Kd(1−t), Ke = Rf + β·ERP | **rebuilt**: shapes, each input and result a sourced `cell` of the DCF sheet |
| Valuation range | EV and equity value, low / base / high | `cell`s for the values; a `bar` chart or `range` for the range; terminal share as a `cell` |
| Sensitivity | WACC × g grid, base outlined | `range` over the sensitivity grid |
| Scenarios | side by side, Base first | `range`; the hypotheses typed beside it |
| What you need to believe | growth vs market, margin vs peers, capex, terminal assumptions — verdicts, break-evens | `range` over the model's `Believe` rows (`modeling`) |

The revenue driver tree, where the company discloses its drivers, is
**rebuilt** like the market's.

## The HTML report — sections

1. Objective and scope of use — the headline conclusion in one line.
2. Data landscape.
3. Operating performance — KPI tiles, the revenue trajectory, the margin
   waterfall.
4. Cash generation — only if in scope.
5. Balance sheet and working capital — only if decision-relevant.
6. KPIs and margins.
7. Valuation — the FCFF spine, the WACC tree (`.dtree`), the terminal
   method and share, EV → equity → per share, the sensitivity heatmap
   (`table.heatmap`), a tornado of the inputs that move the value most.
8. Scenarios — Base first.
9. Sources and confidence.

## Module rules

- Build only the **statements in scope**; say why the others are out.
- Keep the **margin bridge legible**: the named steps, not every line.
- **Valuation as a range**, never a false-precision point; the terminal
  value's share of EV always stated, flagged above ~75%.
- **Inputs vs computed** visibly distinct: the reader knows what is an
  assumption.
- A **validated Base before any scenario**.

## What to gather

- The **brief**: decision, questions, company, fiscal year end, currency,
  statements in scope.
- The **statement sheets** (`read_spreadsheet`; `show_spreadsheet_range`
  for a reader's view): which rows are inputs and which computed, the
  tie-out rows, the driver rows and their notes.
- The **KPI block** and the **DCF sheet**: FCFF, WACC inputs, EV, equity,
  per share, terminal value and its share, the sensitivity grid.
- Per historical figure, its **dataset** (the filing and page),
  confidence and method.
- The **charts** over the model (bridge, trajectory, revenue build).
- The **insights** that answer the company questions.
- The **scenarios**: the hypotheses, the lines they move, the realization.
