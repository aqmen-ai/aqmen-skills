---
name: research
description: 'Find the data a strategic-decision project needs and load it into the aqmen workspace as cited datasets — official statistics first, then analysts and databases, then filings, news last. Use for "what data exists for X", "find the drivers", "research this market / these companies / these players", "get me the numbers for…", or after aqmen:scope. Fans out parallel read-only aqmen:researcher agents, then hands the accepted packets to aqmen:data-loader, one loader at a time. A shared step (after aqmen:scope, before aqmen:model) that use cases such as aqmen:cdd drive.'
---

# Research — every driver a cited dataset

The model is only as defensible as its inputs. This step finds them,
loads each one **as published** with its citation, and names every gap
honestly, so the model step never waits on data and never makes it up.

Read `references/practice.md` once per session. Then read the MCP topics
`datasets` (how files are cleaned, uploaded and cited), `modeling` (the
data section: drivers are datasets, groupings are data, time is a column)
and the framework's topic, which says what shape its data takes: drivers
at their published grain for a sizing, reported figures as `line_item,
fiscal_year, value` for a company, field datasets with `source_url` and
`confidence` columns for a landscape.

## 1. Read the brief

`describe_workspace`. The brief in the workspace docs names the questions,
the frame and the framework. If there is no brief, run **aqmen:scope**
first. Research without questions has no stopping rule.

## 2. Scoping scan, in parallel

Before any model structure exists, spawn two to four **aqmen:researcher**
agents in one message, each with a disjoint focus and the brief verbatim:

- `top-down-estimates`: published totals and growth rates for this market
  or company, each with its exact scope. They become the triangulation
  reference later.
- `segmentation-conventions`: how analysts and statistics offices cut
  this subject, and whether differentiated data exists per segment.
- `driver-data-landscape`: for the drivers the framework will plausibly
  need, the best source per driver and the granularity it publishes at.
- `players-and-filings` (company analysis, competitive landscape): the
  long list of companies, what each discloses, and where.

Synthesise their packets into a short summary for the user. Say what
exists, at which breakdowns, and where the gaps are. The trade-off between
granularity and evidence is the user's; it shapes the model step.

## 3. Value packages, in parallel

Once the model's grain is agreed (aqmen:model, dependencies), partition
the drivers still missing into work packages, weighted by how much each
moves the answer, disjoint so no two researchers chase the same figure.
Spawn one **aqmen:researcher** per package, all in one message, with
mission `value-package`, the drivers, the grain, the periods, the unit, the
workspace id and the brief verbatim. Each returns a **load-ready packet**:
tables as CSV-shaped rows with column names, units and scale, one citation
per document, a confidence, and what it could not find.

Read the packets yourself before anything loads: drop a table whose scope
does not fit the brief, and note each `not_found` as a gap. Show the user
what was found, per driver, with its source and confidence, and the gaps.

## 4. Load, one loader at a time

Loading is delegated to **aqmen:data-loader**, which extracts, checks and
loads mechanically by the `datasets` topic: unique keys, units and scale,
coordinates inside the country, histories that are not current attributes,
the CSV contract, then upload, `create_dataset` with sources,
`annotate_dataset`, filing in the collection.

1. **Preview.** Spawn one data loader with `mode: preview`, the workspace
   and collection ids, the brief's frame verbatim, and the accepted tables
   (the packets' JSON verbatim, filtered) or the client's files with what
   each is. It writes nothing and returns, per table, the header and first
   rows as they will load, the checks, the sources and the proposed name
   and semantics.
2. **Show the user** the preview (step-by-step mode: wait). This is where
   a mis-read table, a wrong scale or a refused check is caught. A replace
   of an existing dataset is destructive: it needs the user's yes.
3. **Load.** Continue the same loader (or spawn one) with `mode: load`, its
   preview's working directory, the approved tables and any corrections.
   It returns what landed (names, rows, columns, warnings — a duplicate-row
   warning is a failure to fix, not a footnote) and what it refused and why.
4. **Verify** with `describe_workspace` that what it reports exists.

**Serialize loaders**: one per workspace at a time. Run two in parallel
only when their datasets are independent (different names, no append to a
common target), and say so in each prompt.

A grouping (country to region, company to tier) is a dataset too, cited.
A researcher's estimate enters only as an estimate: its docs say what was
searched, why nothing was found, and the confidence (at most 2).

## 5. The sources register

Append each dataset the loader reports (its `sources_register`) to the
brief's **Sources register** with `edit_docs` on the workspace: the
dataset, the publisher, the year, the confidence. The brief is yours, not
the loader's.
Append a line to the **Log**.

## Gate

Every driver the model needs has a dataset, or a named gap the user has
seen. Show the register, then offer **aqmen:model**.
