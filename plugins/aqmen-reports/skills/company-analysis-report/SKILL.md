---
name: company-analysis-report
description: Generate a standardized aqmen company analysis output report as a self-contained HTML file. Use when the user wants to produce, write, generate, or export a company analysis report, output, conclusion, valuation write-up, summary, or deliverable from a company analysis (P&L model / DCF) — especially in a workspace connected to the aqmen MCP connector. Applies aqmen's house structure, design system, and source/confidence conventions so every company analysis output is consistent and decision-grade.
---

# Aqmen Company Analysis Report

Produce a **decision-grade company analysis report** as a single self-contained
HTML file, in aqmen's house style, so every company analysis output looks and
reads consistently.

## When to use

Trigger when the user asks for a company analysis **report / output / conclusion
/ valuation write-up / summary / deliverable** — e.g. "write up the company
analysis", "produce the valuation output", "summarize the P&L model". Building
the model itself (statements, nodes, DCF) is the aqmen MCP tools' job — this
skill is about the **write-up**.

## Inputs

Assemble from the analysis data already in context. If the aqmen MCP connector
is available, read the company analysis through it (income statement / margin
bridge, cash flow, working capital, KPIs, DCF valuation and WACC, scenarios).
**Never invent numbers** — if something needed for a section is missing, mark it
as a gap (a caveat callout) rather than filling it in.

## How to build the report

First, **gather the full analysis from the aqmen MCP** — read `references/report-data.md` (how to pull the data and turn its per-value sources & confidence into citations and watch-outs) and the **What to gather from aqmen** section of the structure file. Build the report only once you have the whole model; never invent numbers or sources.

1. Read `references/report-standards.md` — the voice, base-first discipline, and
   the sources & confidence rules every aqmen report must follow.
2. Read `references/report-style.md` — the aqmen design system (layout,
   typography, color tokens, components, chart rules) and the hard constraints.
3. Read `references/company-analysis-structure.md` — the required section order
   and what belongs in each.
4. Start from `references/report-template.html` and fill it in, following the
   section order. Keep it a **single HTML file** (inline CSS/JS, `data:` images)
   that renders in a sandboxed, cross-origin iframe. Charts use the ECharts
   library already loaded from cdnjs in the template — don't change that include
   or the CSP, and don't add other external resources.
5. Lead with the so-what (the valuation range or key finding). Present the
   **Base case before any scenario**. End with the **Sources & confidence**
   section.

## Saving the report

If the aqmen MCP connector is available, the finished HTML can be stored back in the project's Files as an artifact (where it renders inline).
This skill does not upload on its own — offer it, and let the user confirm.

## Non-negotiables

- Single HTML file; the only external resource is the pinned ECharts CDN
  already in the template — don't add others or loosen the CSP.
- Consulting-grade, concise, decision-oriented; so-what first.
- Every value attributed (source, confidence, note); facts vs. estimates
  labelled; inputs distinguished from computed figures.
- Valuation shown as a range with a terminal-value sanity check — no false
  precision.
- Surface gaps and out-of-scope statements honestly — never imply completeness.
