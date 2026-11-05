---
name: market-sizing
description: 'Size a market on the Aqmen platform end to end — TAM/SAM/SOM or a bottom-up driver model by segment — from the question to approved findings and a deck, every figure sourced and checked against a published estimate. Use for "size the market for X", "how big is the market for Y in Z", "build a TAM/SAM/SOM model", "market sizing for X in Y", "is the market the plan assumes really there", in a session connected to the Aqmen MCP. Follows the platform''s market-sizing playbook and chains the stage skills, with parallel researchers and fresh-context critics.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Size a market — the `market-sizing` playbook

The method lives on the platform, not in this skill. First,
`read_instructions` with topics `["start", "rules", "market-sizing"]`,
and follow the playbook stage by stage: read each stage's units as you
reach it (up to six topics per call), never from memory of a topic not
read this session.

## Stages and the skill each chains

| # | Stage | Skill | Reads |
| --- | --- | --- | --- |
| 1 | Set the question | `aqmen:scope` | `scope`, `projects`, `collections` |
| 2 | Research what exists | `aqmen:research` | `research`, `datasets` |
| 3 | Shape the model | `aqmen:model` | `model`, `modeling`, `method-market`, `spreadsheets` |
| 4 | Fill it with sourced values | `aqmen:research` | `research`, `datasets`, `sql` |
| 5 | Check it | `aqmen:challenge` | `challenge`, `critics`, `method-market`, `charts` |
| 6 | Write the findings | `aqmen:conclude` | `conclude`, `docs` |
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
stage whose checks fail. The deck is the hand-over. When the data moves,
`refresh`; inside a due diligence, `due-diligence` picks up from the check.
