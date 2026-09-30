---
name: challenge
description: 'Adversarially review a model on the aqmen platform with two fresh-context, read-only critics — the structure critic (segmentation, decomposition, dependencies, units) and the values critic (sources, confidence, methods, triangulation, gaps). Use for "critique this", "review the model", "check the sources", "is this defensible", "audit the numbers", and as the gates of aqmen:model — structure before values are researched, values before anyone calls the model done. Step 4 of the aqmen project flow.'
---

# Challenge — the two critics

A model its builder reviewed is a model nobody reviewed. The critics read
the stored workspace cold, with no builder rationale, and their product is
a list of findings. They never write.

Read `references/practice.md` once per session, and the `modeling`
topic's section on the critics.

## Which critic, when

| Critic | When | Reads |
| --- | --- | --- |
| **aqmen:structure-critic** | After the feed and formulas exist, before values are trusted | The brief, `read_spreadsheet` column structure, the feed transformation, the charts |
| **aqmen:values-critic** | After values are in, before "done" | Datasets' sources and docs, the adapting transformations, the model's totals, a top-down reference |

Asked for "a review" with no qualifier: run the structure critic if
values are not populated yet, otherwise both, in parallel.

## Spawning

Use the Agent tool with the critic's agent type. The prompt carries
**only**:

- the workspace id and name;
- the spreadsheet id, and the collection id if the model has one;
- the scope, if the user narrowed it ("only the Nordics branch");
- the brief's decision and questions, **verbatim** from the workspace docs.

Never pass your design reasoning, your sourcing notes or what you expect
them to find. A critic that knows why you did something anchors on it.
Never run a critique inline in your own context for the same reason.

## Triage

Each critic returns findings with a severity (critical, major, minor), the
evidence, a suggested fix and whether the fix is destructive. You:

1. **Verify** each finding against the workspace before presenting it.
   Drop what does not hold, and say you dropped it.
2. **Present** the list to the user, most severe first, in plain words.
3. **Fix** what the user accepts, through **aqmen:model** or
   **aqmen:research**. Destructive fixes (deleting a segment, rewriting a
   feed, replacing a dataset) need the user's explicit yes, in either
   pacing mode. When the values critic suggests a better source, cite the
   publication itself, never "the critic".
4. **Record** what the user accepts as a known limitation: an insight on
   the spreadsheet or chart it affects, with the caveat in the body. Append
   the review to the brief's Log.

Re-run the same critic after material fixes. A clean second pass is the
evidence the fix worked.

## Gate

Every finding is resolved, or accepted by the user and recorded as an
insight with its caveat.
