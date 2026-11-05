---
name: company-analysis
description: 'Analyse a company on the Aqmen platform end to end — its reported statements tied out, a driver-based forecast, a valuation if needed — from the question to approved findings and a deck. Use for "analyse company X", "build the P&L / the model for X", "does the management plan hold up", "forecast X''s revenue and margins", "value this company", "DCF for X", in a session connected to the Aqmen MCP. Follows the platform''s company-analysis playbook and chains the stage skills, with parallel researchers and fresh-context critics.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Analyse a company — the `company-analysis` playbook

The method lives on the platform, not in this skill. First,
`read_instructions` with topics `["start", "rules", "company-analysis"]`,
and follow the playbook stage by stage: read each stage's units as you
reach it (up to six topics per call), never from memory of a topic not
read this session.

## Stages and the skill each chains

| # | Stage | Skill | Reads |
| --- | --- | --- | --- |
| 1 | Set the question | `aqmen:scope` | `scope`, `projects`, `collections` |
| 2 | Read the disclosure | `aqmen:research` | `research`, `datasets`, `method-company` |
| 3 | Build the statements | `aqmen:model` | `model`, `method-company`, `spreadsheets` |
| 4 | Forecast from drivers — and value it, if needed | `aqmen:model` | `model`, `method-company`, `modeling` |
| 5 | Have it challenged | `aqmen:challenge` | `challenge`, `critics`, `method-company` |
| 6 | Write the findings | `aqmen:conclude` | `conclude`, `docs`, `charts` |
| 7 | Deliver it | `aqmen:deliver` | `deliver`, `standards`, `decks` |

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

## Resuming

`describe_workspace` with the project: its notes, Status first, say where
the work stands; then read the notes of what you touch. Pick up at the first
stage whose checks fail. The deck is the hand-over. A new filing or a
restatement: `refresh`. Inside a due diligence, `due-diligence` picks up
from the review.
