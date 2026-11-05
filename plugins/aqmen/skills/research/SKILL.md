---
name: research
description: 'Find the data a project needs and load it into the Aqmen workspace as cited datasets — official statistics first, then analysts and databases, then filings, news last — every document stored as a source and cited at the page. Use for "what data exists for X", "find the drivers", "research this market / these companies / these players", "get me the numbers for…", "load these files", or after aqmen:scope. Fans out parallel read-only aqmen:researcher agents, then hands the accepted packets to aqmen:data-loader, one loader at a time.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Research — every figure a cited dataset

The method lives on the platform, not in this skill:
`read_instructions` with topics `["research"]` (with `start` and
`rules` if not read this session), then the units it names as you reach
them, and follow it. Inside a playbook, the playbook's stage and gate
decide when it is done; on its own, the practice's Check and Then.

## What Claude adds

- **The scoping scan, in parallel.** The practice's four missions are four
  researchers: spawn two to four `aqmen:researcher` agents in one message,
  `mission: scoping-scan`, one focus each (`top-down-estimates`,
  `segmentation-conventions`, `driver-data-landscape`, `players-and-filings`
  when companies are in scope), each with the workspace and project ids and
  the scope doc's decision, questions and frame verbatim. Synthesise their
  packets into the summary the practice asks for.
- **Value packages, in parallel.** Once the grain is agreed, one
  `aqmen:researcher` per disjoint package, all in one message, `mission: value-package`,
  with the drivers, grain, periods, unit, ids and the scope's frame
  verbatim. Read the packets yourself before anything loads: drop what does
  not fit the scope; each `not_found` is a gap.
- **Load through one `aqmen:data-loader` at a time per workspace** (two only
  when their datasets are independent, said in both prompts): `mode: preview`
  with the ids, the workstream's collection id, the scope's frame verbatim
  and the accepted tables (the packets' JSON, filtered) or the client's
  files; show the user its preview; then `mode: load` with the preview's
  working directory and the approved tables. It writes each dataset's notes
  in the artifact shape; the project's notes and the scope doc stay yours.

## Then

Offer `aqmen:model` — or, inside a playbook, go on to its next stage.
