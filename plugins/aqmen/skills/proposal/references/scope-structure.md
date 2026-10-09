# Scope structure: section by section

Three engagement types share one skeleton. Decide the type first, from the intake:

- **Analysis engagement** — a question to answer (CDD, market entry, business-plan
  assessment, AI diligence, strategy diagnostic). Hypothesis-led. Exemplar:
  Project Meridian (`assets/example-meridian.json`).
- **Build engagement** — an asset to deliver (a data product, a matching
  pipeline, a model, a query layer). Phase- and gate-led. Exemplar:
  `assets/example-build.json` (IBMG product-data mapping, "Project One Code"),
  which follows the pattern of the IBMG Oracle proposal summarised below.
- **Internal engagement** — an internal sprint (a demo, a reusable asset, a
  capability build) with no client paying for it. Analysis- or build-shaped
  as fits, but it **omits section 6 (Commercials)** and the **What we need
  from [client]** table in section 4; dependencies on other teams go in the
  workplan paragraph. Header right and confidentiality read "Internal".
  Exemplar: `assets/example-internal.json` (Project Lighthouse, a two-week
  demo sprint). Aim at 2–4 pages.

In a build engagement the hypotheses box still appears, once, at the top of
section 2 under a label such as **What we believe going in**: 3–4 rated
assertions about the asset (e.g. "most records match from part numbers alone").
It tells the client where the risk sits and what the pilot phase tests.

Both aim at **6–8 pages**. A short scope that a partner reads in ten minutes beats
a long one nobody finishes.

---

## Cover

Kicker (who it is for), project name, one-line promise, a two-line summary
(duration, what kind of work, the questions or the asset), confidentiality line,
month and year, company footer lines. The summary is the sentence the client
forwards internally, so it must say what they get, not what we do.

## 1 · Context and objectives  (Situation → Complication)

- One paragraph on how we got here (prior relationship, who introduced whom, what
  the client asked for).
- One bold-led paragraph on the situation: the company, the transaction or
  decision, the headline numbers.
- **Label: The decision [client] faces** — three bullets: what they must underwrite
  or decide; why the existing evidence is not enough; the time pressure.
- **Label: What [client] asked us to address** — a `callout` with their questions
  in their words (these become the workstreams).
- **Label: What makes Aqmen different** — four bullets from the boilerplate, each
  tied to this engagement. For a build engagement, replace with **What the asset
  is** (what it does, how it works in layers, what data sits inside) and **Why it
  matters** (verbatims from the client's own people, one quantified example).

## 2 · Our approach  (Resolution)

Title it with the structure: "four workstreams, one per question" or "three
monthly stages".

**Analysis engagement — per workstream:**
1. `workstream` title: "Workstream N: <question, phrased as a topic>".
2. `hypotheses` box: 2–3 assertions, each rated confidence × importance, restarting
   at H1. State what a sceptic would dispute; avoid task-like phrasing.
3. `subheading` **Approach** — 3–5 bold-led bullets, each an analysis: what it
   is and how it is done (method, comparison set, scenario logic).
4. `subheading` **Data and sources** — two bullets: off the shelf (what we already
   have or can pull immediately) and to be produced (interviews, surveys, paid
   reports, client data), with long-lead items flagged. Name the owner where it
   is not obvious (agent / analyst / client).
5. `subheading` **Outputs** — what the client sees from this workstream, ending
   with "Verdict on each hypothesis, with the evidence."

Open the section with two short paragraphs: the sources the whole engagement
draws on, and the sentence that every hypothesis will be reported with a verdict
(validated / partially validated / challenged).

**Build engagement — instead of workstreams:**
- **Project scope** — where it is built (client estate vs Aqmen-hosted), what the
  client owns and maintains at handover, and an explicit **What this phase does
  not include** paragraph.
- **Key decision gate** — if the architecture or scope is settled mid-engagement,
  describe the decision, who takes it, the options (e.g. a three-column
  Accept / Work around / Supplement table) and what each option means for the
  client after handover.
- **The N-week engagement** — a `columns` block, one column per phase, with the
  gate at the foot of each.
- **Ownership transition** — named roles, documentation, training.

## 3 · Deliverables

A two-column `table` (Deliverable | Description). Each row is something the
client can tick off; the description says what it contains and its state at
handover. Follow with **Label: Out of scope** (2–4 bullets) and, where relevant,
**Label: Why interactive models, not a static report** (boilerplate, adapted).

For build engagements: one table per phase ("Month 1 — Scope, validate…"), plus
**Retained by Aqmen** (methods and skill patterns; client has unrestricted
internal use), **External data: what ownership means**, and **What [client]
provides**.

## 4 · Workplan and cadence

Three parts, so the scope doubles as the project plan:

1. A paragraph naming the start date, the weekly rhythm (e.g. interim check
   Wednesdays, findings Fridays) and the sentence that each findings session is
   prepared backwards (storyline → 75% → pre-wire). See `engagement-method.md` §4.
2. `table` **When | Session | Content** — every client touchpoint with a real
   date, its duration where fixed, who attends, and what is shown. The last row
   is the final session with a hands-on walkthrough of the deliverables.
3. **Label: Week by week** — a `gantt` block: one row per workstream (owner
   under the name), one column per week, milestones row for gates and client
   sessions. This is the picture the client reads first, so it must agree with
   the touchpoint table to the day. Follow it with a short `table` or bullets
   only where a cell needs words (e.g. which analyses run in week 1, which
   items are long-lead). Long-lead items start in week 1.
4. **Label: What we need from [client]** (not in an internal engagement) —
   the first data request, as a
   three-column `table` (Item | Owner | By; widths `[5511, 2200, 1700]`), or
   bullets when there are only two or three items. Include VDR access,
   introductions, approvals for paid data, and the client time you are asking
   for (e.g. "two days a week from David and Lee").

For a build engagement the week-by-week grid becomes phases × workstreams
(data, semantic layer, access, analyses, users).

## 5 · Team and ways of working

`table` **Person | Role on [project]** — 3–4 rows: engagement lead, technical
lead, analyst/engineering capacity. Roles argued for fit ("led the recent
operational diagnostic for IBMG"), not biographies; the biographies live in the
boilerplate for a build engagement that needs the credentials. Then two bullets:
single working channel and named counterpart; confidentiality perimeter.

## 6 · Commercials

Omitted in an internal engagement; the document ends at section 5.

**Label: Professional fees** → `callout`: the fee model in one bold line (fixed
fee for the programme: £[XX]k; or N equal instalments released at gates), then
pass-through costs, VAT, expenses cap. The number is filled by the consultant
case by case; the logic is always written. Gate-based: state that the client may
stop at any gate and how overruns are treated.

**Label: Why Aqmen** — three short bold-led bullets (team, creators run the
analysis, proven with [most relevant reference]). For a build engagement add
**Beyond the engagement** (what is available as separately scoped work) and a
`signature` block.

## Closing line

The company footer line from the boilerplate.

---

## Quality gate (run before rendering)

- Every client question in the callout maps to a workstream; every workstream
  has ≥2 hypotheses, ≥3 analyses, sources, and outputs.
- Every hypothesis is an assertion a sceptic could dispute, and is rated.
- Every deliverable traces to a workstream or phase.
- Every long-lead item is in week 1 of the workplan and in the data request
  (internal: in the workplan paragraph).
- Touchpoints have real dates; the workplan spans the same weeks.
- Team × weeks is plausible against the fee, if a fee is given.
- No empty bullets, no `[brackets]` except the fee placeholder, one project name
  throughout, client-centric phrasing.
