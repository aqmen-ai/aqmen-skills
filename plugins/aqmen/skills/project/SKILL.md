---
name: project
description: 'Run a whole strategic-decision project on the aqmen platform end to end — scope, research, model, challenge, conclude, deliver — with the user''s confirmation between steps. Use when the user hands over a brief or asks for the whole thing — "run the CDD on X", "do the market sizing for Y end to end", "take this from the question to the deck", "go from zero to a deliverable". Orchestrates the aqmen step skills; each step''s gate must hold before the next begins.'
---

# Project — the whole flow

A strategic-decision project runs in steps, and each ends at a gate. This
skill runs them in order, holds each gate, and keeps the user in the loop
at the moments their judgement matters.

Read `references/practice.md` once per session. Tell the user once, early,
that they can say "go autonomous".

## The steps

| # | Skill | Ends when |
| --- | --- | --- |
| 1 | **aqmen:scope** | The user confirms the brief: the decision, the questions, the deliverable |
| 2 | **aqmen:research** (scoping scan) | The user has seen what data exists and where the gaps are |
| 3 | **aqmen:model** (structure) | The structure is proposed and confirmed |
| 4 | **aqmen:challenge** (structure critic) | Findings resolved or accepted |
| 5 | **aqmen:research** (value packages) and **aqmen:model** (values) | Every driver has a cited dataset or a named gap; the model evaluates clean |
| 6 | **aqmen:challenge** (values critic) | Findings resolved or accepted |
| 7 | The user validates Base | An explicit yes, before any scenario |
| 8 | **aqmen:conclude** | Every question has an insight or a stated "cannot say" |
| 9 | The deliverable: **aqmen:cdd-output** for the full CDD set, a framework's report or deck skill, **aqmen:bp-assessment** for a management plan | A deliverable whose every number traces to the workspace |
| 10 | Optional: **aqmen:demo-prep**, when the answers are shown live | A run-of-show where every question opens a saved chart or view |

Before step 1, the engagement may already have a proposal from
**aqmen:aqmen-scope** and a slide plan from **aqmen:dot-dash**. The scope step
reads both, and the slide plan's data column becomes the research agenda.

Invoke each step skill with the Skill tool when you reach it, and follow
its instructions in full. Do not paraphrase a step from memory.

## Rules across the steps

- **Resume, don't restart.** At the start, and whenever you come back to
  the project, read `describe_workspace` and the brief's Log. Pick up at
  the first gate that does not hold.
- **One writer.** Researchers and critics run in parallel and only read.
  You apply every write, one at a time.
- **The gates are not skippable,** in either pacing mode. Autonomous mode
  removes the pauses between steps, never the gates, the critics, the
  Base validation or the confirmation of destructive changes.
- **Keep the Log.** Every step appends one dated line to the brief: what
  was done and what is left. It is how the next session, or a colleague,
  knows where the project stands.
- **Report at each gate** in a few plain sentences: what exists now, what
  it says so far, and what is next.
