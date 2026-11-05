---
name: proposal
description: 'Write an engagement proposal (scope / statement of work) and plan its storyline before the work, on the Aqmen platform — the client''s questions as workstreams, rated hypotheses, analyses and data, deliverables, a dated workplan, then a ghost deck. Use whenever a consultant wants to scope, propose, pitch or plan a client project from call notes, a transcript, an email or a brief: "draft the proposal for X", "turn these notes into a scope", "what would we offer them", "put together the SoW", "plan the engagement", "plan the deck", "what slides do we need", "make the ghost deck".'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Write the proposal — the `proposal` playbook

The method lives on the platform, not in this skill. First,
`read_instructions` with topics `["start", "rules", "proposal"]`,
and follow the playbook stage by stage: read each stage's units as you
reach it (up to six topics per call), never from memory of a topic not
read this session.

## Stages and the skill each chains

| # | Stage | Skill | Reads |
| --- | --- | --- | --- |
| 1 | Read the brief | `aqmen:scope` | `scope`, `projects`, `collections` |
| 2 | Structure the problem | `aqmen:scope` | `scope`, `research` |
| 3 | Write the proposal | — | `docs` |
| 4 | Check it | — | `standards`, `docs` |
| 5 | Plan the storyline | — | `standards`, `decks` |

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
stage whose checks fail. When the client signs, the job's playbook — usually
`due-diligence` — starts in this project: the proposal seeds the scope doc,
the hypotheses stay in the notes, the ghost deck is the deck its last stage
fills.
