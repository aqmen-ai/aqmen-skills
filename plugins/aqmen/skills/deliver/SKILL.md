---
name: deliver
description: 'Build the deliverable of an Aqmen project from the approved findings — a deck exported to PowerPoint and/or a memo as a doc exported to Word — every figure added by source, nothing stale, checked by the deck critic; optionally an HTML report read from the deck, stored as a page in the project. Use for "build the deck", "make the slides / the readout / the presentation", "write the memo / the report", "write it up", "export to PowerPoint / Word", "an HTML version", or after aqmen:conclude.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Deliver — the deck, every figure from the work

The method lives on the platform, not in this skill:
`read_instructions` with topics `["deliver"]` (with `start` and
`rules` if not read this session), then the units it names as you reach
them, and follow it. Inside a playbook, the playbook's stage and gate
decide when it is done; on its own, the practice's Check and Then.

## What Claude adds

- **The deck critic is an agent.** Before a client-facing deck is shown or
  exported, spawn `aqmen:deck-critic` fresh through `aqmen:challenge`'s
  contract (the deck id and version, the findings doc id, the audience, the
  storyline, the scope doc's questions verbatim). Apply its accepted ops
  yourself against the current version, then recheck.

## Then

The hand-over, as the practice says. When the data moves, `aqmen:refresh`.
