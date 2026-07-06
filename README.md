# Aqmen skills for Claude

A Claude **plugin marketplace** published by [Aqmen](https://aqmen.ai). Install
in Claude Code or Claude Desktop to get aqmen's connector and standardized
report skills for commercial due diligence.

## Install

```
/plugin marketplace add aqmen-ai/aqmen-skills
/plugin install aqmen-reports@aqmen
```

In Claude Desktop: **Customize → Plugins → Add marketplace** (`aqmen-ai/aqmen-skills`),
then install. On first use Claude prompts you to sign in to aqmen.

## Plugins

| Plugin | What it does |
| --- | --- |
| [`aqmen-reports`](./plugins/aqmen-reports) | The aqmen MCP connector + standardized output-report skills (market sizing, company analysis, competitive landscape). |

## Layout

```
.claude-plugin/marketplace.json   # this marketplace
plugins/
  aqmen-reports/                  # the plugin (see its README)
```

## Contributing

Report skills share a canonical design system and standards in
`plugins/aqmen-reports/shared/`. After editing those (or adding a skill), run:

```
node plugins/aqmen-reports/scripts/sync-shared.mjs
```

Validate before pushing:

```
claude plugin validate ./plugins/aqmen-reports
```
