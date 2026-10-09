# How Aqmen runs an engagement

The scope is the first artefact of a method, not a standalone sales document.
Everything in it (workstreams, hypotheses, cadence, workplan) exists so the team
can run the project the way described here. Write the scope so that a consultant
or an AI agent could start work from it on day one without a briefing.

This is the method Miguel brought from McKinsey and Bain, condensed. The same
file is synced into the proposal and storyline skills.

## 1. Answer First: start from the client's action, not from the analysis

Every engagement exists because someone has to **decide or act**. Frame the work
backwards from that:

1. **Situation** — the relevant background, in two or three sentences.
2. **Complication** — what changed, or what is at stake, that prompts the question now.
3. **Critical question** — the one question the client needs answered. If there
   are several, they become the workstreams.
4. **Hypothesis** — the answer we expect, stated as an assertion the client could
   disagree with. "Market growth supports the plan" is a hypothesis; "assess market
   growth" is a task.
5. **Primary and secondary assertions** — what would have to be true for the
   hypothesis to hold. These are the leaves of the tree, and each leaf maps to an
   analysis.

Five questions to build the tree (Bain's Answer First workplanning):
- What is the hypothesis for client action?
- What do we need to convince them of?
- What analysis is required?
- What data do we need?
- Why is this difficult, and what biases or competing hypotheses will resist it?

A test for a good hypothesis: **if the assertion is not strong enough to elicit an
opposing view, it is not doing any work.** Rewrite it until a sceptical reader
could say "I don't think that's true".

## 2. 80/20: rate every assertion on confidence × importance

Before planning, rate each hypothesis on two axes:

| | Importance for the answer: **high** | **medium/low** |
| --- | --- | --- |
| **Confidence low** | Start here, week 1. Most analytical effort. | Cheap check, park if it doesn't move. |
| **Confidence high** | Confirm quickly with one analysis, then move on. | Assert and footnote. |

This is why the scope carries the ratings: they sequence the workplan (low
confidence + high importance goes first), they size the effort, and they tell an
agent where to spend its budget. They also signal candour to the client: we are
saying openly which parts of our own answer we trust least.

Working rule: build a quick back-of-envelope version first, sense-check it against
market, competitors and management's own numbers, then deepen only where the
answer could still change. "Do it quickly, do it badly, share it."

## 3. Workstreams: one per client question or decision

A workstream has:
- a **question** it answers (usually one of the client's own),
- its **hypotheses** with ratings,
- the **analyses** that test them, each with a **source type** and an **owner**,
- its **outputs** (what the client sees), and
- **dependencies** on other workstreams.

Source types matter because they drive effort and lead time:

| Source type | Typical lead time | Who does it |
| --- | --- | --- |
| Off-the-shelf documents (VDR, filings, sell-side pack) | Immediate | Agent, reviewed by analyst |
| Public and statistical data (ONS, Eurostat, regulators) | Days | Agent |
| Paid reports and databases | Days; needs client approval | Analyst |
| Client data (systems extracts, internal reporting) | 1–2 weeks; needs a data request | Client + analyst |
| Expert / customer interviews | 2–3 weeks incl. recruitment | Analyst or partner network |
| Survey | 3–4 weeks | Analyst + panel provider |
| Web scraping / bespoke data build | Days to weeks | Engineer |

Anything in the bottom four rows is a **long-lead item**: it must be started in
week 1 and flagged in the workplan and in the data request.

Owners are `consultant`, `analyst`, `engineer`, `agent`, or `client`. The AI
agent is a real owner: name the analyses it will run so the team can hand them
off on day one.

## 4. The manufacturing process: plan backwards from each client meeting

Every major client meeting is prepared in a fixed sequence. When the scope lists
a Friday findings session, the internal calendar behind it is:

| Step | When | What exists |
| --- | --- | --- |
| Answer First | Start of the sprint | Storyline with blanks; workplan of analyses and activities |
| Update 1 | ~50% content | Logic and exec-summary check; input on the major analyses |
| Update 2 | ~75% content | Exec summary fine-tuned; input on one or two key topics |
| Pre-wire | 1–2 days before | Key client sees the storyline; no surprises in the room |
| Finalise | 95% | Final slide selection, back-ups ready |
| Brief | Just before | 5Rs: Roadmap, Results, Room, Roles, Risks |
| Meeting | | |
| Debrief | Immediately after | 5Rs: Reconvene, Reset, Review, Refine, Recap; next steps |

In the scope this shows up as: (a) the touchpoint table lists the client
sessions, and (b) the week-by-week workplan places the internal milestones
before each one. A consultant reading the scope should be able to put the whole
calendar in a diary.

## 5. Manager and client updates: 30 / 3 / 30

Updates come in three sizes: a 30-second elevator update (has the answer changed;
what roadblocks), a 3-minute shortened update (answer, where input is needed,
next steps) and a 30-minute full update. The full update structure:

1. Objectives for this meeting
2. This was the question you asked me
3. This is the answer
4. Here are my roadblocks and where I need your help
5. Elaborate on key points; only what is relevant; supporting data separate
6. These are my next steps

Use the same structure for the interim client checkpoints in the scope and for
the emails that go with them.

## 6. Data requests: get it right first time

- Confirm we do not already have the data.
- Name the source (system or person) and the client owner.
- Provide a template and a date; be specific about grain, period and format.
- Check in after sending; verify irregularities on receipt.

The scope's **What we need from the client** list is the first data request.
Every long-lead item in the workplan must appear there with a date.

## 7. New-task checklist (for every analysis in the workplan)

What exactly is the analysis; drop-dead date and internal deadlines; critical path
and dependencies; inputs and lead time; why it matters and what deliverable it
feeds. If an analysis in the scope cannot answer these, it is not yet a task.

## 8. Executive summary rule

The final document opens with the answer, built from the assertions, framed as
what the client should do differently. Short, insight- and action-focused. Do not
summarise process; do not add "interesting" context. This is why the scope ends
each hypothesis with "verdict, with the evidence": the exec summary is already
designed.
