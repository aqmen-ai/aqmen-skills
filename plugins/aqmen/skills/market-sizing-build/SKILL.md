---
name: market-sizing-build
description: Build a decision-grade market sizing analysis on the aqmen platform end-to-end, orchestrating parallel research agents and adversarial critic gates. Use when the user wants to build, create, or run a market sizing — "size the market for X", "build a TAM/SAM/SOM model", "market sizing for X in Y" — in a workspace connected to the aqmen MCP connector. Coordinates fan-out research (read-only, parallel) with a single serialized writer, and enforces two adversarial review gates (structure before values, values before completion) so the result meets aqmen's decision-grade bar. For the write-up afterwards, use aqmen:market-sizing-report or aqmen:market-sizing-deck.
---

# Aqmen Market Sizing Build

Build a **decision-grade market sizing** on the aqmen platform: a driver tree whose structure is justified by the decision question, whose every value is real, cited, and confidence-scored, whose bottom-up total is triangulated against published top-down figures, and whose scenarios are expressed through named hypotheses.

## Division of authority

**The platform is the spec; this skill is the orchestration.** The aqmen MCP's `read_instructions` topics define what a correct analysis is — workflow stages, dimension/driver rules, confidence scale, source types, destructive-action rules. Always read them fresh at the start of a build (`topic: "global-behavior"` first — it returns the `instructionToken` that `create_analysis` requires — then `analysisType: "market-sizing"`, then the `market-sizing/*` topics as each phase needs them). Where this skill and a live `read_instructions` response ever disagree, the platform wins.

What this skill adds on top:

1. **Parallel research, serial writes.** The platform's tools are explicit: structural edits are not concurrency-safe. So all fan-out is **read-only** — researcher and critic subagents that search, read, and report — and **you (the main agent) are the only writer**, applying every mutation sequentially, one call at a time.
2. **Adversarial gates.** Two fresh-context critics audit the work at the moments fixes are cheapest: the **structure critic** after the tree is shaped but before values exist, and the **values critic** after values are in but before the analysis is declared complete. Critics get no builder rationale — they judge the stored model cold.
3. **Work-package handoffs.** Subagents return structured JSON packets (sentinel-delimited) that you apply; the contracts live in the agent definitions.

## The flow

Read `references/orchestration.md` — the full phase-by-phase playbook — before starting. In brief:

- **Phase 0 — Setup.** `read_instructions`, existing-work check (`list_projects`/`list_analyses` — never create first), goal Q&A with the user, pacing mode (step-by-step is the platform default; tell the user once they can say "go autonomous").
- **Phase 1 — Scoping research (parallel).** Fan out 2–4 `market-sizing-researcher` agents on disjoint scoping-scan focuses (top-down estimates, segmentation conventions, driver data landscape, pricing). Synthesize into the research summary the platform requires before any structure is proposed.
- **Phase 2 — Structure (serial writes).** Design the decomposition from goal + evidence; confirm scope with the user; then `create_analysis` → `set_market` → dimensions → market expression → variable expressions → the deliberate dependency/format/units pass. One write at a time, following each tool's hints.
- **Gate A — Structure critic.** Spawn `market-sizing-structure-critic` (fresh context, goal verbatim, no rationale). Triage findings with the user (step-by-step) or apply accepted non-destructive fixes (autonomous); destructive fixes always need explicit user confirmation.
- **Phase 3 — Values (parallel research → serial writes).** Partition drivers into impact-weighted work packages; fan out researchers; you review each packet and write it with `market_sizing_set_values`, reusing sources via `list_sources`. Audit coverage with `query_tree` until no gaps.
- **Gate B — Values critic.** Spawn `market-sizing-values-critic`. Apply accepted suggestions yourself, citing the researched publication (never "the critic"). Then the AI-source audit.
- **Phase 4 — Triangulate & validate.** Bottom-up vs Phase-1 top-down figures; explain >20% gaps; present Base to the user for explicit validation.
- **Phase 5 — Scenarios (only after Base is validated).** Hypotheses-first, per the platform's scenarios topic; a scenario is its hypotheses.
- **Phase 6 — Deliverable.** Offer `aqmen:market-sizing-report` / `aqmen:market-sizing-deck`.

## Non-negotiables

- **Rich segmentation by default.** The segmented view is why the tree exists: consultants want the market split, not one number. There is no prescribed dimension or segment count — the market's real structure and the deliverable decide — but a consultant almost never expects one dimension with a couple of segments. Missing per-segment data is a research problem (find an allocation basis, cite it, cap confidence) — not a reason to flatten the tree. Simplification requires justification; the richer cut does not.
- **Never parallelize writes.** No two mutating calls in flight at once, ever — not even to "different parts" of the tree. Reads may run in parallel.
- **Critics and researchers never write.** If a subagent reports having written anything, treat the model as suspect: check `get_analysis_activity` before continuing.
- **Fresh-context critics.** Spawn via the Agent tool with the critic agent types; pass only analysisId, project, scenario, optional scope, and the user's goal verbatim. Never run a critique inline in your own context — you would anchor on your own reasoning.
- **Never invent numbers.** Unsourced figures enter the model only as explicit `ai`-type assertions (confidence ≤ 2, searched-and-not-found note) and must survive the AI-source audit before completion.
- **Destructive actions always confirmed** with the user, in both pacing modes.
- **Honest completion.** The analysis is "done" only when: no empty cells, no unreviewed `ai` sources, both gates run, triangulation explained, Base explicitly validated by the user.
