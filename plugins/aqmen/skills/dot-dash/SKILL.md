---
name: dot-dash
description: Build the presentation plan ("Dot-Dash") for a consulting deliverable from a scope, brief or set of hypotheses — one row per slide with the action title, content, exhibit, data needed, owner, purpose and an image-generation prompt — rendered as a house-styled Excel plan plus a skeleton PowerPoint deck to agree the storyline with the client before any analysis is built. Use this whenever the user wants to plan a deck or storyline, turn a scope into slides, write a Dot-Dash, ghost deck, skeleton deck or storyboard, agree the structure of a presentation with a client, or decide which analyses to run for a readout — including phrasings like "plan the deck", "what slides do we need", "turn the Meridian scope into a storyline", "make the ghost deck for the SteerCo".
---

# Aqmen Dot-Dash

The Dot-Dash sits between the scope and the deliverable: it turns the
hypotheses and workstreams of a scope into the exact slides the client will
see, before anyone runs an analysis. Two outputs from one plan:

| Output | Use |
| --- | --- |
| `<slug> - Dot-Dash.xlsx` | The plan the team works from: Dot-Dash sheet, Storyline sheet, Data request sheet. |
| `<slug> - Skeleton deck.pptx` | The ghost deck shared with the client to agree the storyline; the team then populates it. |

Why it matters: when the skeleton is agreed up front, the work that follows is
filling slides, not renegotiating them. It also tells the agents and analysts
exactly what to build and what data to fetch, and the image prompts let a
first visual version be produced immediately.

## Read first

1. `references/engagement-method.md` — Answer First and the hypothesis tree:
   the Dot-Dash is that tree laid out as slides.
2. `references/dotdash-format.md` — the plan JSON and the column meanings.
3. `references/cdd-storyline.md` — the standard four-part storyline and which
   exhibit kind carries each topic; use it whenever the engagement is a CDD,
   market study or investment case.
4. `references/report-standards.md` — voice: so-what first, facts vs estimates.

`assets/example-carwash-dotdash.json` is a complete example (derived from the
cdd-output car-wash content).

## Workflow

### 1. Take the scope as input

The best input is the scope produced by `aqmen-scope` (its JSON or the Word
file): client questions, workstreams, hypotheses with confidence × importance,
analyses with sources and owners, deliverables, timeline. Failing that, a
brief, call notes or a list of hypotheses. Extract:

- the **critical question** and the decision it informs,
- the **workstreams** (they become sections),
- the **hypotheses** (they become action titles: each hypothesis is asserted,
  then proven by one or more exhibits),
- the **analyses and data** already listed (they become exhibit and data
  cells),
- the **audience and occasion** (interim SteerCo vs final readout changes the
  length and the appendix).

Ask at most three questions if something essential is missing; otherwise state
assumptions in the handover.

### 2. Write the storyline before the rows

Draft the action titles first, in reading order, as one list. Read them aloud:
they must argue from the situation to the answer without the exhibits. Fix the
order and the wording until they do. Then:

- open with cover, agenda, executive summary (its title is the bottom line);
- one divider per section (workstream or storyline part);
- 3–8 content rows per section; the first row of a section states the
  section's answer, the rest prove it;
- an `appendix` divider, then `content` rows (section Appendix) for
  triangulation, sanity checks, sources.

Rule of thumb: 25–35 rows for a demo or interim readout, 40–55 for a full CDD.

### 3. Fill the rows

For each content row: `content` (what it says), `exhibit` (the analysis by kind
and what it plots, from `cdd-storyline.md` where it applies), `exhibit_title`,
`data` (with long-lead items flagged), `owner` (consultant / analyst / engineer
/ agent / client), `purpose` (the so-what), and an `image_prompt` where an
illustration would help (a scene, a process, a metaphor); leave it empty where
a chart carries the slide. The prompt is the deliverable, not the image: keep
it concrete (subject, flat style, navy/blue palette, no text in the image).

### 4. Render and check

```
python scripts/build_dotdash.py plan.json ./out
```

Open the Storyline sheet and read the titles again; open the skeleton deck and
flick through: every slide should tell the client what they will see there.
Fix in the JSON and re-render rather than editing the outputs.

### 5. Hand over

Tell the consultant: the storyline in ten lines (the section answers), the
number of rows, which exhibits depend on long-lead data, and what you assumed.
Point them to the Data request sheet as the first message to the client. When
the analysis is done, the plan maps one-to-one onto a `cdd-output` content
file (row → section), so the deliverable inherits the agreed storyline.

## Where the skill stops

It plans; it does not run the analysis or build the final deck. The
"data needed" column is the research agenda: `aqmen:research` loads it into
the project's workspace as cited datasets. The scope
comes from `aqmen-scope`; the finished deliverable set from `cdd-output`.
