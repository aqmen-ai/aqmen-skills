---
name: due-diligence
description: 'Run a commercial due diligence (CDD) on the Aqmen platform end to end — the market, the competition and the company as workstreams of one project, reconciled into one answer, its red flags, approved findings and one deck. Use when the user says "we''re running a CDD on X", "diligence on Y", "is there an opportunity in Z", "take this target from the question to the readout", "market study / investment case for…", or hands over a CDD brief or proposal. Follows the platform''s due-diligence playbook and chains the analysis skills, with parallel researchers, fresh-context critics and the skeptic before approval.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Run a due diligence — the `due-diligence` playbook

The method lives on the platform, not in this skill. First,
`read_instructions` with topics `["start", "rules", "due-diligence"]`,
and follow the playbook stage by stage: read each stage's units as you
reach it (up to six topics per call), never from memory of a topic not
read this session.

## Stages and the skill each chains

| # | Stage | Skill | Reads |
| --- | --- | --- | --- |
| 1 | Set the investment question | `aqmen:scope` | `scope`, `projects`, `collections` |
| 2 | Size the market | `aqmen:market-sizing` | `market-sizing`, `method-market` |
| 3 | Map the competition | `aqmen:competitive-landscape` | `competitive-landscape`, `method-competition` |
| 4 | Test the company | `aqmen:company-analysis` | `company-analysis`, `method-company` |
| 5 | Reconcile, and name the red flags | `aqmen:challenge` | `challenge`, `critics`, `modeling` |
| 6 | Write the findings | `aqmen:conclude` | `conclude`, `critics`, `docs` |
| 7 | Deliver the report | `aqmen:deliver` | `deliver`, `standards`, `decks` |

## What Claude adds

- **Chain the stage skills.** At each stage, invoke its skill with the
  Skill tool and follow it inside the stage: the practice says how, the
  playbook's checks and gate say when the stage is done. A stage with no
  skill runs from the units it reads.
- **Subagents where the platform allows a self-review.** Research passes
  run as parallel researchers (`aqmen:research`); every critic gate
  spawns a fresh-context critic (`aqmen:challenge`) — never a critique in
  your own context.
- **Keep the project's notes current.** After each stage and gate, its
  Status says where the job is and what it waits for, Decisions and Open
  are updated in place, and the Log gets a line — so any session, or any
  agent, resumes from the project. One stage per session is fine.
- **The workstreams are playbooks.** Each workstream stage runs its own
  playbook skill (`aqmen:market-sizing`, `aqmen:competitive-landscape`,
  `aqmen:company-analysis`) inside this one project, in its workstream's
  collection, through Base; the findings and the deck are the deal's. Market
  first — the others read its definition; then Competition and Company may
  run side by side: their researchers and critics in parallel, one data
  loader at a time per workspace.
- **The skeptic by default.** Before the user approves the findings, spawn
  `aqmen:skeptic` fresh on the findings doc (`aqmen:conclude`); keep its
  hardest questions for whoever presents.

## Resuming

`describe_workspace` with the project: its notes, Status first, say where
the work stands; then read the notes of what you touch. Pick up at the first
stage whose checks fail. The deck is the hand-over. When the data moves,
`refresh` the whole project.
