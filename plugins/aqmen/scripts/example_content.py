#!/usr/bin/env python3
"""Single source of the **example placeholder content** for each deck/report
module.

Both the PPTX starter templates (`build-templates.py`) and the HTML report
starter templates (`build-html-examples.py`) render THIS content, so a module's
deck and report always show the same information — same title, so-whats,
sections, figures, and sources — differing only in format. Edit the content
here, then regenerate both and re-sync.

Placeholders use the `[bracketed]` convention (e.g. `[Market]`, `[Region A]`,
`~$[XX]B`) so a consultant sees what to fill in.

Schema per module:
  title, subtitle, doctype, year          cover / brand
  agenda: {items, active, subitems?, active_sub?}
  bottom_line                             the one-line answer + decision (report)
  confidence                              overall 1–5 (report cover badge)
  exec_summary: [(label, [bullets])]      the one-page answer
  kpis: [(value, label, delta_or_None)]   headline tiles (report)
  sections: [ {kind, ...} ]               ordered content topics (see below)
  sources: [(source, conf, note)]

Section kinds and their fields:
  content   title, headline, left_title?, body[], so_whats[], watchout?, source
  chart     title, headline, chart{kind,categories,series,number_format,legend,y_title?},
            chart_title, so_whats[], source, illustrative?
  mekko     title, headline, chart_title, mekko[(label,width,[(seg,val)])],
            so_whats[], source, illustrative?     (deck: Marimekko; report: stacked bar)
  harvey    title, headline, columns[], rows[(label,[fills 0..1])], row_header,
            so_whats[], source, illustrative?     (deck: harvey balls; report: table)
  scenario  title, headline, left_title?, body[], so_whats[], source

Bullets are `(text, bold, level)` tuples (level 0–2). so_whats are plain strings
(deck: takeaways rail; report: insight callout).
"""

# convenience: a plain level-0 non-bold bullet
def t(text, bold=False, level=0):
    return (text, bold, level)


MARKET_SIZING = {
    "title": "The [Market] Opportunity",
    "subtitle": "Market sizing & growth outlook — Commercial Due Diligence",
    "doctype": "Market Sizing",
    "agenda": {
        "items": ["Context", "Market Overview", "Competitive Landscape", "Appendix"],
        "active": "Market Overview",
        "subitems": {"Market Overview": ["Definition & Projections",
                                         "Deep Dive on Assumptions"]},
        "active_sub": "Definition & Projections",
    },
    "bottom_line": ("The [market] is a ~$[XX]B opportunity (TAM) growing ~[X]% a "
                    "year; the serviceable market is ~$[XX]B, enough to underwrite "
                    "the [decision]."),
    "confidence": 4,
    "exec_summary": [
        ("Objective", [
            "Size the [market] and its trajectory to underwrite the investment thesis",
            "Question answered: how large is the serviceable opportunity, and how fast is it growing?"]),
        ("Market size", [
            "TAM of ~$[XX]B in [base year], with a serviceable market (SAM) of ~$[XX]B",
            "Projected to grow ~[X]% annually through [year] as [key driver] plays out",
            "[Region] leads with ~[XX]% of value on higher penetration and pricing"]),
        ("Confidence", [
            "Base case triangulated top-down and bottom-up to within [X]%",
            "Lowest-confidence, highest-leverage driver: [driver] — see sensitivity"]),
    ],
    "kpis": [
        ("~$[XX]B", "TAM, [base year]", "▲ ~[X]% CAGR"),
        ("~$[XX]B", "SAM, [base year]", None),
        ("~[XX]%", "[Region A] share of TAM", None),
    ],
    "sections": [
        {"kind": "content", "title": "Objective & scope",
         "headline": "We size the [market] on a clear, decision-relevant boundary",
         "left_title": "Definition & scope",
         "body": [t("In scope: [products / services], [geographies], [customer types]", True),
                  t("Out of scope: [adjacencies excluded], and why"),
                  t("Geography: [regions]; horizon: [base year] – [year], annual", level=1),
                  t("Currency: $; figures directional unless sourced", level=1)],
         "so_whats": ["A tight boundary keeps the size decision-relevant",
                      "Adjacencies are flagged, not silently included"],
         "source": "[client scope], aqmen"},
        {"kind": "content", "title": "Data landscape",
         "headline": "Public data covers [X]; the gaps that forced estimates are flagged",
         "body": [t("Strong coverage: [official statistics], [analyst databases]", True),
                  t("Partial coverage: [breakdown] available only for [subset]"),
                  t("Gaps: [segment] estimated bottom-up — labelled and low-confidence")],
         "so_whats": ["Where data is thin, we estimate transparently",
                      "No estimate is presented as observed data"],
         "watchout": "[segment] is a bottom-up estimate (confidence 2) — the biggest data gap",
         "source": "Eurostat, Statista, company filings, aqmen", "illustrative": True},
        {"kind": "mekko", "title": "Headline TAM view",
         "headline": "The TAM is a ~$[XX]B opportunity, led by [Region]",
         "chart_title": "[Market] TAM by region, [base year] $B",
         "mekko": [("[Region A]", 53.3, [("Whitespace", 46.6), ("SAM", 6.7)]),
                   ("[Region B]", 20.9, [("Whitespace", 18.4), ("SAM", 2.4)]),
                   ("[Region C]", 13.8, [("Whitespace", 12.5), ("SAM", 1.3)])],
         "so_whats": ["[Region A] is ~two-thirds of total value",
                      "[Region B] is second despite fewer [deals/units]",
                      "[Region C] remains underpenetrated"],
         "source": "[sources], aqmen"},
        {"kind": "chart", "title": "Trajectory",
         "headline": "The market is [recovering / growing] at ~[X]% through [year]",
         "chart_title": "[Market] size, $B",
         "chart": {"kind": "column",
                   "categories": ["'21", "'22", "'23", "'24", "'25E", "'29E"],
                   "series": [("Market size", [11.2, 9.4, 9.1, 10.4, 11.0, 14.6])],
                   "number_format": "#,##0.0", "legend": False},
         "so_whats": ["Trough in [year]; recovery underway",
                      "~[X]% CAGR projected through [year]"],
         "source": "aqmen analysis"},
        {"kind": "chart", "title": "Segmentation breakdown",
         "headline": "[Segment A] drives over half of the market by value",
         "chart_title": "[Market] by segment, $B",
         "chart": {"kind": "stacked_column",
                   "categories": ["[Region A]", "[Region B]", "[Region C]"],
                   "series": [("[Segment A]", [30, 12, 8]),
                              ("[Segment B]", [15, 6, 4]),
                              ("[Segment C]", [8, 3, 2])],
                   "number_format": "#,##0"},
         "so_whats": ["Mix skews to [Segment A] in [Region A]",
                      "[Segment C] is nascent everywhere"],
         "source": "aqmen analysis"},
        {"kind": "chart", "title": "Triangulation",
         "headline": "Bottom-up and top-down reconcile to within [X]%",
         "chart_title": "Triangulation, $B",
         "chart": {"kind": "column", "categories": ["Bottom-up", "Top-down"],
                   "series": [("Estimate", [10.1, 10.8])],
                   "number_format": "#,##0.0", "legend": False},
         "so_whats": ["Two independent methods agree within [X]%",
                      "Divergence explained by [reason]"],
         "source": "aqmen analysis"},
        {"kind": "chart", "title": "Sensitivity",
         "headline": "[Driver] moves the answer most — the swing is ~$[X]B",
         "chart_title": "Sensitivity of TAM to key drivers, $B",
         "chart": {"kind": "bar",
                   "categories": ["[Driver 3]", "[Driver 2]", "[Driver 1]"],
                   "series": [("Low", [9.2, 8.7, 7.9]), ("High", [11.4, 12.1, 13.2])],
                   "number_format": "#,##0.0"},
         "so_whats": ["[Driver 1] dominates the range",
                      "Prioritise diligence on [Driver 1]"],
         "source": "aqmen analysis", "illustrative": True},
        {"kind": "scenario", "title": "Scenario",
         "headline": "[Scenario]: [one-line thesis] lifts the market to ~$[XX]B",
         "left_title": "Trend (qualitative thesis)",
         "body": [t("[Directional thesis in plain words — what changes and why]", True),
                  t("Overrides vs Base (quantitative):"),
                  t("[driver] [assumption] → [value] (was [base])", level=1),
                  t("[driver] [assumption] → [value] (was [base])", level=1)],
         "so_whats": ["Thesis stated in words, then the numbers that implement it",
                      "Base case shown before this scenario"],
         "source": "aqmen analysis"},
    ],
    "sources": [
        ("[Official statistics source]", 5, "base-year market value & population"),
        ("[Analyst database]", 4, "growth rates and segment mix"),
        ("[Company filings]", 5, "bottom-up validation"),
        ("[News / trade press]", 3, "directional colour only (news cap 3)"),
    ],
}


COMPETITIVE_LANDSCAPE = {
    "title": "The [Market] Competitive Landscape",
    "subtitle": "Player benchmarking & positioning — Commercial Due Diligence",
    "doctype": "Competitive Landscape",
    "agenda": {"items": ["Context", "Market Overview", "Competitive Landscape", "Appendix"],
               "active": "Competitive Landscape"},
    "bottom_line": ("[Archetype A] leads on [criterion] while [Archetype C] wins on "
                    "price and speed; the whitespace in [segment] is where [target] "
                    "can win."),
    "confidence": 4,
    "exec_summary": [
        ("Objective", [
            "Benchmark the players and locate where [target] can win",
            "Question answered: who competes, on what, and where is the whitespace?"]),
        ("Landscape", [
            "[N] players cluster into [M] archetypes: [archetype A], [archetype B], [archetype C]",
            "[Archetype A] leads on [criterion]; [Archetype C] competes on [criterion]",
            "Purchase criteria centre on [expertise / brand / price], shifting by [buyer type]"]),
        ("Implication", [
            "Whitespace in [segment] where no incumbent holds [capability]",
            "[Target] is best positioned on [criterion]; exposed on [criterion]"]),
    ],
    "kpis": [
        ("[N]", "players benchmarked", None),
        ("[M]", "archetypes", None),
        ("~[XX]%", "market value covered", None),
    ],
    "sections": [
        {"kind": "content", "title": "Player set, tiering & archetypes",
         "headline": "We benchmark [N] players grouped into [M] archetypes",
         "left_title": "Players in scope",
         "body": [t("[Archetype A]: [Player 1], [Player 2] — [defining trait]", True),
                  t("[Archetype B]: [Player 3], [Player 4] — [defining trait]", True),
                  t("[Archetype C]: [Player 5], [Player 6] — [defining trait]", True),
                  t("Excluded: [players] — [reason]", level=1)],
         "so_whats": ["Grouping by archetype avoids a misleading flat ranking",
                      "Scope covers ~[X]% of market value"],
         "source": "Company filings, company sites, aqmen"},
        {"kind": "content", "title": "Comparison framework",
         "headline": "Players are compared on [K] decision-relevant criteria",
         "body": [t("[Criterion 1]: [what it measures and why it matters]", True),
                  t("[Criterion 2]: [what it measures and why it matters]", True),
                  t("[Criterion 3]: [what it measures and why it matters]", True),
                  t("Each criterion is scored relative to the strongest player", level=1)],
         "so_whats": ["Criteria are decision-relevant, not decorative",
                      "Scores are relative standing, not absolute"],
         "source": "aqmen framework"},
        {"kind": "harvey", "title": "Player × criteria benchmark",
         "headline": "[Archetype A] wins on [criterion]; [Archetype C] on price and speed",
         "row_header": "Purchase criterion",
         "columns": ["[Player 1]", "[Player 2]", "[Player 3]", "[Player 4]"],
         "rows": [("Domain expertise", [1.0, 0.75, 0.5, 0.5]),
                  ("Brand / reputation", [1.0, 0.75, 0.5, 0.25]),
                  ("Price competitiveness", [0.25, 0.5, 0.75, 1.0]),
                  ("Speed / agility", [0.5, 0.5, 0.75, 1.0]),
                  ("Breadth of offer", [0.75, 1.0, 0.5, 0.25])],
         "so_whats": ["No single player leads on every criterion",
                      "Trade-off: expertise/brand vs price/speed",
                      "[Target] can differentiate on [criterion]"],
         "source": "Expert interviews, company materials, aqmen"},
        {"kind": "chart", "title": "Quantitative comparison",
         "headline": "[Player 1] leads on [measured metric], but [Player 4] is closing",
         "chart_title": "[Metric] by player, [unit]",
         "chart": {"kind": "bar",
                   "categories": ["[Player 4]", "[Player 3]", "[Player 2]", "[Player 1]"],
                   "series": [("[Metric]", [42, 58, 71, 96])],
                   "number_format": "#,##0", "legend": False},
         "so_whats": ["[Player 1] ~[X]x [Player 4] on [metric]",
                      "Gap narrowing as [dynamic]"],
         "source": "Company filings, aqmen"},
        {"kind": "content", "title": "Positioning",
         "headline": "Each archetype wins in a distinct part of the market",
         "left_title": "Archetype profiles",
         "body": [t("[Archetype A] — strengths: [..]; weak on: [..]; wins in [segment]", True),
                  t("[Archetype B] — strengths: [..]; weak on: [..]; wins in [segment]", True),
                  t("[Archetype C] — strengths: [..]; weak on: [..]; wins in [segment]", True)],
         "so_whats": ["Positioning depends on the segment contested",
                      "Head-to-head only within an archetype"],
         "source": "aqmen analysis"},
        {"kind": "content", "title": "Reliability review",
         "headline": "Coverage is strong on [fields], thin on [fields]",
         "body": [t("Strong: [fields] — full coverage across players", True),
                  t("Moderate: [fields] — partial coverage"),
                  t("Weak: [fields] — [players] revenue-only; do not over-read")],
         "so_whats": ["Sparse cells are called out, not hidden",
                      "Revenue-only players are not treated as fully covered"],
         "watchout": "[field] is sparse for [players] — treat comparisons there as directional",
         "source": "aqmen analysis"},
        {"kind": "content", "title": "Implications",
         "headline": "Whitespace sits in [segment]; [target] is positioned to take it",
         "body": [t("Whitespace: [where no incumbent holds the capability]", True),
                  t("Threats: [who could contest it and how]"),
                  t("So-what: [the action the finding implies for the deal]", True)],
         "so_whats": ["Clear route to differentiated share",
                      "Watch [threat] over the hold period"],
         "source": "aqmen analysis"},
    ],
    "sources": [
        ("[Company filings / annual reports]", 5, "revenue, share, headcount"),
        ("[Investor materials / company sites]", 4, "positioning & offer"),
        ("[Analyst / industry sources]", 4, "market shares"),
        ("[Expert interviews]", 3, "qualitative benchmarking"),
    ],
}


COMPANY_ANALYSIS = {
    "title": "[Target] — Company Analysis",
    "subtitle": "Financial baseline, value creation & valuation — CDD",
    "doctype": "Company Analysis",
    "agenda": {"items": ["Context", "Company Analysis", "Valuation", "Appendix"],
               "active": "Company Analysis"},
    "bottom_line": ("[Target] is worth ~$[XX]–[XX]m (base ~$[XX]m) on a [X]-year "
                    "DCF; value is created by [lever] lifting margin ~[XXX]bps."),
    "confidence": 4,
    "exec_summary": [
        ("Objective", [
            "Assess [target]'s financial trajectory and value the business",
            "Question answered: what is it worth, and where is the value created?"]),
        ("Valuation", [
            "Enterprise value of ~$[XX]–[XX]m (base ~$[XX]m) on a [X]-year DCF",
            "Terminal value is ~[XX]% of EV — [flag if it dominates]",
            "WACC of [X]%; implied [X]x [metric]"]),
        ("Value creation", [
            "Revenue growing ~[X]% with margin expanding ~[XXX]bps by year [Y]",
            "Key levers: [lever 1], [lever 2] — see scenarios"]),
    ],
    "kpis": [
        ("~$[XX]m", "Enterprise value (base)", None),
        ("~[X]%", "Revenue CAGR", "▲ [XXX]bps margin"),
        ("[X]%", "WACC", None),
    ],
    "sections": [
        {"kind": "content", "title": "Business & scope",
         "headline": "[Target] is a [what it does]; we model [period] on [basis]",
         "left_title": "Business & scope",
         "body": [t("Business: [products / customers / geographies]", True),
                  t("Model: [P&L / DCF] over [historicals] + [forecast years]"),
                  t("Inputs vs computed clearly flagged throughout", level=1),
                  t("Figures directional unless sourced to filings", level=1)],
         "so_whats": ["Scope matches the decision the model informs",
                      "Assumptions separated from computed outputs"],
         "source": "[target] filings, management information, aqmen"},
        {"kind": "chart", "title": "Revenue trajectory",
         "headline": "Revenue grows ~[X]% to ~$[XX]m by [year]",
         "chart_title": "Revenue, $m",
         "chart": {"kind": "column",
                   "categories": ["'22", "'23", "'24", "'25E", "'26E", "'27E"],
                   "series": [("Revenue", [120, 138, 151, 168, 189, 212])],
                   "number_format": "#,##0", "legend": False},
         "so_whats": ["Growth driven by [driver]", "Forecast years flagged (E)"],
         "source": "[target] filings, aqmen"},
        {"kind": "chart", "title": "Margin bridge",
         "headline": "EBITDA margin expands ~[XXX]bps as [driver] scales",
         "chart_title": "EBITDA margin bridge, % of revenue",
         "chart": {"kind": "stacked_column",
                   "categories": ["'24 margin", "Volume", "Price/mix", "Cost", "'27E margin"],
                   "series": [("Contribution (pp)", [18.0, 1.5, 2.0, 1.5, 23.0])],
                   "number_format": "#,##0.0", "legend": False},
         "so_whats": ["Margin story is [operating leverage / mix]",
                      "Downside if [risk] materialises"],
         "source": "aqmen analysis", "illustrative": True},
        {"kind": "content", "title": "Operating drivers & KPIs",
         "headline": "The forecast rests on [N] operating levers",
         "body": [t("[KPI 1]: [assumption] — INPUT", True),
                  t("[KPI 2]: [assumption] — INPUT", True),
                  t("[KPI 3]: [computed from KPI 1 × KPI 2] — COMPUTED"),
                  t("Sanity check: [ratio] stays within [range]", level=1)],
         "so_whats": ["Inputs (assumptions) marked distinctly from computed figures",
                      "Each lever traces to a source"],
         "source": "[target] filings, aqmen"},
        {"kind": "content", "title": "Working capital & cash flow",
         "headline": "Cash conversion is ~[XX]%; working capital is a [use/source]",
         "body": [t("EBITDA-to-cash conversion ~[XX]% after capex and working capital", True),
                  t("Working capital: [DSO / DIO / DPO] dynamics"),
                  t("Watch-out: [seasonality / one-off] in [period]", level=1)],
         "so_whats": ["Cash quality [supports / pressures] the valuation",
                      "Working-capital swing modelled explicitly"],
         "source": "[target] filings, aqmen"},
        {"kind": "chart", "title": "DCF valuation",
         "headline": "Enterprise value of ~$[XX]–[XX]m on the base case",
         "chart_title": "DCF enterprise value, $m",
         "chart": {"kind": "bar", "categories": ["Low", "Base", "High"],
                   "series": [("EV", [180, 210, 245])],
                   "number_format": "#,##0", "legend": False},
         "so_whats": ["Range reflects WACC and terminal-growth spread",
                      "Terminal value ~[XX]% of EV (sanity check)"],
         "source": "aqmen DCF"},
        {"kind": "chart", "title": "Sensitivity",
         "headline": "Value is most sensitive to [WACC / terminal growth / margin]",
         "chart_title": "EV sensitivity, $m",
         "chart": {"kind": "bar",
                   "categories": ["Margin ±100bps", "Growth ±50bps", "WACC ±50bps"],
                   "series": [("Low", [188, 182, 176]), ("High", [232, 238, 246])],
                   "number_format": "#,##0"},
         "so_whats": ["WACC dominates the range",
                      "Terminal assumptions warrant the most diligence"],
         "source": "aqmen DCF", "illustrative": True},
        {"kind": "scenario", "title": "Scenario",
         "headline": "[Initiative]: [one-line thesis] adds ~$[X]m of EV",
         "left_title": "Initiative (qualitative thesis)",
         "body": [t("[Directional thesis in plain words — the value-creation lever]", True),
                  t("Overrides vs Base (quantitative):"),
                  t("[driver] [assumption] → [value] (was [base])", level=1),
                  t("[driver] [assumption] → [value] (was [base])", level=1)],
         "so_whats": ["Thesis in words, then the numbers that implement it",
                      "Base case shown before this scenario"],
         "source": "aqmen analysis"},
    ],
    "sources": [
        ("[Target] 10-K / annual report", 5, "historical financials"),
        ("Management information", 5, "KPI build & forecast assumptions"),
        ("[Capital IQ / PitchBook]", 4, "comparables & WACC inputs"),
        ("[News / trade press]", 3, "directional colour only (news cap 3)"),
    ],
}


# skill-name stem  ->  content
MODULES = {
    "market-sizing": MARKET_SIZING,
    "competitive-landscape": COMPETITIVE_LANDSCAPE,
    "company-analysis": COMPANY_ANALYSIS,
}
