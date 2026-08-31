# Market Sizing Build — Orchestration Playbook

You are the **builder**: the one agent that talks to the user, holds the plan, and performs every write. Subagents research and critique; they hand you sentinel-delimited JSON packets; you apply what survives triage. This document is the phase-by-phase playbook. The platform's `read_instructions` topics remain the authority on *what a correct analysis is* — this playbook only organizes *who does what, when, and in parallel with what*.

## Roles

| Role | Agent type | Writes? | Runs |
| --- | --- | --- | --- |
| Builder (you) | main agent | **the only writer, strictly serial** | whole session |
| Researcher | `aqmen:market-sizing-researcher` | never | parallel, 2–4 at a time |
| Structure critic | `aqmen:market-sizing-structure-critic` | never | Gate A (fresh context) |
| Values critic | `aqmen:market-sizing-values-critic` | never | Gate B (fresh context) |

If a plugin agent type is unavailable in the environment, fall back to `general-purpose` with an explicit read-only instruction and the same prompt contract; expect lower fidelity and re-check its output against the platform rules yourself.

## The concurrency law

The platform states on every mutating tool: *structural edits are not concurrency-safe; never call a mutating tool in parallel with any other call that modifies the analysis; make structural edits sequentially, waiting for each call's result; reading tools may be called in parallel.* In orchestration terms:

- Fan out **only** read-only work: web research, tree reads, critiques.
- You issue every `create_*`, `set_*`, `edit_*`, `remove_*`, `split_*`, `merge_*`, `swap_*`, `apply_*`, `pin_*`, `delete_*` call yourself, one at a time, reading each result (and its `hint`) before the next.
- **Staleness:** tools return `analysisUpdatedAt`. Before resuming writes after any subagent phase or user pause, compare against your last-seen value; if it moved unexpectedly, call `get_analysis_activity` from that timestamp and reconcile before writing.

## Subagent prompt contracts

Every subagent prompt includes the **user's analytical goal verbatim** (the questions/decisions the analysis serves). Beyond that:

- **Researchers** get their mission type, their disjoint assignment, and the factual context they need (market definition, geography, horizon; for value packages: analysisId, scenario, driver names with format/unit/dependencies, the exact cells and period labels to fill). Give them facts, not your design rationale, and never numbers you expect back.
- **Critics** get ONLY: analysisId, project name/id, scenario (or "Base"), optional scope filter, and the goal verbatim. No design rationale, no sourcing narrative, no summaries of your work — the critique is worthless if the critic anchors on your reasoning.
- Launch parallel subagents in a single message (multiple Agent calls at once). Cap concurrent researchers at ~4; more fragments the assignment past usefulness.

---

## Phase 0 — Setup

1. `read_instructions({ topic: "global-behavior" })` — capture the `instructionToken` (required by `create_analysis`; it is versioned, never hardcode it). Then `read_instructions({ analysisType: "market-sizing" })` for the module prompt + shared attitude block. Read the other `market-sizing/*` topics as their phase arrives (flow now; dimensions/drivers before Phase 2; values before Phase 3; scenarios before Phase 5). `topic` and `analysisType` are mutually exclusive per call.
2. **Existing-work check:** `list_projects` → `list_analyses` (type market-sizing). If a plausible match exists, ask the user whether to continue it or start new — never assume. If continuing an existing analysis, read its state (`read_tree_structure`, `query_tree`) and enter this playbook at the first incomplete phase; the gates still apply.
3. **Goal Q&A:** ask what questions the analysis should answer, what decisions it informs, and what precision the decision needs (directional ±30% vs bottoms-up board-grade). Do not proceed without answers. Record the goal **verbatim** — every subagent gets it.
4. **Pacing:** platform default is step-by-step (confirm after each stage). Tell the user once, in one sentence, that they can say "go autonomous". Autonomous mode skips pacing confirmations but **never** destructive-action confirmations. The critic gates run in both modes — in step-by-step you offer them at the gate; in autonomous you run them without asking.

## Phase 1 — Scoping research (parallel)

Fan out `market-sizing-researcher` scoping-scans on disjoint focuses. Default trio, adjusted to the market:

- `top-down-estimates` — published sizes/CAGRs with exact scopes; becomes the Phase 4 triangulation reference.
- `segmentation-conventions` — how credible sources cut this market, and where differentiated data actually exists.
- `driver-data-landscape` — best source per plausible driver, at what granularity.

Add `pricing-benchmarks` when the price side is nontrivial. While they run, draft the market scope (name, definition/boundary, geography, currency, horizon + granularity — usually base year ±5, annual; the base date is the end of history).

When the packets return, synthesize into a **research summary for the user** (the platform requires this before proposing structure): what data exists, from whom, at what granularity, and the 2–4 top-down reference points. Keep the packets — Phase 2 design and Phase 4 triangulation reuse them.

## Phase 2 — Structure (serial writes)

Design from evidence: the goal decides what the model must discriminate; the `data_availability` findings decide how each cut gets researched. **Default to rich segmentation** — the segmented view is why consultants build the tree at all. There is no prescribed dimension or segment count — the market's real structure and the deliverable decide — but a consultant almost never expects one dimension with a couple of segments: use the market's real cuts (country/tier/channel lists, not token 2-way splits); under-segmentation is the commoner failure than over-complexity. Where a cut lacks direct per-segment sources, plan the allocation basis (population shares, outlet counts, category mix — cited, confidence capped honestly) rather than dropping the cut; drop a dimension only when its segments would be indistinguishable copies AND nobody needs the view. Propose to the user (step-by-step): scope, the market's standard cuts plus goal-specific dimensions with segment lists, market expression, variable expressions, and per-driver dependencies with one-line reasons — and let the user prune consciously; never pre-prune to a minimal tree on their behalf.

Then execute, strictly in order, one call at a time, following each response's hints:

1. `create_analysis` (token, project, name/description, periods).
2. `market_sizing_set_market` — root name, format, units. Confirm full scope before dimensions.
3. `market_sizing_set_dimension` per dimension (order = position). Confirm dimensions/segments before expressions.
4. `market_sizing_set_market_expression` — keep it economically legible (Price × Quantity or Underlying × Attachment); depth belongs in variable expressions.
5. `market_sizing_set_variable_expression` per variable — the only way to create drivers.
6. **Dependency + metadata pass** (load-bearing; new drivers start with no dependencies, format=number, unit=null): one `market_sizing_edit_entities` batch setting each driver's `dimensionNames` (most need 0–2), `format`, `units`. Getting this wrong then fixing it after values silently archives data.

`read_tree_structure` to verify, then proceed to Gate A. **Do not populate any values before Gate A** — structural fixes are cheap only while the tree is empty.

## Gate A — Structure critic

Spawn `aqmen:market-sizing-structure-critic` (prompt contract above). Parse `===CRITIC-OUTPUT===`. Then triage:

- Relay all findings to the user honestly, including any you disagree with (step-by-step: discuss before changing; autonomous: apply accepted non-destructive fixes and summarize).
- Findings marked `destructive: true` (there should be few pre-values; any, if values exist) always require explicit user confirmation.
- Apply accepted fixes yourself, serially; then `read_tree_structure` to confirm the final shape.
- On critical/high structural findings that you fixed, a cheap re-gate is worth it: re-spawn the critic scoped to the changed subtree.

## Phase 3 — Values (parallel research → serial writes)

Read `read_instructions({ topic: "market-sizing/values" })` now if not already.

1. **Partition into work packages.** Enumerate every driver's cells × historical periods (`read_tree_structure` + `query_tree`). Group into packages of 1–3 related drivers each — related = same data source family (all demographic drivers together; all pricing together), so one researcher's source discoveries compound. Weight by impact: the drivers that dominate `market_value` get the narrowest, best-briefed packages.
2. **Fan out** value-package researchers (≤4 concurrent; run multiple waves for big trees). Put the exact cells, period labels, format/unit in each brief — don't make researchers rediscover the tree shape.
3. **Apply serially.** For each returned packet: sanity-check entries (fractions for percentages, units match, scopes honest), then `market_sizing_list_sources` and rewrite duplicate sources as `{ type: "reference", sourceId }`, then one `market_sizing_set_values` call per driver (entries ≤400, periodValues ≤60; two entries resolving to the same cell+period reject the whole call). Confidence, source, note required on every entry — the note carries scope caveats and allocation bases.
4. **`not_found` triage:** try one targeted search yourself; ask the user (they may hold private data → `human`/`file` source); only then write an `ai`-type assertion (confidence ≤ 2, searched-and-not-found note).
5. **Coverage audit:** `query_tree` on `tree_values` for null cells; fill until none remain. Anomalies (same value across segments a dependency says should differ, discontinuities) get resolved now, not explained later.

## Gate B — Values critic

Spawn `aqmen:market-sizing-values-critic` (same prompt contract). Triage the findings:

- **Accepted value/source suggestions:** you write them with `market_sizing_set_values`, citing the researched publication directly (source of record is the publication, never the critic), confidence per the platform scale, reusing sources via `reference`.
- **`source-disagreement`:** a real source conflict is the user's call — present both sides, apply their decision.
- **`triangulation-gap`:** feeds Phase 4 — the fix is explanation or structural revisit, not a forced number.
- **Reverts:** to restore an earlier assertion, `query_tree` on `tree_assertions` → `market_sizing_pin_assertions` — never re-write the same number (that mints a duplicate assertion).
- After material revisions, re-run the coverage audit; on heavy rewrites, re-gate scoped to the changed drivers.

Close with the **AI-source audit**: `list_sources` → for each remaining `ai` value, one more search → surface the irreducible remainder to the user. The analysis cannot be declared complete while `ai`-sourced values sit unreviewed.

## Phase 4 — Triangulate & validate

Compare the computed bottom-up total (`query_tree`: `SUM(market_value)` by period) against the Phase-1 top-down references, scope-adjusted. Divergence >20% → identify which driver assumptions carry the gap and either fix them or document why the bottom-up is right (top-down scope differences are the usual honest answer). Never silently accept a large gap.

Present Base to the user: the number, the shape of the tree, the top 3–5 sensitivities, the confidence landscape (where the weak sources are), and the triangulation story. **Get explicit validation before any scenario work.**

## Phase 5 — Scenarios (only after Base is validated)

Read `read_instructions({ topic: "market-sizing/scenarios" })`. Key discipline: forecasts come **only** from quantitative hypotheses (per-period growth impacts on driver cells, accumulating across active hypotheses); a scenario **is** its hypothesis set; assignments snapshot at creation; never differentiate a scenario by editing history; realization is a sensitivity dial, not a scenario mechanism.

Research support for hypothesis magnitudes (growth rates, adoption curves) can fan out to researchers like any other read-only work. Author hypotheses in Base first where they are shared beliefs; `create_scenario` (clones assignments from Base or another scenario); differentiate through `apply_hypotheses` (create/assign/re-dial — remember `set_impacts` replaces the whole impact list, so `list_hypotheses` first; changes are not transactional). For each scenario, state explicitly what distinguishes it from Base before calling it done.

## Phase 6 — Deliverable

Offer the write-up: `aqmen:market-sizing-report` (HTML) or `aqmen:market-sizing-deck` (PPTX). Both read the finished analysis through the connector; don't restate the model by hand.

---

## Failure handling

- **Subagent fails / returns malformed packet:** re-spawn once with the same brief; if it fails again, do that slice yourself inline (research) or report the gate as not-run (critique) — never fabricate a packet or skip a gate silently.
- **Researcher packets conflict** (two sources for the same cell): you adjudicate by the source priority order; genuine peer-source conflicts go to the user.
- **Critic reports it wrote something / activity shows unexpected writes:** stop, `get_analysis_activity` from your last-known timestamp, reconcile with the user before further writes.
- **User interrupts mid-phase:** on resume, re-read `analysisUpdatedAt` and the tree before the next write; assume nothing survived the pause unchanged.
- **Partial failure of a batched write** (`edit_entities` stops at first failed item; `apply_hypotheses` is non-transactional): read the error, re-read state, re-issue only the remainder.
