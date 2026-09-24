# Project economics — content (Company part, project variant)

Use this instead of `company-analysis-content.md` when the "company" being
assessed is **an investment case rather than an operating business**: a new
site, a new format, a roll-out, a capex programme. Examples: one more car wash
on a Moeve forecourt; a dark store; a new production line. The question is not
"what is this company worth" but **"does this pay back, and what do you need to
believe for it to?"**

Read alongside `report-standards.md` (facts vs estimates, base first) and
`report-data.md` (pull the model from aqmen; never invent numbers).

## Objective

State the investment decision (how many sites, which format, go/no-go), the
unit of analysis (one site, one line) and the horizon. Lead with the answer:
payback in N years, IRR of X%, break-even at Y units per day.

## What the deliverable must cover

1. **The investment case** (`content`): what is being built, where, capex per
   unit (split: equipment, civil works, permits), ramp-up assumption, life of
   the asset. The client's own numbers where they exist, labelled as such.
2. **Unit-economics tree** (`driver_tree`): Revenue = volume × ticket (×
   mix); EBITDA = revenue − variable cost (water, chemicals, energy, card fees,
   per unit) − fixed cost (staff, rent or opportunity cost of land, maintenance,
   marketing). Certainty dots on every leaf. This is the exhibit the client
   argues with, so the leaves must be the numbers they can check.
3. **Volume build** (`chart` or `content`): where the units come from: site
   traffic × capture rate × frequency, or catchment × penetration × frequency.
   Tie back to the market section (the site's share of local SAM).
4. **P&L per unit at maturity** (`waterfall`): revenue → contribution → EBITDA
   → cash after maintenance capex. Show the margin structure, not just the end
   number.
5. **Ramp-up and cash flow** (`chart` cumulative line/column): capex at t0,
   cash flows by year, cumulative curve crossing zero = payback. State
   discounted and undiscounted payback, IRR and NPV at the client's hurdle
   rate.
6. **Break-even** (`chart` bar or `content`): units per day (or per month) to
   cover fixed costs; to reach target IRR; compared with the current run-rate
   of the flagship if it exists. This is the "how many cars" question.
7. **Sensitivity** (`heatmap`): volume × ticket (or volume × capex) → payback
   years or IRR, base case outlined. Also a tornado (`chart` bar Low/High) if
   more than two drivers matter.
8. **What you need to believe** (`content`): four to six assertions, each with
   the number and its current evidence, e.g. "capture rate of 4% of forecourt
   traffic — flagship shows 3.1% after 8 weeks". This is the bridge to the
   executive summary and to the market and competition parts.
9. **Scenarios** (`scenario`): base first; then downside (competitor opens
   nearby, ticket pressure) and upside (subscription, cross-sell to shop) as
   initiatives in words, then the overrides.
10. **Sources & confidence** — as in every aqmen output.

## Module rules

- Separate **client-provided inputs** (capex, flagship run-rate) from
  **aqmen assumptions** (capture, frequency) and **computed** results.
- Give payback and IRR as **ranges** with the base highlighted; a single point
  hides the uncertainty the sensitivity exhibit shows.
- Volume assumptions must reconcile to the market: N sites × units per site
  must not exceed the local SAM or imply an implausible share.
- Include the **opportunity cost** of the land or floor space when the asset
  sits inside an existing site; otherwise the case is flattered.
- State the ramp-up curve and the year at which "maturity" numbers apply.

## What to gather from aqmen

The company-analysis model built as a project model: input nodes (capex items,
volume drivers, ticket, unit costs, fixed costs, ramp-up), computed nodes
(revenue, EBITDA, cash flow, cumulative cash, payback, IRR, NPV), per-period
values, each with source/confidence/note; scenarios and their initiative
levers; the market sizing's local SAM for the volume reconciliation.
