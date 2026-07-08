#!/usr/bin/env node
/**
 * Copy the canonical shared reference files into every skill's `references/`
 * folder, so each skill is self-contained (plugins don't reliably copy files
 * that live outside a skill's own directory) while we still edit the shared
 * files in one place.
 *
 * Files are grouped so each skill only gets what its output format needs:
 *   - common: analytical standards + how to pull aqmen data (all skills)
 *   - report: HTML report style + template  (skills named "*-report")
 *   - deck:   deck design system + pptx builder (skills named "*-deck")
 * A skill matching neither suffix gets everything (safe fallback).
 *
 * Each module also has a format-agnostic content spec, "<module>-content.md",
 * which is the single source of truth for what the deliverable covers. It is
 * synced into BOTH that module's report and deck skills (e.g.
 * market-sizing-content.md → market-sizing-report AND market-sizing-deck), so
 * the two formats never drift.
 *
 * A "*-deck" skill additionally gets its own populated starter template,
 * "<skill>-template.pptx" (e.g. market-sizing-deck-template.pptx).
 *
 * Run from anywhere:  node plugins/aqmen/scripts/sync-shared.mjs
 */
import { cpSync, existsSync, mkdirSync, readdirSync, rmSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const sharedDir = join(pluginRoot, "shared");
const skillsDir = join(pluginRoot, "skills");

const GROUPS = {
  common: ["report-standards.md", "report-data.md"],
  // Note: report-template.html is NOT shipped to skills — the populated
  // <module>-report-template.html already embeds the whole shell (CSS, head,
  // components) inline, so shipping the shell too would duplicate it. The shell
  // stays in shared/ only as the CSS source for build-html-examples.py.
  report: ["report-style.md"],
  deck: ["deck-style.md", "aqmen_deck.py"],
};

// Files that a skill may have received in the past but should no longer carry —
// pruned from references/ on sync.
const RETIRED = ["report-template.html"];

// Shared files that belong to *some* group or naming convention — used to prune
// stale files a skill no longer wants.
const allTemplates = readdirSync(sharedDir).filter(
  (f) => f.endsWith("-template.pptx") || f.endsWith("-report-template.html"),
);
const allContent = readdirSync(sharedDir).filter((f) =>
  f.endsWith("-content.md"),
);

// The module name for a skill is its name minus the format suffix.
const moduleOf = (name) => name.replace(/-(report|deck)$/, "");

function filesForSkill(name) {
  const module = moduleOf(name);
  const withContent = (files) => {
    const content = `${module}-content.md`; // shared across both formats
    if (existsSync(join(sharedDir, content))) files.push(content);
    return files;
  };
  if (name.endsWith("-report")) {
    const files = withContent([...GROUPS.common, ...GROUPS.report]);
    const tmpl = `${module}-report-template.html`; // this module's populated example
    if (existsSync(join(sharedDir, tmpl))) files.push(tmpl);
    return files;
  }
  if (name.endsWith("-deck")) {
    const files = withContent([...GROUPS.common, ...GROUPS.deck]);
    const tmpl = `${name}-template.pptx`; // this skill's own starter deck
    if (existsSync(join(sharedDir, tmpl))) files.push(tmpl);
    return files;
  }
  return Object.values(GROUPS).flat(); // fallback: everything
}

const skills = readdirSync(skillsDir).filter((name) =>
  statSync(join(skillsDir, name)).isDirectory(),
);

for (const skill of skills) {
  const refs = join(skillsDir, skill, "references");
  mkdirSync(refs, { recursive: true });
  const wanted = filesForSkill(skill);
  const wantedSet = new Set(wanted);

  // Remove stale shared files from a skill that no longer wants them
  // (e.g. a *-deck skill should not carry report-template.html, and a skill
  // should not carry another skill's starter template). Only files that belong
  // to some group are candidates for removal; skill-specific reference files
  // (structure docs) are left untouched.
  const allShared = new Set([
    ...Object.values(GROUPS).flat(), ...allTemplates, ...allContent, ...RETIRED,
  ]);
  for (const existing of readdirSync(refs)) {
    if (allShared.has(existing) && !wantedSet.has(existing)) {
      rmSync(join(refs, existing));
    }
  }

  for (const file of wanted) {
    cpSync(join(sharedDir, file), join(refs, file));
  }
  console.log(`synced ${wanted.length} shared file(s) → skills/${skill}/references/`);
}

console.log(`Done. ${skills.length} skill(s) updated.`);
