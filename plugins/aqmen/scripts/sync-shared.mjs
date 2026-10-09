#!/usr/bin/env node
/**
 * Copy the canonical shared reference files from `shared/` into the
 * `references/` folder of each skill that needs them. Plugins don't reliably
 * ship files outside a skill's own directory, so a file several skills read is
 * edited once in `shared/` and synced; a file only one skill reads lives in
 * that skill alone (e.g. deliver's report style, cdd's workstream files).
 *
 *   practice.md               the working practice: topics first, pacing, the
 *                             agents, numbers by source, the brief, gates
 *   deliverable-standards.md  voice, base first, traceability, sources and
 *                             confidence — every skill that writes a deliverable
 *   cdd-storyline.md          the CDD deck storyline — the use case and the
 *                             storyline planner
 *   engagement-method.md      Answer First, ratings, backwards planning — the
 *                             pre-project skills
 *
 * How the platform works (tools, decks, the house look) is NOT here: skills
 * reference the aqmen MCP's read_instructions topics by name.
 *
 * Run from anywhere:  node plugins/aqmen/scripts/sync-shared.mjs
 */
import {
  cpSync,
  existsSync,
  mkdirSync,
  readdirSync,
  rmSync,
  statSync,
} from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const sharedDir = join(pluginRoot, "shared");
const skillsDir = join(pluginRoot, "skills");

const STEPS = [
  "scope",
  "research",
  "model",
  "challenge",
  "conclude",
  "deliver",
  "refresh",
  "demo-prep",
];

/** Which shared files each skill gets. */
const ROUTES = {
  // The use case: the practice, the deliverable standard, its storyline.
  cdd: ["practice.md", "deliverable-standards.md", "cdd-storyline.md"],
  // The shared steps: the practice; deliver also the deliverable standard.
  ...Object.fromEntries(STEPS.map((s) => [s, ["practice.md"]])),
  deliver: ["practice.md", "deliverable-standards.md"],
  // Pre-project: the method and the voice; storyline also writes a ghost
  // deck to the workspace, so it gets the practice and the CDD storyline.
  proposal: ["engagement-method.md", "deliverable-standards.md"],
  storyline: [
    "engagement-method.md",
    "deliverable-standards.md",
    "cdd-storyline.md",
    "practice.md",
  ],
};

const sharedFiles = new Set(readdirSync(sharedDir));
const skills = readdirSync(skillsDir).filter((name) =>
  statSync(join(skillsDir, name)).isDirectory(),
);

let failed = false;
for (const skill of skills) {
  const wanted = ROUTES[skill];
  if (!wanted) {
    console.error(`skills/${skill}: no route in sync-shared.mjs — add one`);
    failed = true;
    continue;
  }
  const refs = join(skillsDir, skill, "references");
  mkdirSync(refs, { recursive: true });

  // Prune shared files this skill no longer wants; its own files stay.
  for (const existing of readdirSync(refs)) {
    if (sharedFiles.has(existing) && !wanted.includes(existing)) {
      rmSync(join(refs, existing));
      console.log(`  removed skills/${skill}/references/${existing}`);
    }
  }
  for (const file of wanted) {
    if (!existsSync(join(sharedDir, file))) {
      console.error(`shared/${file} is missing (wanted by ${skill})`);
      failed = true;
      continue;
    }
    cpSync(join(sharedDir, file), join(refs, file));
  }
  console.log(`synced ${wanted.length} shared file(s) → skills/${skill}/references/`);
}

for (const routed of Object.keys(ROUTES)) {
  if (!skills.includes(routed)) {
    console.error(`sync-shared.mjs routes "${routed}", but skills/${routed} does not exist`);
    failed = true;
  }
}

if (failed) process.exit(1);
console.log(`Done. ${skills.length} skill(s) updated.`);
