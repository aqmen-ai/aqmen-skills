---
name: conclude
description: 'Turn a finished Aqmen model into conclusions — the project''s findings doc, one section per question with the answer as a headline sentence and every figure a sourced block, approved by the user claim by claim; the plan doc and the brief kept current (questions answered, hypotheses supported or refuted with the figure that decides them); a view per question built by background aqmen:view-builder agents in parallel; and (on a CDD by default) the aqmen:skeptic playing the investment committee against the findings. Use for "what does it say", "so what", "what are the takeaways", "answer the questions", "write up the findings", "build the views / the dashboard", or after aqmen:challenge. A shared step; aqmen:deliver presents the findings as a deck or a memo.'
---

# Conclude — claims with receipts

The brief asked questions. This step answers each one in the project's
**findings doc**, where every figure is a sourced block wired to the chart,
cell or dataset it comes from: when the data changes, the doc says which
figures went stale instead of silently showing an old number. The findings
are the claims the deliverable makes — the deck's headlines and the memo
are written from them.

Read `references/practice.md` once per session. Then read the MCP topics
`docs` and `charts` before the first write (the view builders read `views`
themselves).

**Views explore; docs record; decks and memos present.** A view is a live
page to explore an answer while the work moves. The findings doc is the
record of what the work concluded. The finished story the user presents is
a deck or a memo, built by **aqmen:deliver** from the findings and charts
this step leaves behind.

## 1. Collect the questions

`describe_workspace` with the `projectId`. The brief's **Questions** list
is the agenda: one line per question, `Q<n> [open]: …`. `read_doc` the plan
(`as: "markdown"`) for each question's hypotheses. `list_docs` in the
project: if a findings doc exists, update it — never a second one; do not
re-derive a claim its Log or the brief's Log records as dropped.

## 2. One finding per question

For each question, find the figure that answers it and the artifact that
shows it. If no chart shows it yet, save one (`charts`) with the
`projectId` and the `collectionId` of the question's workstream — choosing a type a slide can draw where the
story allows (the `decks` topic lists them) — and `show_chart` it. A model
result is a spreadsheet cell or a summary-block range; a published value a
dataset value.

Write the finding:

- **The headline** — the whole claim with its figure, in one sentence,
  written as a slide headline: "The addressable market reaches $7.5B by
  2029, growing 11% a year". The figure is a sourced `figure` block, the
  sentence around it its `before` and `after`.
- **The exhibit** — the `chart` (or `range`) that shows it, by source,
  with a caption.
- **Method and caveat** — one or two sentences in plain words: how the
  figure was built (no SQL, no table names), the confidence of the drivers
  it rests on when any is below 4, and the `Believe` rows it rests on, with
  their verdicts ("rests on adoption ≥ 30% — demanding"; `modeling`: what
  you need to believe).

One claim per finding; a question may need two or three.

## 3. Write the findings doc

`create_doc` in the project (`projectId`, the Deliverables collection's
`collectionId` from the brief's Collections), named
`findings`, displayName "<project> — findings", with `markdown` for the
skeleton and `ops` inserting the sourced blocks (the `docs` topic is the
contract):

- `# <Project> — findings`, then the bottom line so far in one paragraph.
- Per question, `## Q<n> — <question>`: a `callout` (`warning`) "Draft —
  not yet approved", the headline `figure` block, the exhibit, the method
  and caveat paragraph; a `callout` for a skeptic risk carried as a caveat.
- `## Sources and confidence` at the end: per load-bearing figure, the
  publisher, the document and year and where in it (the dataset's
  citation — `get_dataset`), the confidence, the method in words. Check
  each against the stored page (`read_source` at its `where`) before the
  finding goes to the user for approval: the page must state the figure
  at the scope the finding claims.

Every number from the workspace goes in by source, never typed. `read_doc`
after each write: every sourced block reads **fresh**. `annotate` (entityType `doc`) with
a one-line description. Record the doc in the brief's **Docs** section
(`edit_notes`, entityType `project`).

## 4. Views, in the background, in parallel

Views are independent entities, so each is built by its own
**aqmen:view-builder**. As soon as a question has its finding and the
charts that show it (§2–3), spawn its builder **in the background**
(`run_in_background`) and go on to the next question; spawn the rest the
same way. One builder per view; a small group of questions may share a
view.

Each builder's prompt is its spec, and nothing else it needs to guess:

- the workspace and project ids, the collection id of the question's
  workstream (and `viewId` to fix an existing one);
- the question, verbatim, and the audience (the deal team, the client);
- the finding that answers it (headline, method and caveat, as written in
  the findings doc), the saved charts by `name`, the spreadsheet ranges
  (summary blocks), the datasets;
- the figures that must appear, as they read;
- filters and interactions, the layout (headline, exhibit, caveat, source
  line), the view's title.

Builders cannot ask the user anything; if this session would prompt for
their writes, run them in the foreground instead. **Collect every result**
before the gate: the view's url, what it shows, the figures it checked,
and any figure it could not source — that goes back to §2 (save the chart)
and the builder is re-run in fix mode with the `viewId`. Check
`list_views` shows each one fresh. A finding later reworded or dropped
re-runs its view's builder.

## 5. Approve what holds, after the skeptic

The deliverable states only **approved** findings. Before approving:

- The values critic has passed (**aqmen:challenge**).
- **On a CDD, the skeptic** (`aqmen:skeptic`, by default; on request for
  other use cases) has played the investment committee against the
  findings doc, through **aqmen:challenge**: the workspace, project and
  findings doc ids, the brief verbatim, the scope (all conclusions), the
  use case — never your reasoning. Its critical challenges are settled (new
  evidence, a new analysis) or carried as a caveat callout under the
  finding, which the deck will show as a risk. Its "hardest questions" list
  is kept for **aqmen:demo-prep**.
- **The user has approved each claim, explicitly.** Show the findings as a
  list — each headline with its figure, the artifact it rests on, the
  critics' and the skeptic's caveats — and ask which hold. Seeing them is
  not approving them: an approved finding heads a slide, so approval is the
  user's call, never yours. A claim resting on an `implausible` row is
  approved only when the user explicitly accepts that row, named — say so
  in its caveat.

Then, in one `update_doc`: delete the "Draft" callout of each finding the
user approved; delete each finding the user rejects and record it, with
why, in the brief's Log — negative knowledge the next session must not
re-derive. A finding the user has not answered on keeps its callout.

## 6. Update the brief and the plan

- **The brief.** Mark each question on its own line with `edit_notes`
  (entityType `project`) find and replace: find that question's exact
  `Q<n> [open]` and replace the status only — `Q2 [answered]`, or
  `Q2 [cannot say: <reason>]`. Never rewrite the question text or the list.
- **The plan.** `read_doc` the plan, then one `update_doc`: each question
  marked answered or "cannot say"; each hypothesis marked **supported**,
  **refuted** or **partly supported**, with the figure that decides it as a
  sourced `figure` block under it ("Refuted: the segment grows "
  + figure + " a year, below the 8% the hypothesis needed"). Plain words, no
  SQL.

Append a line to the brief's Log.

**Tidy.** `describe_workspace` on the project: the root is empty; file
any chart or view left there into its workstream's collection
(`move_to_collection`).

## Gate

Every question from the brief has an approved finding in the findings doc,
or a "cannot say" the user has agreed to; `read_doc` shows no stale or
broken source in the findings doc or the plan; the plan's hypotheses each
carry their verdict; every view builder has reported and its view is
fresh; on a CDD, the skeptic's critical challenges are settled or carried
as caveats. Then offer **aqmen:deliver** for the deck or the memo, or the
views themselves shared with the client. When the answers will be shown
live, offer **aqmen:demo-prep**.
