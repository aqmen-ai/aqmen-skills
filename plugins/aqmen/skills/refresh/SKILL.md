---
name: refresh
description: 'Bring an existing Aqmen project up to date when the data moves — new figures, a new period, a corrected source — and re-check every finding, doc block, deck figure and page that depended on it. Use for "update the model", "new data arrived", "refresh with the latest figures", "roll it forward a year", "the source was revised", "update the deck", "update the memo", or when describe_workspace, list_docs or list_decks shows stale items. Follows the platform''s refresh playbook.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Update with new data — the `refresh` playbook

The method lives on the platform, not in this skill. First,
`read_instructions` with topics `["start", "rules", "refresh"]`,
and follow the playbook stage by stage: read each stage's units as you
reach it (up to six topics per call), never from memory of a topic not
read this session.

## Stages and the skill each chains

| # | Stage | Skill | Reads |
| --- | --- | --- | --- |
| 1 | See what moved | — | `projects`, `datasets` |
| 2 | Update the data | `aqmen:research` | `research`, `datasets` |
| 3 | Rerun the chain | — | `sql`, `spreadsheets`, `charts` |
| 4 | Re-check the findings | `aqmen:conclude` | `conclude`, `challenge`, `docs` |
| 5 | Bring the deliverables with it | `aqmen:deliver` | `deliver`, `decks`, `docs`, `pages` |

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
- **Broken views in the background.** One `aqmen:view-builder` per broken
  view, in fix mode (its `viewId`, the workstream's collection id, the
  question, the finding, the charts, the figures that must appear), all in
  one message with `run_in_background`; collect them before the findings
  gate.

## Resuming

`describe_workspace` with the project: its notes, Status first, say where
the work stands; then read the notes of what you touch. Pick up at the first
stage whose checks fail. The project is current. The next change starts here
again.
