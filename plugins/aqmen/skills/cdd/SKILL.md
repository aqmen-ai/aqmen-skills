---
name: cdd
description: 'Run a commercial due diligence (CDD) on the aqmen platform end to end — the market, the competition and the company, from the brief to a deck in the workspace — with the user''s confirmation at each gate. Use when the user says "we''re running a CDD on X", "diligence on Y", "is there an opportunity in Z", "take this target from the question to the readout", "market study / investment case for…", or hands over a CDD brief or proposal. Drives the shared steps (scope, research, model, challenge, conclude, deliver) across the three CDD workstreams and holds the CDD deliverable standard.'
---

# CDD — commercial due diligence

A CDD answers one question for an investor or a board: **is there an
opportunity here, and what do you need to believe for it to be real?** It
does so through three workstreams, each a framework the platform teaches,
and ends in one deck whose every figure is the workspace's.

Read `references/practice.md` once per session, then
`references/cdd-storyline.md` (the deliverable's shape) and
`references/deliverable-standards.md`. Tell the user once, early, that they
can say "go autonomous".

## The questions a CDD answers

| Workstream | Questions | Method (platform topic) | Detail |
| --- | --- | --- | --- |
| **Market** | How large is the market, how fast is it growing, what drives it, where is the whitespace? | `market-sizing` | `references/workstream-market-sizing.md` |
| **Competition** | Who are the players, who is winning and why, where can the target win? | `competitive-landscape` | `references/workstream-competitive-landscape.md` |
| **Company** | How has the target performed, is its plan credible, what is it worth? | `company-analysis` | `references/workstream-company-analysis.md` |

Each workstream file says what its part of the deliverable covers, which
slides it contributes and how each exhibit is sourced, the report sections,
what to gather and the module rules. The **method** — stages, structure,
recipes, critic checklists — is the platform topic: read it fresh
(`read_instructions('modeling')`, then the workstream's topic) before
modeling. Do not work from memory of it.

Not every CDD needs all three. The brief decides: a market study is the
Market workstream alone; a buy-and-build adds Competition.

## Before the work: proposal and storyline

An engagement usually starts with **aqmen:proposal** (the scope the client
signs) and **aqmen:storyline** (the slide plan and the ghost deck). Neither
is required. When they exist, scope reads both: the client's questions
become the brief's questions, the hypotheses carry over rated, the plan's
data column becomes the research agenda, and the ghost deck in the
workspace is the deck `deliver` fills.

## The flow

Invoke each step skill with the Skill tool when you reach it and follow it in
full; do not paraphrase a step from memory. Run the workstreams in the
order the brief's dependencies need: usually Market first (Competition
reuses its definition and Company reconciles to it), Competition and
Company in parallel once the market is defined.

| # | Step | CDD-specific | Gate |
| --- | --- | --- | --- |
| 1 | **aqmen:scope** | Questions grouped by workstream; framework per workstream; deliverable = a deck in the workspace (optionally an HTML report) | The user confirms the brief |
| 2 | **aqmen:research** (scoping scan) | Researchers in parallel; one `players-and-filings` when Competition or Company is in scope | The user has seen what data exists and the gaps |
| 3 | **aqmen:model** (structure), per workstream | The workstream's topic stages | Structure proposed and confirmed |
| 4 | **aqmen:challenge** (model critic), per workstream | The topic's critic checklist | Findings resolved or accepted |
| 5 | **aqmen:research** (value packages) + **aqmen:model** (values) | Researchers in parallel, weighted by what moves the answer; the data loader one at a time | Every driver cited or a named gap; the model evaluates clean |
| 6 | **aqmen:challenge** (values critic) | Cross-workstream triangulation (below) | Findings resolved or accepted |
| 7 | The user validates Base and **what you need to believe** | Per workstream: the `Believe` block (`modeling`) walked through — verdicts, break-evens, sanity checks | An explicit yes, before any scenario or conclusion |
| 8 | **aqmen:conclude** | Insights answer the CDD questions; view builders in the background; **the skeptic** before validation | Every question answered or "cannot say"; critical IC challenges settled or carried as risks |
| 9 | **aqmen:deliver** | The CDD storyline; the standards below; the deck critic | Deck critic passed, nothing stale, shown; report if asked |
| 10 | Optional **aqmen:demo-prep** | The readout | Every question opens a saved figure |
| — | **aqmen:refresh** whenever data moves | Decks included | Nothing stale |

## Agents at each gate

| Gate | Agents | Mode |
| --- | --- | --- |
| Scoping scan (2) | `researcher` × 2–4, one per focus | Parallel, read-only |
| Structure (4) | `model-critic`, per workstream | Fresh context; the workstreams' critics in parallel |
| Values (5) | `researcher` × one per package → `data-loader` | Researchers parallel; one loader at a time per workspace |
| Values gate (6) | `values-critic` | Fresh context, per workspace or workstream in parallel; recheck after fixes |
| Scenarios (after 7) | `model-critic` on the scenario layer | Fresh context, once scenarios exist |
| Conclusions (8) | `view-builder` × one per question; **`skeptic` (on by default)** | Builders in the background; the skeptic fresh, on the recorded claims, before validation |
| Hand-over (9) | `deck-critic` | Fresh context; recheck after fixes |
| Refresh | `data-loader`, `view-builder` (broken views), critics if the model changed | As above |

The skeptic is on by default for a CDD: an investor's committee will ask
the hardest questions whether or not you have. The user may turn it off;
record that in the Log.

## Cross-workstream reconciliation

The three workstreams must tell one story. Before conclude, check and
record the result in the brief's Log:

- **Competition ↔ Market:** the players' market-specific revenues do not
  sum to more than the sized market, and the landscape uses the sizing's
  market definition (or says why not).
- **Company ↔ Market:** the target's revenue growth against the market's
  growth is a share gain or loss someone must believe — say which; its
  revenue is a plausible share of the SAM.
- **Project ↔ Market:** sites × units per site stays within the local SAM
  at a plausible share.

Each check is a sanity-check row in a `Believe` block (`modeling`), so it
stays live with the models. A break is a finding for **aqmen:challenge**,
not a footnote.

## The CDD deliverable standard

On top of `references/deliverable-standards.md`:

- **The storyline is fixed** (`references/cdd-storyline.md`): Context →
  Market → Competition → Company → Appendix, the executive summary first
  and written last. 25–35 slides for a demo or interim, 40–55 for a full
  readout.
- **Each workstream ends in its slides**, per its workstream file; the deck
  is one deck, not three.
- **Headlines are validated insights**, by source where the slide's
  headline is exactly the claim, and consistent with the verdicts.
- **What you need to believe is on a slide**, sourced from the `Believe`
  ranges (`references/cdd-storyline.md`).
- **Every workspace figure is sourced**; the deck critic passes before
  hand-over.
- **The IC's hard questions are in the deck.** The skeptic's critical
  challenges are answered on a slide or stated as risks; its hardest
  questions have a backup slide or a view.
- **Sources and confidence** close the deck; a source line on every
  content slide.

## Rules across the steps

- **Resume, don't restart.** At the start and whenever you return, read
  `describe_workspace` and the brief's Log; pick up at the first gate that
  does not hold.
- **The gates are not skippable**, in either pacing mode. Autonomous mode
  removes the pauses, never the gates, the critics, the skeptic, the Base
  validation or the confirmation of destructive changes.
- **Report at each gate** in a few plain sentences: what exists, what it
  says so far, what is next.
