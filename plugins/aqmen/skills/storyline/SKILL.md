---
name: storyline
description: 'Plan the deliverable''s storyline before the analysis — one row per slide with the action title, content, exhibit, data needed, owner and purpose (the "Dot-Dash") — as a house-styled Excel plan, and, when the aqmen workspace exists, a ghost deck in it (action titles, exhibit titles, dashed placeholders) to agree with the client and fill later. Use when the user wants to plan a deck or storyline, turn a proposal or hypotheses into slides, write a Dot-Dash, ghost deck, skeleton deck or storyboard, agree the structure of a presentation, or decide which analyses a readout needs — "plan the deck", "what slides do we need", "turn the Meridian scope into a storyline", "make the ghost deck for the SteerCo".'
---

# Storyline — the deck before the analysis

The storyline sits between the proposal and the deliverable: it turns the
hypotheses and workstreams into the exact slides the client will see,
before anyone runs an analysis. When the skeleton is agreed up front, the
work that follows is filling slides, not renegotiating them, and the agents
know exactly what to build and what data to fetch.

| Output | Use |
| --- | --- |
| `<slug> - Storyline plan.xlsx` | The plan the team works from: Plan, Storyline and Data request sheets. |
| A **ghost deck** in the aqmen workspace | The skeleton shared with the client to agree the storyline; **aqmen:deliver** later fills it with sourced exhibits. Built only when the project's workspace exists. |

## Read first

1. `references/engagement-method.md` — Answer First and the hypothesis tree:
   the storyline is that tree laid out as slides.
2. `references/plan-format.md` — the plan JSON and the column meanings.
3. `references/cdd-storyline.md` — the standard four-part CDD storyline and
   how each exhibit reaches a slide; use it whenever the engagement is a
   CDD, market study or investment case.
4. `references/deliverable-standards.md` — the voice: so-what first, facts
   vs estimates.
5. For the ghost deck: `references/practice.md`, and the platform's `decks`
   topic (`read_instructions('decks')`) before the first deck write.

`assets/example-carwash-plan.json` is a complete example.

## Steps

### 1. Take the proposal as input

The best input is the proposal from **aqmen:proposal** (its JSON or the
Word file): client questions, workstreams, hypotheses with confidence ×
importance, analyses with sources and owners, deliverables, timeline.
Failing that, a brief, call notes or a list of hypotheses. Extract the
critical question and the decision; the workstreams (sections); the
hypotheses (action titles, each asserted then proven by one or more
exhibits); the analyses and data (exhibit and data cells); the audience and
occasion (an interim SteerCo vs a final readout changes length and
appendix). Ask at most three questions if something essential is missing;
otherwise state assumptions in the hand-over.

### 2. Write the storyline before the rows

Draft the action titles first, in reading order, as one list. Read them
aloud: they must argue from the situation to the answer without the
exhibits. Then: cover, agenda, executive summary (its title is the bottom
line), on a CDD the what-you-need-to-believe slide; one divider per section; 3–8 content rows per section, the first
stating the section's answer; an appendix divider, then appendix rows
(triangulation, sanity checks, sources).

**Gate:** the user reads the title list and agrees it argues the case.

### 3. Fill the rows

For each content row: `content`, `exhibit` (by kind, and how it will reach
the slide per `cdd-storyline.md`), `exhibit_title`, `data` (long-lead items
flagged), `owner`, `purpose`, and an `image_prompt` only where an
illustration would help.

### 4. Render the plan

```
python scripts/build_plan.py plan.json ./out
```

(`pip install openpyxl` if missing.) Open the Storyline sheet and read the
titles again. Fix in the JSON and re-render rather than editing the output.

### 5. The ghost deck (when the workspace exists)

If the project already has its aqmen workspace (after **aqmen:scope**),
build the plan as a deck there, so the client agrees the storyline on the
same object the deliverable will become:

- `list_decks` first: update an existing ghost deck rather than adding a
  second one.
- `create_deck` in the project's collection, named for the deliverable
  (`<project>_readout`), one `addSlide` per row, in the platform's house
  look (`decks`):
  - **cover, agenda, dividers, executive summary** as the house look lays
    them out, the executive summary's bullets as the section answers;
  - **content slides**: the action title as the title, the exhibit title,
    and in the exhibit's box a **dashed rectangle named `placeholder`**
    whose text describes the exhibit (what it plots, how it will be
    sourced); the purpose as the takeaway; the eyebrow and the source line
    left as "Source: to come";
  - **notes** on every slide: content, purpose, data, owner, the plan row
    number.
- No figures: the titles are hypotheses until the data is in. A number in
  a title is a hypothesis marked as such ("~€1bn?").
- Fix the lint; `show_deck` it; `annotate_deck` with a description saying
  it is the ghost deck, agreed on <date>.

Without a workspace, the Excel plan is the hand-over; the ghost deck is
built when the workspace exists (**aqmen:scope** reads the plan).

### 6. Hand over

The storyline in ten lines (the section answers), the number of rows,
which exhibits depend on long-lead data, what you assumed, and the ghost
deck's link if built. Point the consultant to the Data request sheet as the
first message to the client.

## Where the skill stops

It plans; it does not run the analysis or fill the deck. The data column
is the research agenda (**aqmen:research** loads it as cited datasets). The
proposal comes from **aqmen:proposal**; the filled deck from
**aqmen:deliver**, which replaces each placeholder with its sourced
exhibit.
