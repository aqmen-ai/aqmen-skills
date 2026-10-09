---
name: demo-prep
description: 'Turn a concluded aqmen workspace into a run-of-show for a live demo or readout — for each question in the brief, the figure to say, the saved chart, view or deck slide to open, and the fallback if it fails — written as demo_script.md. Use for "prepare the demo", "run-of-show", "what do I open in the meeting", "rehearse the readout", "script the walkthrough", or after aqmen:deliver. An optional shared step.'
---

# Demo prep — every answer one click away

A demo is the workspace answering the brief's questions in front of the
reader. It goes wrong when a figure on screen disagrees with the one just
said, or when someone types fresh SQL and waits. This step fixes, before
the meeting, what is said and what is opened for each question.

Read `references/practice.md` once per session.

**The rule: answer from saved charts, views and the deck, never fresh SQL
during a demo.** A saved figure has its query checked, its insight recorded
and its staleness tracked; a live query has none of these.

## 1. Check nothing is stale

`describe_workspace`, `list_insights` and `list_decks`. If any dataset,
chart, view, insight or deck figure is stale or broken, stop: run
**aqmen:refresh** first. Every answer the script points at must be a
validated insight on a fresh parent. An unanswered question in the brief
(`Q<n> [open]`) goes back to **aqmen:conclude**, or into the script as
"cannot say yet", in those words.

## 2. Choose the mode

- **Present the deck**: the readout runs from the deck's page in aqmen
  (**Present** shows it full screen from the selected slide; arrows move,
  Escape leaves), with the charts and views as drill-downs.
- **Walk the workspace**: the readout runs from charts and views, the deck
  as backup.

Ask the user which, or propose the deck when one exists and the audience is
the client.

## 3. Map each question to what is opened

Take the brief's questions in order (`Q<n> [answered → <insightId>]`). For
each:

- **Say:** the insight's title, the figure as it reads in the deck.
- **Open:** the deck slide that answers it (in Present mode, or
  `show_deck` with that slide), or the saved chart that is the insight's
  parent (`show_chart`), or the view that answers the question
  (`read_view`). `list_charts`, `list_views` and `read_deck` to find them;
  open each once now to check it renders and shows the figure you will say.
- **Caveat:** the insight's body, in one line, for the follow-up question.
- **Fallback:** if the first choice fails to load, `show_deck` on the
  slide that shows it, or the spreadsheet range that holds the figure
  (`show_spreadsheet_range`: sheet and range).

A question with no saved figure gets one now, through **aqmen:conclude**,
not a query in the script. A view that is broken, or does not show the
figure you will say, gets an **aqmen:view-builder** in fix mode (its
`viewId`, the question, the insight, the charts, the figure that must
appear) — several in parallel, in the background, while you script the
rest; open each again once it reports.

## 4. Write demo_script.md

One file, in the order the reader will hear it:

```markdown
# <Project> — run-of-show
Workspace: <name> · deck: <deck name> v<version> · checked <date>: nothing stale
Mode: present the deck | walk the workspace

## Opening (1 min)
<the bottom line, one sentence>

## Q1: <question, as in the brief>
- Say: <insight title>
- Open: deck slide <n> "<slide title>" · or chart "<chart title>" (show_chart <chartId>)
- Caveat: <insight body, one line>
- Fallback: show_deck <deckId> slide <slideId> · show_spreadsheet_range <spreadsheetId> <sheet>!<range>

## Q2: …

## Likely follow-ups
- <question> → <chart, view or backup slide to open>

## The IC's hardest questions (from the skeptic)
- <question> → <where the answer lives> · or "open: <what is missing>"

## What you need to believe
- <assumption>: <value> — <verdict> vs <reference>; breaks at <break-even> → open: the WYNTB slide · show_spreadsheet_range <spreadsheetId> Believe!<range>

## Close
<the decision the answers inform, and what is next>
```

Ids go in the script: it is for the presenter, not the client. Titles and
figures as they read on screen. Add likely follow-ups only where a saved
figure answers them (a hidden backup slide is a good home). On a CDD, the
skeptic's `ic_questions` from **aqmen:conclude** are the follow-ups to
prepare first; if it did not run, offer it (**aqmen:challenge**) — each
question it raises needs an answer to open, or an honest "open". The
`Believe` rows (`modeling`: what you need to believe) are the prepared
answers to "what do I have to believe?": one line each, the `demanding` and
`implausible` ones first, with how far each can move before the answer
flips.

## 5. Rehearse once

Walk the script top to bottom: open every slide, chart and view it names,
in order, and check each figure on screen matches the "Say" line. Fix the
script, not the workspace, unless a figure is wrong; a wrong figure goes
back to **aqmen:refresh** or **aqmen:conclude**. Append a line to the
brief's Log.

## Gate

Nothing stale, deck figures included; every question in the brief has a
"Say", an "Open" that renders the figure said, and a fallback; no step in
the script runs SQL. Hand the user the path to `demo_script.md`.
