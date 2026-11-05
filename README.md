# Aqmen

A Claude plugin for strategic-decision work on the [Aqmen platform](https://try.aqmen.ai):
the **Aqmen MCP connector** plus **thin skills** for what only Claude can do
on top of it.

**The method lives on the platform.** How to size a market, analyse a
company, map the competition or run a due diligence — the playbooks, the
practices of each stage, the four critic checklists, the deliverable
standards — is served by the connector to any agent, Claude or not:
`read_instructions` with topics `["start", "rules"]`, then the playbook, then
each stage's units as it gets there. An agent with the connector alone does
the same work through the same gates, running each critic as a marked
self-review.

**What the plugin adds over the connector alone:**

- **Skills that trigger on the job** ("size the market for X", "we're
  running a CDD on Y") and **chain the stage skills** with the Skill tool,
  keeping the plan doc current so any session resumes from the project.
- **Researchers in parallel** — scoping scans and value packages as
  read-only agents, one data loader at a time.
- **Fresh-context critics** — the model, values, deck and skeptic critics as
  agents that see only the ids and the brief, never the builder's
  reasoning, with a recheck mode.
- **View builders in the background**, one per view.
- **Local builders**: Aqmen's house-styled Word proposal and the storyline
  plan in Excel (`proposal`), the HTML report template (`deliver`).

## Install

```
/plugin marketplace add aqmen-ai/aqmen-skills
/plugin install aqmen@aqmen-skills
```

In the desktop app: **Customize → Plugins → Add marketplace** (`aqmen-ai/aqmen-skills`),
then install. On first use you'll be prompted to sign in to Aqmen (OAuth). Updates
ship via git: `/plugin marketplace update aqmen-skills`.

The connector points at `https://platform.aqmen.ai/api/mcp`. Any other assistant
with MCP support can connect to the same URL and read the same method.

_(Local dev: `claude --plugin-dir ./plugins/aqmen` from the repo root.)_

## Skills

### Jobs — one per playbook

Each reads `read_instructions(['start', 'rules', '<job>'])` and follows the
playbook stage by stage, invoking the stage's skill.

| Skill | Use it when |
| --- | --- |
| `aqmen:market-sizing` | "Size the market for X", "build a TAM/SAM/SOM", "is the market the plan assumes really there" |
| `aqmen:company-analysis` | "Analyse X", "build the P&L", "does the management plan hold up", "value this company" |
| `aqmen:competitive-landscape` | "Benchmark the players in X", "who competes with Y", "how does X compare with its peers" |
| `aqmen:due-diligence` | "We're running a CDD on X", "is there an opportunity in Y" — the three analyses as workstreams of one project, reconciled into one deck (replaces `aqmen:cdd`) |
| `aqmen:proposal` | "Draft the proposal", "turn these notes into a scope", "plan the deck", "make the ghost deck" (absorbs `aqmen:storyline`) |
| `aqmen:refresh` | "New data arrived", "roll it forward a year", "update the deck" |

### Practices — one per stage

Each reads `read_instructions(['<practice>'])` and adds the Claude-only moves.

| Skill | What Claude adds |
| --- | --- |
| `aqmen:scope` | Reads a proposal or plan left on disk by `aqmen:proposal` |
| `aqmen:research` | Researchers in parallel; one data loader at a time, preview then load |
| `aqmen:model` | The model critic as an agent at the structure gate |
| `aqmen:challenge` | The four critics spawned fresh, together, with recheck |
| `aqmen:conclude` | The skeptic before approval; view builders in the background |
| `aqmen:deliver` | The deck critic before hand-over; the HTML report template |

### Agents

| Agent | Kind | Writes | Method read from |
| --- | --- | --- | --- |
| `researcher` | Build, parallel | Nothing — returns load-ready packets | `research` |
| `data-loader` | Build, one at a time | Sources and datasets only | `datasets`, `research` |
| `view-builder` | Build, background | One view only | `views` |
| `model-critic` | Critique | Nothing | `critics` → the model critic |
| `values-critic` | Critique | Nothing | `critics` → the values critic |
| `skeptic` | Critique | Nothing | `critics` → the skeptic |
| `deck-critic` | Critique | Nothing | `critics` → the deck critic |

Each agent file keeps only its Claude-only shell: its role, what its
prompt carries (ids and the brief, verbatim), the tools it may call, its
report format and its recheck mode. Its checklist is the platform's.

## Generated skills — do not edit by hand

The twelve job and practice `SKILL.md` files are **generated** from the
platform's playbook registry and practices (`aqmen-data-workspace`,
`packages/content/src/skills.ts`); each carries a header saying so. To
change one, change the definition there and regenerate from the platform
repo:

```
pnpm skills:generate                # writes ../../aqmen-skills/plugins/aqmen
pnpm skills:generate <plugin-dir>   # or another checkout
pnpm skills:generate --check        # exit 1 if any is out of date
```

Only the `SKILL.md` files are written; the agents are hand-kept. Nothing
is built locally: everything a skill makes — docs, decks, pages, the
storyline as a ghost deck, the HTML report — is made in Aqmen.

## Repo layout

```
.claude-plugin/marketplace.json   # marketplace (aqmen-skills) → ./plugins/aqmen
plugins/aqmen/
  .claude-plugin/plugin.json      # the plugin (name: "aqmen")
  .mcp.json                       # Aqmen connector (https://platform.aqmen.ai/api/mcp)
  agents/                         # researcher, data-loader, view-builder;
                                  #   model-critic, values-critic, skeptic, deck-critic
  skills/
    market-sizing/ company-analysis/ competitive-landscape/
    due-diligence/ proposal/ refresh/          # jobs (generated SKILL.md)
    scope/ research/ model/
    challenge/ conclude/ deliver/              # practices (generated SKILL.md)
```

## HTML reports

An HTML report is a page in the project. Its house shell and guide live on
the platform (`read_instructions` with `recipe: "report"` and
`"report-shell"`); to change the look or bump the pinned ECharts build,
change the shell there.

## Validate

```
claude plugin validate .                # the marketplace
claude plugin validate ./plugins/aqmen  # the plugin
```

## Changes

**3.0.0** — thin skills; the method moves to the platform.

- **One source.** The playbooks, practices, critic checklists, research
  missions and deliverable standards are the platform's
  (`read_instructions`), readable by any agent. The skills keep only what
  Claude adds; `shared/`, `sync-shared.mjs` and its 18 copies are gone.
- **Skills by job:** `market-sizing`, `company-analysis`,
  `competitive-landscape`, `due-diligence` (was `cdd`), `proposal` (absorbs
  `storyline`), `refresh` — each chaining `scope`, `research`, `model`,
  `challenge`, `conclude`, `deliver`. Generated from the platform, so they
  cannot drift.
- **Agents keep their shells:** prompt contract, tools, report format,
  recheck; their checklists point at `critics`, `research`, `datasets`,
  `views`.
- Older installs keep working: the platform still answers the old topic
  and prompt names (`workflow`, `size_a_market` …).

**2.5.0** — annotate, one-call orientation. **2.3.0** — sources are items:
store what you read, cite the page. **2.2.0** — collections organize every
project. **2.1.0** — projects, notes and docs.
