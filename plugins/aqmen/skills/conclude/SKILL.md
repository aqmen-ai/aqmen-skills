---
name: conclude
description: 'Turn a finished aqmen model into conclusions — one insight per claim on the chart or spreadsheet that shows it, validated once the user approves it so a deck can head a slide with it, a view per question built by background aqmen:view-builder agents in parallel, and (on a CDD by default) the aqmen:skeptic playing the investment committee against the conclusions. Use for "what does it say", "so what", "what are the takeaways", "answer the questions", "build the views / the dashboard", or after aqmen:challenge. A shared step; aqmen:deliver presents the conclusions as a deck.'
---

# Conclude — claims with receipts

The brief asked questions. This step answers each one on the platform,
where the answer stays wired to the numbers behind it: when the data
changes, the answer is flagged instead of silently wrong. The insights it
records are the claims the deliverable makes — a deck heads its slides with
them by source.

Read `references/practice.md` once per session. Then read the MCP topics
`insights` and `charts` before the first write (the view builders read
`views` themselves).

**Views explore; decks present.** A view is a live page for the team and
the client to explore an answer while the work moves. The finished story
the user presents is a deck, built by **aqmen:deliver** from the insights
and charts this step leaves behind.

## 1. Collect the questions

`describe_workspace`. The brief's **Questions** list is the agenda: one
line per question, `Q<n> [open]: …`. The current insights (`list_insights`)
may already answer some; do not re-derive a rejected claim.

## 2. One insight per claim

For each question, find the figure that answers it and the artifact that
shows it. If no chart shows it yet, save one (`charts`) — and since the
deck will put it on a slide, choose a type a slide can draw where the
story allows (the `decks` topic lists them). `show_chart` it.

`record_insight` on the parent that visibly shows the claim — a chart
normally; the spreadsheet for a model's result; a dataset only for what its
rows show; a view for what the page as a whole shows; the workspace only
when no single artifact can (the `insights` topic is the rule).

The title is the whole claim with its figure, in one sentence, written as
a slide headline: "The addressable market reaches $7.5B by 2029, growing
11% a year". The body is one or two sentences of method or caveat,
including the confidence of the drivers it rests on when any is below 4,
and the `Believe` rows it rests on, with their verdicts ("rests on
adoption ≥ 30% — demanding"; `modeling`: what you need to believe). One
claim per insight.

## 3. Views, in the background, in parallel

Views are independent entities, so each is built by its own
**aqmen:view-builder**. As soon as a question has its insight and the
charts that show it (§2), spawn its builder **in the background**
(`run_in_background`) and go on recording the next question's insights;
spawn the rest the same way. One builder per view; a small group of
questions may share a view.

Each builder's prompt is its spec, and nothing else it needs to guess:

- the workspace id and the collection id (and `viewId` to fix an existing
  one);
- the question, verbatim, and the audience (the deal team, the client);
- the insights that answer it (ids, titles, bodies), the saved charts by
  `name`, the spreadsheet ranges (summary blocks), the datasets;
- the figures that must appear, as they read;
- filters and interactions, the layout (headline, exhibit, caveat, source
  line), the view's title.

Builders cannot ask the user anything; if this session would prompt for
their writes, run them in the foreground instead. **Collect every result**
before the gate: the view's url, what it shows, the figures it checked,
and any figure it could not source — that goes back to §2 (save the chart)
and the builder is re-run in fix mode with the `viewId`. Check
`list_views` shows each one fresh.

A builder drafts from the insights you give it; if the insight is later
rejected or retitled, re-run its builder with the `viewId`.

## 4. Validate what holds, after the skeptic

A deck sources only **validated** insights. Before validating:

- The values critic has passed (**aqmen:challenge**).
- **On a CDD, the skeptic** (`aqmen:skeptic`, by default; on request for
  other use cases) has played the investment committee against the
  claims, through **aqmen:challenge**: the workspace id, the brief
  verbatim, the scope (all conclusions), the use case — never your
  reasoning. Its critical challenges are settled (new evidence, a new
  analysis) or carried as a caveat in the insight's body, which the deck
  will show as a risk. Its "hardest questions" list is kept for
  **aqmen:demo-prep**.
- **The user has approved each claim, explicitly.** Show the claims as a
  list — each title with its figure, the artifact it sits on, the critics'
  and the skeptic's caveats — and ask which hold. Seeing them is not
  approving them: a validated insight can head a slide, so validation is
  the user's call, never yours. A claim resting on an `implausible` row
  is validated only when the user explicitly accepts that row, named —
  record the acceptance in the body.

Then validate exactly the claims the user approved (`update_insight`, per
the `insights` topic). Reject the ones the user rejects, with a body saying
why — they stay as negative knowledge. A claim the user has not answered
on stays open. A view headed by a claim that changed gets its builder
re-run.

## 5. Update the brief

Mark each question on its own line with `edit_docs` find and replace on
the workspace: find that question's exact `Q<n> [open]` and replace the
status only.

- Answered: `Q2 [open]` → `Q2 [answered → <insightId>]`.
- Not answerable: `Q2 [open]` → `Q2 [cannot say: <reason>]`.

Never rewrite the question text or the list. Append a line to the Log.

## Gate

Every question from the brief has an insight the user approved and you
validated, or a "cannot say" the user has agreed to; every view builder has reported and its view is
fresh; on a CDD, the skeptic's critical challenges are settled or carried
as caveats. Then offer **aqmen:deliver** for the deck (and
optionally the HTML report), or the views themselves shared with the
client. When the answers will be shown live, offer **aqmen:demo-prep**.
