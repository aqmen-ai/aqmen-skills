---
name: company-analysis-deck
description: Generate a standardized aqmen company analysis deliverable as a real, editable PowerPoint deck (.pptx) in aqmen's house "Discussion Materials" style. Use when the user wants to produce, write, generate, or export a company analysis deck, slides, presentation, PowerPoint, pptx, valuation deck, or client-facing deliverable from a company analysis (P&L model / DCF) — especially in a workspace connected to the aqmen MCP connector. Builds 16:9 slides with native editable charts (revenue/EBITDA bridges, DCF) via the aqmen_deck.py builder, applying aqmen's palette, type, slide chrome, and source/confidence conventions so every deck is consistent and decision-grade.
---

# Aqmen Company Analysis Deck

Produce a **decision-grade company analysis deck** as a real, editable
`.pptx` file in aqmen's house "Discussion Materials" style — the CDD deliverable
format clients receive — so every company analysis presentation looks and reads
consistently.

## When to use

Trigger when the user asks for a company analysis **deck / slides / presentation
/ PowerPoint / pptx / valuation deck / client deliverable** — e.g. "turn the
company analysis into a deck", "make the valuation slides", "export the P&L model
to PowerPoint". For a **document-style HTML report** instead, use
`company-analysis-report`. Building the model itself (statements, nodes, DCF) is
the aqmen MCP tools' job — this skill is the **presentation**.

## Inputs

Assemble from the analysis data in context. If the aqmen MCP connector is
available, read the company analysis through it (income statement / margin
bridge, cash flow, working capital, KPIs, DCF valuation & WACC, scenarios) — see
`references/report-data.md`. **Never invent numbers**; if something needed for a
slide is missing, mark it a gap rather than filling it in.

## How to build the deck

First, **gather the full model from the aqmen MCP** (`references/report-data.md`
and the *What to gather* section of `references/company-analysis-content.md`). Build only once you have
the whole model.

1. Read `references/report-standards.md` — voice, base-first discipline, and the
   sources & confidence rules every aqmen deliverable follows.
2. Read `references/deck-style.md` — the aqmen deck design system (palette, type,
   slide chrome, chart rules) and how the builder works.
3. Read `references/company-analysis-content.md` — the single source of truth for what the deliverable covers, the module rules, and what to gather — then `references/company-analysis-deck-structure.md` — the required slide
   order and which builder method to use for each.
4. Ensure `python-pptx` is installed (`pip install python-pptx`). Write a short
   Python script that imports `aqmen_deck` from `references/aqmen_deck.py`,
   instantiates `Deck(...)`, calls the slide builders in
   order, and `deck.save("<name>.pptx")`. `Deck()` self-brands (aqmen theme,
   Montserrat, master wordmark) — no base file needed. A populated,
   fully-styled starter deck for this module lives at
   `references/company-analysis-deck-template.pptx`; open it to see the house style, or
   build on it with `Deck(template="references/company-analysis-deck-template.pptx")`. Use **native charts** (`chart_slide`) — never
   paste chart images.
5. Lead with the so-what (the valuation range or key finding). Present the
   **Base case before any scenario**. Show valuation as a **range with a
   terminal-value sanity check** — no false precision. End with a **Sources &
   confidence** treatment.

## Saving the deck

The output is a `.pptx` that opens in PowerPoint / Google Slides with editable
charts. If the aqmen MCP connector is available, offer to store it back in the
project's Files as an artifact (it downloads rather than rendering inline). A PDF
can be produced with `soffice --headless --convert-to pdf <name>.pptx` if the
user wants one. Offer — don't upload unprompted.

## Non-negotiables

- Real editable `.pptx` built via `aqmen_deck.py`; native charts, never
  screenshots. Don't hand-author slide XML.
- Montserrat on the blue-dominant navy palette; navy leads, azure is the only
  accent. Standard chrome (DRAFT tag, eyebrow, wordmark, source, page number).
- So-what headline on every slide; Key Takeaways rail on analytical slides.
- Every value attributed; facts vs. estimates labelled; inputs distinguished from
  computed figures. Valuation shown as a range with a terminal-value sanity
  check.
- Base case before scenarios; directional exhibits tagged ILLUSTRATIVE. Never
  invent numbers. Close with Sources & confidence.
