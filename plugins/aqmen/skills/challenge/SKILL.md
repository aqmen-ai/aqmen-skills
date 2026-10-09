---
name: challenge
description: 'Adversarially review work on the aqmen platform with fresh-context, read-only agents — the model critic (the chain from datasets to spreadsheet: segmentation, decomposition, dependencies, units, formulas, lint, scenarios), the values critic (sources, confidence, methods, data integrity, triangulation), the skeptic (the client''s investment committee against the conclusions) and the deck critic (the deliverable as communication and its sourcing). Use for "critique this", "review the model", "check the sources", "is this defensible", "audit the numbers", "what will the IC ask", "stress-test the conclusions", "audit the deck", and as the gates of aqmen:model, aqmen:conclude and aqmen:deliver. A shared step.'
---

# Challenge — the critics and the skeptic

A model its builder reviewed is a model nobody reviewed. The critics read
the stored workspace cold, with no builder rationale, and their product is
a list of findings with ids. They never write.

Read `references/practice.md` once per session (its **Agents** section is
the contract), and the `modeling` topic's section on the critics.

## Which agent, when

| Agent | When | Reads |
| --- | --- | --- |
| **aqmen:model-critic** | After the feed and formulas exist, before values are trusted (the gate in aqmen:model); again after scenarios | The brief, the transformations, `read_spreadsheet` column structure and lint, the scenario layer, the charts |
| **aqmen:values-critic** | After values are in, before "done" and before aqmen:deliver | Datasets' sources and docs, data integrity, the adapting transformations, the model's totals, a top-down reference |
| **aqmen:skeptic** | After values, on the conclusions — **by default on a CDD**, on request otherwise ("what will the IC ask", "red-team it") | The `Believe` block first (`modeling`: what you need to believe), then the brief, the insights and what carries them, a sensitivity, the deck if in scope |
| **aqmen:deck-critic** | A deck is built, before it is shown or exported (the gate in aqmen:deliver) | `read_deck`: the storyline, titles, so-whats, consistency, every figure's source |

Asked for "a review" with no qualifier: the model critic if values are not
populated yet; otherwise the model and values critics **in parallel** (one
message), plus the skeptic on a CDD. Asked to "check the deck": the deck
critic. Critics are independent of each other: run them together, never
one after reading the other's report.

## Spawning

Use the Agent tool with the agent's type. The prompt carries **only**:

- the workspace id and name;
- the spreadsheet id, and the collection id if the model has one;
- for the deck critic, the deck id (and version), the audience and the
  storyline standard the deck must follow (for a CDD: Context → Market →
  Competition → Company → Appendix, executive summary first);
- for the skeptic, the use case and the scope (all conclusions, a
  workstream, a deck);
- the scope, if the user narrowed it ("only the Nordics branch");
- the brief's decision, questions and hypotheses, **verbatim** from the
  workspace docs.

Never pass your design reasoning, your sourcing notes or what you expect
them to find. A critic that knows why you did something anchors on it.
Never run a critique inline in your own context for the same reason.

## Triage

Each critic returns findings with an id (`M…` model, `V…` values, `D…`
deck, `C…` skeptic), a severity (critical, major, minor), the evidence, a
suggested fix (the skeptic: what would settle it) and whether the fix is
destructive. You:

1. **Verify** each finding against the workspace before presenting it.
   Drop what does not hold, and say you dropped it.
2. **Present** the list to the user, most severe first, in plain words.
3. **Fix** what the user accepts — a missing load-bearing assumption
   becomes a `Believe` row, a contested verdict a better reference —
   through **aqmen:model**, **aqmen:research**, **aqmen:conclude** (a
   claim the skeptic breaks), or
   for a deck finding **aqmen:deliver** (the deck critic's ops are
   suggestions; you apply them, against the current version).
   Destructive fixes (deleting a segment, rewriting a feed, replacing a
   dataset, detaching a deck source) need the user's explicit yes, in
   either pacing mode. When the values critic suggests a better source, cite the
   publication itself, never "the critic". A skeptic challenge is settled
   by new evidence or analysis, or accepted as a stated risk; never by
   rewording the claim to dodge it.
4. **Record** what the user accepts as a known limitation: an insight on
   the spreadsheet or chart it affects, with the caveat in the body. Append
   the review to the brief's Log.

## Recheck

After material fixes, run the same critic again in **recheck** mode rather
than a full pass. The prompt carries the usual ids and brief, plus
`mode: recheck` and the critic's own earlier findings, verbatim, filtered
to the ids the user accepted and you fixed. The critic verifies only those,
plus anything that depends on them, and returns `rechecked: [{id, status}]`
(the skeptic: `settled`, `partly-settled` or `unsettled`; the deck critic
reads the deck's new version).

Passing the critic its own findings does not break the spawning rule: they
are its words, not your reasoning. Still pass nothing about how you fixed them.
A finding comes back `fixed` only from the workspace; anything else goes
back to triage. A full pass is still due when the fixes reshaped the model
(a new dimension, a rewritten feed).

## Gate

Every finding is resolved, or accepted by the user and recorded as an
insight with its caveat. On a CDD, every critical skeptic challenge is
settled or carried into the deck as a stated risk.
