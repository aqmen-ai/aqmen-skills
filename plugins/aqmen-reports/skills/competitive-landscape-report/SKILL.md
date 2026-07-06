---
name: competitive-landscape-report
description: Generate a standardized aqmen competitive landscape output report as a self-contained HTML file. Use when the user wants to produce, write, generate, or export a competitive landscape report, output, conclusion, benchmarking write-up, summary, or deliverable from a competitive landscape analysis (player/field dataset grid) — especially in a workspace connected to the aqmen MCP connector. Applies aqmen's house structure, design system, and source/confidence conventions so every competitive landscape output is consistent and decision-grade.
---

# Aqmen Competitive Landscape Report

Produce a **decision-grade competitive landscape report** as a single
self-contained HTML file, in aqmen's house style, so every competitive landscape
output looks and reads consistently.

## When to use

Trigger when the user asks for a competitive landscape **report / output /
conclusion / benchmarking write-up / summary / deliverable** — e.g. "write up
the competitive landscape", "produce the benchmarking output", "summarize the
player comparison". Building the dataset (players, fields, assertions) is the
aqmen MCP tools' job — this skill is about the **write-up**.

## Inputs

Assemble from the analysis data already in context. If the aqmen MCP connector
is available, read the competitive landscape through it (player set & tiering,
fields, the dataset grid, coverage/reliability, scenarios). **Never invent
numbers** — if something needed for a section is missing, mark it as a gap (a
caveat callout) rather than filling it in.

## How to build the report

First, **gather the full analysis from the aqmen MCP** — read `references/report-data.md` (how to pull the data and turn its per-value sources & confidence into citations and watch-outs) and the **What to gather from aqmen** section of the structure file. Build the report only once you have the whole model; never invent numbers or sources.

1. Read `references/report-standards.md` — the voice, base-first discipline, and
   the sources & confidence rules every aqmen report must follow.
2. Read `references/report-style.md` — the aqmen design system (layout,
   typography, color tokens, components, chart rules) and the hard constraints.
3. Read `references/competitive-landscape-structure.md` — the required section
   order and what belongs in each.
4. Start from `references/report-template.html` and fill it in, following the
   section order. Keep it a **single HTML file** (inline CSS/JS, `data:` images)
   that renders in a sandboxed, cross-origin iframe. Charts use the ECharts
   library already loaded from cdnjs in the template — don't change that include
   or the CSP, and don't add other external resources.
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
  labelled; web figures cited with URLs.
- Be honest about coverage — tier players correctly and call out sparse
  data explicitly; never imply completeness.
