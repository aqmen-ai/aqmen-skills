---
name: proposal
description: Write an aqmen engagement proposal (scope / statement of work) as an editable Word document in the house style — an analysis engagement (commercial due diligence, market or business-plan assessment, AI diligence, strategy diagnostic), a build engagement (a data product, model or query layer for a client) or an internal sprint. Use this whenever a consultant wants to scope, propose, pitch, price or plan a client project from call notes, a transcript, an email or a brief — including phrasings like "draft the proposal for X", "turn these notes into a scope", "what would we offer them", "put together the SoW", "plan the engagement", or when they paste a client's questions and ask how Aqmen would answer them. Produces workstreams with rated hypotheses, analyses with sources and owners (incl. AI agents), deliverables, a dated cadence, a week-by-week workplan, a data request, team and commercials, then renders a .docx via the bundled script.
---

# Proposal — the engagement scope

Turn a consultant's brief into a client-ready **scope document** (`.docx`) that
also works as the project plan: the client can sign it, and the team, human or
agent, can start work from it on Monday.

The output follows the aqmen brand (Montserrat, the navy/blue/azure palette, A4,
wordmark, header/footer — all carried by `assets/scope-template.docx`)
and the structure of Aqmen's best past proposals. The consultant edits the Word
file afterwards, so optimise for a strong first draft rather than for finality.

## Read first

1. `references/engagement-method.md` — how Aqmen runs work (Answer First,
   80/20 ratings, backwards planning). The scope encodes this method; without it
   you will write a brochure.
2. `references/scope-structure.md` — the section-by-section spec for the
   three engagement types, and the quality gate.
3. `references/aqmen-boilerplate.md` — company facts, people, standard
   differentiators and commercial clauses. Adapt, never paste unchanged.
4. `references/scope-best-practice.md` — what wins, what fails. Short.
5. `references/spec-format.md` — the JSON the renderer takes, with block types.
6. `references/deliverable-standards.md` — only its **Voice** section
   applies here (decision-grade, so-what first, facts vs estimates). The
   sources-and-confidence machinery is for analysis deliverables, not
   proposals.

Three complete specs to pattern-match against: `assets/example-meridian.json`
(analysis engagement, CDD), `assets/example-build.json` (build engagement,
data pipeline with gates) and `assets/example-internal.json` (internal sprint,
no commercials).

## Workflow

### 1. Intake: extract before you ask

The consultant will give you something imperfect: call notes, a Plaud
transcript, an email thread, a paragraph. Read it all and pull out:

- **Client and counterpart** (fund / company, who asked, who decides)
- **The decision at stake** and why now (transaction, board date, budget cycle)
- **The questions asked**, in the client's words: these become workstreams
- **Timing and budget signals** (deadline, "a few weeks", a number mentioned)
- **What data exists** (VDR, sell-side pack, systems, prior Aqmen work)
- **Relationship history** (introduced by whom, prior engagement)

Then decide the **engagement type**: analysis (a question to answer), build (an
asset to deliver), or internal (a sprint for Aqmen itself: no Commercials
section, no client data-request table). If genuinely unclear, ask; it changes
half the document.

Ask the consultant only what you cannot infer, in **one batch of at most five
questions**, and say what you will assume if they don't answer. Typical gaps:
start date, fee expectation, who from Aqmen is on it, whether interviews are in
scope, project codename. Do not run a long interview; a strong draft with stated
assumptions is more useful than a questionnaire.

### 2. Structure the problem

For an analysis engagement, build the tree before writing prose:

- Critical question → one **workstream per client question** (3–5).
- Per workstream, 2–3 **hypotheses as assertions** a sceptic could dispute. Rate
  each **confidence (L/M/H) × importance (L/M/H)**. Low confidence + high
  importance is where the work starts and where the effort goes.
- Per hypothesis, the **analyses** that test it. Tag each with a **source type**
  (off-the-shelf documents, public data, paid reports, client data, interviews,
  survey, scraping) and an **owner** (consultant, analyst, engineer, agent,
  client). Interviews, surveys and client data are long-lead: they start week 1.
- Per workstream, the **outputs** the client sees.

For a build engagement, structure by **phases with gates**: what each phase
delivers, the standard of success at its gate, the decision (if any) taken at a
gate, what the client owns at handover and what is explicitly not included.

Sanity-check the whole against the timing: workstreams × analyses × owners must
fit the weeks and the team. If they don't, cut scope or extend time, and say so.

### 3. Draft the spec

Write `scope.json` following `references/scope-structure.md` (sections and
what goes in each) and `references/spec-format.md` (block types). Content rules
that matter most:

- **Client-centric, so-what first.** "Ares will be able to…", not "we will
  leverage…". Lead bullets with a bold phrase that carries the point.
- **Hypotheses are assertions**, not tasks. "Meridian's pricing is sustainable
  under the pressure building in the market", not "assess pricing".
- **Dates are real.** Name the start Monday, every touchpoint's day, the final
  session. The week-by-week grid spans the same weeks.
- **The data request is part of the scope.** What we need from the client, by
  when. Every long-lead item appears there. An internal scope has none; name
  dependencies on other teams in the workplan instead.
- **Fees: logic always, number only if given.** Leave `£[XX]k` otherwise. The
  consultant sets the figure case by case. An internal scope omits section 6;
  the renderer prints only the sections in the spec.
- **Boilerplate is adapted**, mentioning the client's situation in each block.
- **Length:** 6–8 pages (internal: 2–4). Cut before you pad.

### 4. Quality gate

Run the checklist at the end of `references/scope-structure.md` against the
spec. Fix, don't annotate. In particular: every client question maps to a
workstream; every hypothesis is rated and disputable; every deliverable traces
back; no empty items; one project name throughout.

### 5. Render and hand over

```
python scripts/build_scope.py scope.json "Aqmen - <Project> <Type> Proposal vDRAFT.docx"
```

(`pip install python-docx` if missing.) The renderer already keeps table
headers with their first row and boxes on one page. If you want a visual check
and Word is installed, this one-liner exports a PDF (kill any lingering
`WINWORD` process first if it hangs):

```powershell
$w = New-Object -ComObject Word.Application; $d = $w.Documents.Open("<abs path>.docx", $false, $true); $d.SaveAs2([ref]"<abs path>.pdf", [ref]17); $d.Close($false); $w.Quit()
```

Then rasterise with PyMuPDF (`fitz`) and look at the pages. Skip this if the
environment can't run Word; a 3,500–4,000-word spec renders to 8–10 pages,
which is the upper end of the target, so trim before you render again.

Tell the consultant in a few lines: the engagement type you chose, the
assumptions you made (dates, team, interviews), the hypotheses you are least
sure of, and what they must fill in (fee, names). Offer the `.json` alongside
the `.docx` so a second pass can be regenerated rather than re-edited.

## Where the skill stops

It writes the proposal. It does not price the work (case by case), does not
send anything, and does not produce the presentation plan (that is
**aqmen:storyline**, which reads the proposal as its input). Once the work
starts, **aqmen:scope** turns the agreed proposal into the brief of the
project's aqmen workspace — the client's questions, the workstreams, the
rated hypotheses and the data request — where every later step reads them;
for a CDD, **aqmen:cdd** runs the work from there.
