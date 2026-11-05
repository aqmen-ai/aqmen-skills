---
name: competitive-landscape
description: 'Map the competition on the Aqmen platform end to end — the long list of players, benchmarked on comparable sourced fields, grouped into archetypes — from the question to approved findings and a deck. Use for "benchmark the players in X", "who competes with Y", "competitive landscape for Z", "how does X compare with its peers", "map the market''s players", in a session connected to the Aqmen MCP. Follows the platform''s competitive-landscape playbook and chains the stage skills, with parallel researchers and fresh-context critics.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Map the competition — the `competitive-landscape` playbook

The method lives on the platform, not in this skill. First,
`read_instructions` with topics `["start", "rules", "competitive-landscape"]`,
and follow the playbook stage by stage: read each stage's units as you
reach it (up to six topics per call), never from memory of a topic not
read this session.

## Stages and the skill each chains

| # | Stage | Skill | Reads |
| --- | --- | --- | --- |
| 1 | Set the question and the market | `aqmen:scope` | `scope`, `projects`, `collections` |
| 2 | The long list, tiered | `aqmen:research` | `research`, `method-competition`, `datasets` |
| 3 | Choose what to compare | `aqmen:model` | `model`, `method-competition` |
| 4 | Fill the grid | `aqmen:research` | `research`, `datasets`, `sql` |
| 5 | Archetypes and the check | `aqmen:challenge` | `challenge`, `critics`, `method-competition`, `charts` |
| 6 | The so-what, as findings | `aqmen:conclude` | `conclude`, `docs` |
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
stage whose checks fail. The deck is the hand-over. New figures: `refresh`.
Inside a due diligence, `due-diligence` picks up from the check.
