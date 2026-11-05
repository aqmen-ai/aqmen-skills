---
name: conclude
description: 'Turn a validated Aqmen model into conclusions — the project''s findings doc, one claim per question with its figure as a sourced block, challenged by the skeptic and approved by the user claim by claim; the questions'' statuses and the hypotheses'' verdicts in the project''s notes; a view per question. Use for "what does it say", "so what", "what are the takeaways", "answer the questions", "write up the findings", "build the views / the dashboard", or after aqmen:challenge. aqmen:deliver presents the findings.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Conclude — the findings, approved claim by claim

The method lives on the platform, not in this skill:
`read_instructions` with topics `["conclude"]` (with `start` and
`rules` if not read this session), then the units it names as you reach
them, and follow it. Inside a playbook, the playbook's stage and gate
decide when it is done; on its own, the practice's Check and Then.

## What Claude adds

- **The skeptic before approval.** Once the findings are drafted — by
  default on a due diligence, on request otherwise — spawn `aqmen:skeptic`
  fresh, through `aqmen:challenge`'s contract, on the findings doc. Settle
  or carry its critical challenges before the user approves.
- **Views in the background.** When the user will explore, one
  `aqmen:view-builder` per question, all in one message with
  `run_in_background`: the workspace and project ids, the question's
  workstream collection id, the question verbatim, the finding as drafted,
  the charts by name, the figures that must appear. Go on writing while they
  build; read each back when it reports.

## Then

Offer `aqmen:deliver` for the deck or the memo — or, inside a playbook, go
on to its next stage.
