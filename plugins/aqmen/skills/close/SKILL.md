---
name: close
description: 'Close an Aqmen project for delivery — everything stale refreshed and broken fixed, the leftovers found (artifacts nothing reads that are not deliverables, superseded drafts, failed transformations, empty collections), deleted or kept as working material only on the user''s yes, the deliverables and the project''s notes tidied, a final check. Use for "clean up the project", "wrap up", "close the project", "finalize", "prepare the final version", "prepare the presentation", "tidy the workspace", "remove unused", "get it ready to send", "get it ready to publish", or after aqmen:deliver.'
---

<!-- Generated from the Aqmen platform's playbooks and practices (aqmen-data-workspace, packages/content/src/skills.ts). Do not edit by hand: change the definition there and run `pnpm skills:generate`. -->

# Close — a clean project for delivery

The method lives on the platform, not in this skill:
`read_instructions` with topics `["close"]` (with `start` and
`rules` if not read this session), then the units it names as you reach
them, and follow it. Inside a playbook, the playbook's stage and gate
decide when it is done; on its own, the practice's Check and Then.

## What Claude adds

- **Ask before every delete.** Show the list grouped Delete / Keep as
  working material / Keep and wait for the user's yes, item by item or on
  the list as a whole — in autonomous mode too. Nothing upstream of a
  deliverable goes.
- **Stale first, through `aqmen:refresh`.** A stale or broken item is
  brought current before the leftovers are judged: what is unused can only
  be told once everything reads what it should.

## Then

The project is ready to send, archive or publish; before publishing, the
publish audit (`explore`). When the data moves, `aqmen:refresh`.
