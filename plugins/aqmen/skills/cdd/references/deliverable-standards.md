# Aqmen deliverable standards (shared)

The standard every aqmen deliverable is held to, whatever its form — a deck
or a doc in the workspace, an HTML report, a proposal or a slide plan. They
exist so the work reads as one house voice and holds up in front of an
investment committee.

> Canonical in `shared/`, synced into the skills that write deliverables.
> How a deck or a doc is built (elements and blocks, sources, the house
> look, Word export) is the platform's `decks` and `docs` topics, not this
> file.

## Voice

- **Decision-grade.** The readers are expert consultants and the people
  they advise, making real commercial-diligence calls.
- **So-what first.** Lead the deliverable, every section and every slide
  with the conclusion, then support it. A slide title is a finding with its
  number ("The SAM is €1.1bn and grows 4% a year"), never a topic ("Market
  size"). The executive summary states the answer and the decision it
  informs before any method.
- **Signal over volume.** Plain language, no filler, no process narration.
  If a sentence or a slide does not change what the reader believes, cut it.
- **Facts vs estimates, always labelled.** Observed data, modelled
  estimates and interpretation are visibly different. Assumptions and
  uncertainty are named.
- **Justified complexity.** The structure the economics require — neither a
  real model dumbed down nor complexity manufactured.
- **No implied completeness.** Gaps, sparse coverage and missing values are
  shown, not hidden behind a tidy exhibit.
- **No SQL, no code, no internal names.** Whatever the client reads — a
  doc, a deck, a report, an export — never shows SQL, code or table and
  column identifiers. The method is described in plain words ("allocated
  by each region's share of headcount"), the sources cited by publisher and
  document.

## Base first

- Present the **validated Base case** before any scenario.
- A scenario is its **hypotheses**: state each named claim in words first,
  then the numbers that change against Base. Thesis and numbers stay
  visibly separate.

## Every number traceable

- **Numbers come from the workspace.** Every figure in a deliverable is one
  the workspace computes — in a deck or a doc, added by source; in an HTML
  report, read from the deck's pinned figures or the workspace directly.
  No rounding away precision the workspace has, no figures it does not
  contain.
- **Conclusions come from the findings doc.** Headlines are the findings
  the user approved. A draft finding may be used only marked as not yet
  approved; a dropped one is never a finding; one whose figures went stale
  is re-checked first (`aqmen:refresh`).
- **A source line on every exhibit**, from the datasets the figure rests on.

## Sources and confidence (the closing section)

Every deliverable ends with **Sources and confidence**: for the figures the
conclusions lean on, the source (publisher, document, year, link), the
confidence on the platform's 1–5 scale (as the dataset's notes record it,
never re-scored here), and the method where the figure is derived
(aggregated, allocated, proxied, interpolated — in words, from the
transformation's notes).

**Watch-outs** come from the data, not from taste:

- figures resting on confidence 2 or below, on news (capped at 3), or on an
  allocation, proxy or estimate;
- gaps: questions the brief marks "cannot say", nulls, anything stale;
- the drivers that move the answer most, and whether they are the
  best-sourced.

**Overall confidence** is roughly the low end of the load-bearing figures;
name what drags it down.

## Research order

Official statistics and regulators → major analysts, databases and
industry bodies → company filings and materials → news last, capped at 3.
Each framework topic on the platform (`market-sizing`, `company-analysis`,
`competitive-landscape`) gives its own order; follow it.
