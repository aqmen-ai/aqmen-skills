# Aqmen for Claude

Aqmen is where analytical work done with AI lives: datasets that cite their sources, models in spreadsheets, charts, docs and decks, all saved in a workspace and wired to what they read. This plugin connects Claude to Aqmen and adds skills for the jobs consultants and analysts run there.

## What it contains

- **The Aqmen connector** (`.mcp.json`): Aqmen's remote MCP server at `https://platform.aqmen.ai/api/mcp`. You sign in with your own Aqmen account (OAuth); no key is stored in the plugin.
- **Skills** (`skills/`): one per job — market sizing, company analysis, competitive landscape, due diligence, proposal, refresh — and one per stage of the work — scope, research, model, challenge, conclude, deliver, close. Each skill tells Claude to read Aqmen's own method for that job (`read_instructions`) and follow it.
- **Agents** (`agents/`): a researcher, a data loader, a view builder, and fresh-context critics (model, values, deck) and a skeptic, used by the skills to work in parallel and to review before anything is approved.

## What it runs and sends

Nothing runs locally: no hooks, no scripts, no local servers. The only network destination is Aqmen's MCP server above, reached through Claude's connector with your sign-in. What Claude sends there is what you ask it to build or read in your Aqmen workspace. See Aqmen's privacy policy at https://aqmen.ai/privacy.

## Getting started

1. Install the plugin and connect Aqmen when Claude asks you to sign in (create an account at https://aqmen.ai if you have none).
2. Ask, for example: "Size the market for HR software in Europe", "Benchmark the players in EV charging", or "Draft a proposal from these call notes".

Docs: https://aqmen.ai/docs · Support: https://aqmen.ai/support
