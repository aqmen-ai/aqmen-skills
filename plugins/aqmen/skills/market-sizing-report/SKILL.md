---
name: market-sizing-report
description: Generate a standardized aqmen market sizing output report as a self-contained HTML file. Use when the user wants to produce, write, generate, or export a market sizing report, output, conclusion, summary, or deliverable from a market sizing analysis — especially in a workspace connected to the aqmen MCP connector. Applies aqmen's house structure, design system, and source/confidence conventions so every market sizing output is consistent and decision-grade.
---

# Aqmen Market Sizing Report

Produce a **decision-grade market sizing report** as a single self-contained
HTML file, in aqmen's house style, so every market sizing output looks and reads
consistently.

## When to use

Trigger when the user asks for a market sizing **report / output / conclusion /
summary / deliverable** — e.g. "write up the market sizing", "generate the TAM
report", "produce the output for this sizing". For the underlying analysis
(building the driver tree, setting values), that's the aqmen MCP tools' job —
this skill is about the **write-up**.

## Inputs

Assemble from the analysis data already in context. If the aqmen MCP connector
is available, read the market sizing analysis through it (market definition,
dimensions, driver tree, values, computed size, scenarios). **Never invent
numbers** — if something needed for a section is missing, mark it as a gap
(see the caveat callout) rather than filling it in.

## How to build the report

First, **gather the full analysis from the aqmen MCP** — read `references/report-data.md` (how to pull the data and turn its per-value sources & confidence into citations and watch-outs) and the **What to gather from aqmen** section of `references/market-sizing-content.md`. Build the report only once you have the whole model; never invent numbers or sources.

1. Read `references/report-standards.md` — the voice, base-first discipline, and
   the sources & confidence rules every aqmen report must follow.
2. Read `references/report-style.md` — the aqmen design system (layout,
   typography, color tokens, components, chart rules) and the hard constraints.
3. Read `references/market-sizing-content.md` — the single source of truth for what the deliverable covers, the module rules, and what to gather — then `references/market-sizing-structure.md` — the required section order and
   what belongs in each.
4. Build **on top of** `references/market-sizing-report-template.html` — the
   populated, fully-styled example for this module (it mirrors the deck's content,
   so report and deck show the same information). **Do not regenerate the HTML from
   scratch — that is slow and costly, and it drifts from the house style.** Instead:
   - **First copy the template to your output path** with a shell command, e.g.
     `cp "references/market-sizing-report-template.html" market-sizing-report.html`.
     This carries the whole shell — CSS, CSP, `<head>`, and the inlined logo — at
     zero token cost.
   - **Then edit only the content in that copy** with targeted `Edit` calls: swap the
     `[bracketed]` placeholders and the example body text, section by section,
     following the section order. **Never rewrite the whole file with `Write`, and
     never re-emit the `<style>` block or the base64 logo** — leave everything
     outside the body content byte-for-byte as the template has it.
   - Keep it a **single HTML file** (inline CSS/JS, `data:` images) that renders in
     a sandboxed, cross-origin iframe. Charts use the ECharts library already loaded
     from cdnjs in the template — don't change that include or the CSP, and don't add
     other external resources.
5. Lead with the so-what. Present the **Base case before any scenario**. End with
   the **Sources & confidence** section.

## Saving the report

If the aqmen MCP connector is available, the finished HTML can be stored back in the project's Files as an artifact (where it renders inline).
This skill does not upload on its own — offer it, and let the user confirm.

## Non-negotiables

- Single HTML file; the only external resource is the pinned ECharts CDN
  already in the template — don't add others or loosen the CSP.
- Consulting-grade, concise, decision-oriented; so-what first.
- Every value attributed (source, confidence, note); facts vs. estimates
  labelled.
- Surface gaps and sparse data honestly — never imply completeness.
