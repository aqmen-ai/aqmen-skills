---
name: demo-prep
description: 'Turn a concluded aqmen workspace into a run-of-show for a live demo or readout — for each question in the brief, the figure to say, the saved chart or view to open, and the fallback if it fails — written as demo_script.md. Use for "prepare the demo", "run-of-show", "what do I open in the meeting", "rehearse the readout", "script the walkthrough", or after aqmen:conclude. Optional step after aqmen:conclude in the aqmen project flow.'
---

# Demo prep — every answer one click away

A demo is the workspace answering the brief's questions in front of the
reader. It goes wrong when a figure on screen disagrees with the one just
said, or when someone types fresh SQL and waits. This step fixes, before the
meeting, what is said and what is opened for each question.

Read `references/practice.md` once per session.

**The rule: answer from saved charts and views, never fresh SQL during a
demo.** A saved chart has its query checked, its insight recorded and its
staleness tracked; a live query has none of these.

## 1. Check nothing is stale

`describe_workspace` and `list_insights`. If any dataset, chart, view or
insight is stale or broken, stop: run **aqmen:refresh** first. Every answer
the script points at must be a validated insight on a fresh parent. An
unanswered question in the brief (`Q<n> [open]`) goes back to
**aqmen:conclude**, or into the script as "cannot say yet", in those words.

## 2. Map each question to what is opened

Take the brief's questions in order (`Q<n> [answered → <insightId>]`). For
each:

- **Say:** the insight's title, the figure as it reads in a deck.
- **Open:** the saved chart that is the insight's parent (`show_chart` with
  its id), or the view that answers the question (`read_view` with its id).
  `list_charts` and `list_views` to find them; open each once now to check
  it renders and shows the figure you will say.
- **Caveat:** the insight's body, in one line, for the follow-up question.
- **Fallback:** if the chart or view fails to load, the spreadsheet range
  that holds the figure (`show_spreadsheet_range`: sheet and range), or the
  deck slide that shows it (file and slide number) when a deliverable exists.

A question with no saved chart or view gets one now, through
**aqmen:conclude**, not a query in the script.

## 3. Write demo_script.md

One file, in the order the reader will hear it:

```markdown
# <Project> — run-of-show
Workspace: <name> · checked <date>: nothing stale

## Opening (1 min)
<the bottom line, one sentence>

## Q1: <question, as in the brief>
- Say: <insight title>
- Open: chart "<chart title>" (show_chart <chartId>)
- Caveat: <insight body, one line>
- Fallback: show_spreadsheet_range <spreadsheetId> <sheet>!<range> · deck slide <n>

## Q2: …

## Likely follow-ups
- <question> → <chart or view to open>

## Close
<the decision the answers inform, and what is next>
```

Ids go in the script: it is for the presenter, not the client. Titles and
figures as they read on screen. Add likely follow-ups only where a saved
chart answers them.

## 4. Rehearse once

Walk the script top to bottom: open every chart and view it names, in
order, and check each figure on screen matches the "Say" line. Fix the
script, not the workspace, unless a figure is wrong; a wrong figure goes
back to **aqmen:refresh** or **aqmen:conclude**. Append a line to the
brief's Log.

## Gate

Nothing stale; every question in the brief has a "Say", an "Open" that
renders the figure said, and a fallback; no step in the script runs SQL.
Hand the user the path to `demo_script.md`.
