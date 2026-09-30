---
name: research
description: 'Find the data a strategic-decision project needs and load it into the aqmen workspace as cited datasets — official statistics first, then analysts and databases, then filings, news last. Use for "what data exists for X", "find the drivers", "research this market / these companies / these players", "get me the numbers for…", or after aqmen:scope. Fans out parallel read-only aqmen:researcher agents and applies what they find as the one writer. Step 2 of the aqmen project flow; aqmen:model comes next.'
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
moves the answer. Spawn one **aqmen:researcher** per package with mission
`value-package`, the drivers, the grain, the periods and the brief.

## 4. Apply, one write at a time

You are the only writer. For each finding you accept:

1. Shape the file as published: same unit, same scale, the publisher's
   flags. The only arithmetic allowed is the one step the `datasets`
   topic permits, stated in the docs.
2. `create_upload_slot`, upload with curl, then `create_dataset` with
   `sources`: one citation per document, never "various sources". Use a
   display name a partner would read ("Enterprises by size class, EU").
3. `annotate_dataset`: column semantics (unit, scale, currency, meaning),
   and docs with the method, the confidence and the caveats.
4. `move_to_collection` into the project's collection.

A grouping (country to region, company to tier) is a dataset too, cited.
A researcher's estimate enters only as an estimate: its docs say what was
searched, why nothing was found, and the confidence (at most 2).

## 5. The sources register

Append each dataset to the brief's **Sources register** with `edit_docs`
on the workspace: the dataset, the publisher, the year, the confidence.
Append a line to the **Log**.

## Gate

Every driver the model needs has a dataset, or a named gap the user has
seen. Show the register, then offer **aqmen:model**.
