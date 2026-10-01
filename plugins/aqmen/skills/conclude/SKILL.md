---
name: conclude
description: 'Turn a finished aqmen model into conclusions — one insight per claim on the chart or spreadsheet that shows it, and a view per question for the people who read the work. Use for "what does it say", "so what", "what are the takeaways", "answer the questions", "build the view / the dashboard", or after aqmen:challenge. Step 5 of the aqmen project flow; aqmen''s deliverable skills write it up.'
---

# Conclude — claims with receipts

The brief asked questions. This step answers each one on the platform,
where the answer stays wired to the numbers behind it: when the data
changes, the answer is flagged instead of silently wrong.

Read `references/practice.md` once per session. Then read the MCP topics
`insights`, `visualization` and `views` before the first write.

## 1. Collect the questions

`describe_workspace`. The brief's **Questions** list is the agenda. The
current insights (`list_insights`) may already answer some; do not
re-derive a rejected claim.

## 2. One insight per claim

For each question, find the figure that answers it and the chart that
shows it. If no chart shows it yet, `create_chart` with the exact SQL or
spreadsheet range that computes it, then `show_chart`.

`record_insight` on the parent that visibly shows the claim:

- a **chart** normally;
- the **spreadsheet** for a model's result (a market size, a margin);
- a **dataset** only for what its rows show (a coverage caveat);
- a **view** for what the page as a whole shows;
- the **workspace** only when no single artifact can.

The title is the whole claim with its figure, in one sentence: "The
addressable market reaches $7.5B by 2029, growing 11% a year". The body
is one or two sentences of method or caveat, including the confidence of
the drivers it rests on when any is below 4. One claim per insight.

## 3. A view per question

`create_view` for each question or a small group of them: the headline
figure, the chart that proves it, the caveat, the source line. It is what
the deal team and the client read, so write it for them: plain titles,
figures as they read in a deck, no identifiers. File views in the
project's collection.

## 4. Update the brief

Mark each question in the brief answered, naming its insight, or "cannot
say", with the reason. Use `edit_docs` with find and replace on the
workspace. Append a line to the Log.

## Gate

Every question from the brief has an insight, or a stated "cannot say"
the user has seen. Then offer a deliverable: **aqmen:cdd-output** for the
full CDD set, the report or deck skill for one framework (for example
**aqmen:market-sizing-report**), **aqmen:bp-assessment** for a management
plan, or the views themselves shared with the client.
