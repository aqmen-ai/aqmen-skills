---
name: challenge
description: 'Adversarially review work on the Aqmen platform with fresh-context, read-only critic agents — the model critic (structure, formulas, scenarios), the values critic (sources, confidence, triangulation), the skeptic (the investment committee against the conclusions) and the deck critic (the deliverable and its sourcing). Use for "critique this", "review the model", "check the sources", "is this defensible", "audit the numbers", "what will the IC ask", "stress-test the conclusions", "audit the deck", and at the critic gates of every playbook.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Challenge — running the critics

The method lives on the platform, not in this skill:
`read_instructions` with topics `["challenge"]` (with `start` and
`rules` if not read this session), then the units it names as you reach
them, and follow it. Inside a playbook, the playbook's stage and gate
decide when it is done; on its own, the practice's Check and Then.

## What Claude adds

- **Spawn, never self-review.** Each critic is an agent —
  `aqmen:model-critic`, `aqmen:values-critic`, `aqmen:skeptic`,
  `aqmen:deck-critic` — started with the Agent tool in a fresh context. The
  marked self-review in the practice is for clients that cannot spawn; never
  critique inline.
- **The prompt carries only** the workspace and project ids; the spreadsheet
  id and its workstream's collection id; for the deck critic the deck id and
  version, the audience and the storyline it must follow; for the skeptic
  the findings doc id, the use case and the scope; the user's narrowed
  scope, if any; and the scope doc's decision, questions and frame and the
  hypotheses from the project's notes, verbatim. Never your reasoning, the
  notes' Decisions, sourcing notes or what you expect them to find.
- **Independent critics run together** — model and values in one message —
  never one after reading another's report.
- **Recheck** after material fixes: the same agent with `mode: recheck` and
  its own accepted findings, verbatim and filtered — nothing about how they
  were fixed. Each answers per id in its report's recheck block.

## Then

Triage as the practice says, then back to the stage whose gate it was.
