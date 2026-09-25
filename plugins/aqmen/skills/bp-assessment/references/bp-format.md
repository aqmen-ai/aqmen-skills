# BP assessment format (JSON → deck + Excel)

`scripts/build_bp.py assessment.json <outdir>` renders the assessment deck
(`<slug> - BP Assessment.pptx`) and the table (`<slug> - BP Assessment.xlsx`).
Worked example: `assets/example-wealth-bp.json`.

## Top level

```json
{
  "title": "Project X — Business plan assessment",
  "subtitle": "Assessment of the management case", "client": "[Target]", "date": "2026",
  "slug": "project-x-bp", "metric": "EBITDA", "years": [2026, 2030],
  "overall": {"rating": "optimistic", "headline": "Assessment of key assumptions implies the plan is slightly optimistic"},
  "channels": { … },            // optional context slide
  "bridges": [ … ],             // optional waterfall slides
  "categories": [ … ],          // the assessment rows
  "sensitivity_headline": "…", "view_headline": "…"
}
```

## Growth channels (context slide)

```json
"channels": {
  "headline": "[Target]'s eight growth channels grouped into four categories for assessment",
  "chart_title": "Growth channels and contribution to the plan",
  "metrics": ["Revenue 2026", "Revenue 2030", "EBITDA 2026", "EBITDA 2030"],
  "items": [
    {"name": "1. Constant perimeter", "group": "Organic", "overview": "Existing book run forward",
     "values": {"Revenue 2026": "£122m / 90%", "Revenue 2030": "£151m / 45%", "EBITDA 2030": "£59m / 40%"}},
    …
  ],
  "so_whats": ["+50% of 2030 EBITDA relies on channels with limited track record"],
  "source": "[Target] business plan"
}
```

## Bridges (waterfall slides)

```json
"bridges": [
  {"metric": "Revenue", "unit": "£m", "headline": "Excluding M&A, adviser recruitment is the largest contributor to 2030 revenue",
   "steps": [["Revenue 2026", 135, true], ["1. Constant perimeter", 29.2, false], ["2. Recruitment", 68.1, false],
             ["3. Lead tech", 15.5, false], ["4. M&A", 89.8, false], ["Revenue 2030", 337.6, true]],
   "so_whats": ["Most growth is organic but its track record is limited", "…"]}
]
```

## Categories and assumptions (the assessment)

```json
"categories": [
  {"name": "Assets under advice", "assumptions": [
    {"id": "1", "name": "Net flows",
     "values": {"2026": "0.0%", "2030": "2.5%"},
     "rating": "optimistic",
     "lenses": {
       "market":       {"rating": "realistic",  "note": "UK advice peers average 2.4%"},
       "competitive":  {"rating": "optimistic", "note": "Net flows negative in each of the last three years"},
       "track_record": {"rating": "optimistic", "note": "Turnaround has no historical support"}},
     "rationale": "Gross inflows rise 6.5% to 11% of AuA with withdrawals held at 5–6%; reported net flows were negative in each of the last three years; UK peers average 2.4%.",
     "aqmen_view": "1.5% by 2030",
     "sensitivity": {"delta": -711, "pct": 0.5, "from": "2.5%", "to": "2.25%", "comment": "Impacts the yearly inflow rate; £130m less AuA by 2030"},
     "deep_dive": {
       "headline": "1. AuA growth plan seems realistic, with market upside offsetting an optimistic net-flow recovery",
       "panels": [
         {"title": "1a. Net flows", "rating": "optimistic",
          "body": ["The assumed turnaround lacks historical support…"],
          "chart_title": "Historical net flows, % of AuA",
          "chart": {"kind": "column", "categories": ["2023", "2024", "2025"], "series": [["[Target]", [2.2, 0.4, -1.1]], ["Peer A", [3.5, 4.0, 7.0]]]}},
         {"title": "1b. Market movement", "rating": "conservative", "body": ["…"]}
       ],
       "assessment": {"title": "AuA evolution assessment", "rating": "realistic",
                      "bullets": ["The combined trajectory appears achievable…", "…"]},
       "source": "Factset; [Target] CIM; Aqmen analysis"}}
  ]}
]
```

- `rating` values: `highly_conservative`, `conservative`, `realistic`,
  `optimistic`, `highly_optimistic`, `na` (symbols `++ + = - -- N/A` also
  accepted).
- `values` keys are the `years` (as strings); any unit ("2.5%", "36", "88.7").
- `sensitivity.delta` is the change in end-year `metric` for a 10% downside;
  `pct` its share of end-year metric. Rows with a sensitivity feed the
  sensitivity table, sorted by |delta|.
- `deep_dive` is optional; up to two evidence panels (text and/or a native
  chart) plus the assessment rail. Assumptions with a deep dive get the
  lavender "deep dive to follow" mark on the matrix.
- `aqmen_view` is optional; rows with one feed the Aqmen-view table.

## Excel

One row per assumption: id, category, name, plan values, BP assessment
(colour-coded), the three lens ratings (colour-coded) and notes, rationale,
Aqmen view, sensitivity, deep-dive flag. A second sheet documents the scale.
