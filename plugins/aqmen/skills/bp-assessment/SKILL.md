---
name: bp-assessment
description: Assess a management business plan assumption by assumption — decompose revenue and EBITDA growth into channels and assumptions, rate each on the market, competitive-position and track-record lenses using the fixed scale (highly conservative → highly optimistic / N/A), run the sensitivity, write the rationale and Aqmen's own view — and render the result as house-style deck slides (growth channels, bridges, sensitivity table, the colour-coded assessment matrix, one deep dive per key assumption, Aqmen view) plus a colour-coded Excel table. Use this whenever the user wants to assess, stress-test, pressure-test, challenge or rate a business plan, management case, forecast, budget or projections, or asks "how optimistic is the plan", "which assumptions are realistic", "what do we need to believe in the management case", "give me the BP assessment slides" — for buy-side diligence, M&A process readiness, or an internal plan review.
---

# Aqmen Business Plan Assessment

Turns a management plan into an assumption-by-assumption verdict on one scale,
with the evidence and Aqmen's alternative, so a deal team can adjust the case
rather than debate it.

| Output | Use |
| --- | --- |
| `<slug> - BP Assessment.pptx` | Slides in the house style: growth channels, bridges, sensitivity, the assessment matrix, deep dives, Aqmen view. Drop into a CDD deck or present standalone. |
| `<slug> - BP Assessment.xlsx` | The assessment table with colour-coded ratings, lens notes, sensitivity and Aqmen view; the working document and the audit trail. |

## Read first

1. `references/bp-method.md` — decomposition, the three lenses, the scale,
   deep dives, Aqmen's view. This is the method; the rest is rendering.
2. `references/bp-format.md` — the JSON the renderer takes.
3. `references/engagement-method.md` — hypotheses and 80/20: the deep dives go
   where sensitivity and uncertainty are both high.
4. `references/report-standards.md` — facts vs estimates, sources, honesty
   about what was not assessed.

`assets/example-wealth-bp.json` is a complete illustrative example (a
UK wealth manager's plan; numbers are placeholders).

## Workflow

### 1. Get the plan into a structure you can assess

Inputs arrive as an Excel model, a PDF pack, a CIM or a set of slides. Read
the whole thing before extracting. Pull out:

- **Horizon and metric**: base year and end year; revenue and EBITDA (and the
  operating metric the plan is built on: AuA, sites, users, volume).
- **Growth channels** as management labels them, with each channel's
  contribution to end-year revenue and EBITDA; group organic vs inorganic or
  existing vs new.
- **The assumptions** underneath: volumes, prices, penetration, productivity,
  costs. Keep management's names. Six to ten rows is normal.
- **Historicals** for every assumption (three to five years) and whatever
  external evidence exists in the workspace: the aqmen market model, the
  competitive dataset, benchmarks, expert notes.

If the plan file is not available, work from the table the consultant gives
you and say so in the handover. Never fill an assumption you cannot see.

### 2. Sensitivity

Flex each assumption by 10% (downside) and record the change in end-year
EBITDA, absolute and as a share, with the "from → to" values and a one-line
comment. If the model is not available to recompute, estimate the effect
transparently from the plan's own arithmetic and mark it as an estimate.

### 3. Rate

For each assumption: the three lenses (market / competitive position / track
record), each with a rating and a one-line note; then the overall rating and a
two- to three-sentence rationale that names the plan value, the evidence value
and the gap. Assumptions not assessed in detail are `na` with a reason. Pick
the 3–6 for deep dives: highest sensitivity, most contested rating.

### 4. Aqmen's view and the overall verdict

For every non-realistic assumption, the value Aqmen would use and why. Then
the overall rating of the plan and the headline that carries it.

### 5. Write the JSON and render

```
python scripts/build_bp.py assessment.json ./out
```

Check the matrix slide first: every row has a rating and a rationale, deep
dives are marked, the legend reads. Then the deep dives: headline in the form
"N. <Assumption> deemed <rating> because <gap>".

### 6. Hand over

Tell the consultant: the overall verdict, the three assumptions that drive
it and their EBITDA at stake, what was carried at plan value, and what
evidence was missing. Offer to fold the slides into the `cdd-output` deck
(they slot into the Company part) or to build the adjusted case.

## Where the skill stops

It rates and explains; it does not rebuild the model. Adjusted-case modelling
is done in the client's model or in an aqmen workspace (`aqmen:model`, the
company-analysis guide), from the Aqmen-view column this skill produces. When
the project has a workspace, the market lens reads its market model and the
competitive lens its landscape table, and each rating cites the dataset or
chart it rests on.
