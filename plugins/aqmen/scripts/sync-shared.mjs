#!/usr/bin/env node
/**
 * Copy the canonical shared reference files into every skill's `references/`
 * folder, so each skill is self-contained (plugins don't reliably copy files
 * that live outside a skill's own directory) while we still edit the shared
 * files in one place.
 *
 * Run from anywhere:  node plugins/aqmen/scripts/sync-shared.mjs
 */
import { cpSync, mkdirSync, readdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const sharedDir = join(pluginRoot, "shared");
const skillsDir = join(pluginRoot, "skills");

const sharedFiles = readdirSync(sharedDir).filter((f) =>
  statSync(join(sharedDir, f)).isFile(),
);

const skills = readdirSync(skillsDir).filter((name) =>
  statSync(join(skillsDir, name)).isDirectory(),
);

for (const skill of skills) {
  const refs = join(skillsDir, skill, "references");
  mkdirSync(refs, { recursive: true });
  for (const file of sharedFiles) {
    cpSync(join(sharedDir, file), join(refs, file));
  }
  console.log(`synced ${sharedFiles.length} shared file(s) → skills/${skill}/references/`);
}

console.log(`Done. ${skills.length} skill(s) updated.`);
