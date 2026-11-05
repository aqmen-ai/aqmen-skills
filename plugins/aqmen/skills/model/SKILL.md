---
name: model
description: 'Build the model behind a decision on the Aqmen platform — a market sizing, a company P&L and valuation, a competitive landscape or a custom driver model — as datasets adapted by transformations into an Excel-compatible spreadsheet, drawn as charts, Base first, then scenarios. Use for "build the sizing / the model / the P&L / the landscape", "model the market", "set up the driver tree", "add a scenario", or after aqmen:research. aqmen:challenge reviews it.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Model — structure first, then values, then Base

The method lives on the platform, not in this skill:
`read_instructions` with topics `["model"]` (with `start` and
`rules` if not read this session), then the units it names as you reach
them, and follow it. Inside a playbook, the playbook's stage and gate
decide when it is done; on its own, the practice's Check and Then.

## What Claude adds

- **The model critic is an agent.** At the structure gate — the feed and
  formulas exist, before any value is researched — run `aqmen:challenge`,
  which spawns `aqmen:model-critic` in a fresh context; again after
  scenarios.
- **Recipes on demand.** A topic names its recipes (the workbook recipes,
  `company-model`, `landscape`); fetch one with `read_instructions` and
  `recipe` only when you build from it.

## Then

Offer `aqmen:challenge` for the values critic once values are in — or,
inside a playbook, go on to its next stage.
