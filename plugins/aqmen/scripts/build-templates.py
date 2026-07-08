#!/usr/bin/env python3
"""Generate the aqmen deck **starter templates** — one styled, populated `.pptx`
per module, saved to `shared/`:

    shared/market-sizing-deck-template.pptx
    shared/competitive-landscape-deck-template.pptx
    shared/company-analysis-deck-template.pptx

Content comes from `example_content.py` (the single source shared with the HTML
report templates), so a module's deck and report always show the same
information — differing only in format. Edit the content there, then regenerate
both and re-sync:

    python3 plugins/aqmen/scripts/build-templates.py
    python3 plugins/aqmen/scripts/build-html-examples.py
    node   plugins/aqmen/scripts/sync-shared.mjs

Requires: python-pptx.
"""

import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(HERE, "..", "shared")
sys.path.insert(0, SHARED)
sys.path.insert(0, HERE)

from aqmen_deck import Deck, Bullet, ChartSpec, MekkoColumn, HarveyRow  # noqa: E402
from example_content import MODULES  # noqa: E402

YEAR = str(date.today().year)


def _bullets(body):
    return [Bullet(text, level=level, bold=bold) for (text, bold, level) in body]


def _takeaways(sec):
    tk = list(sec.get("so_whats", []))
    if sec.get("watchout"):
        tk.append("Watch-out: " + sec["watchout"])
    return tk


def build_deck(content, path):
    d = Deck(draft=True)
    doctype = content["doctype"]
    d.title_slide(content["title"], content["subtitle"], YEAR)
    ag = content["agenda"]
    d.agenda(ag["items"], active=ag.get("active"),
             subitems=ag.get("subitems"), active_sub=ag.get("active_sub"))
    d.executive_summary(content["exec_summary"])

    for sec in content["sections"]:
        kind = sec["kind"]
        eyebrow = (doctype, sec["title"])
        common = dict(eyebrow=eyebrow, source=sec.get("source"),
                      takeaways=_takeaways(sec),
                      illustrative=sec.get("illustrative", False))
        if kind in ("content", "scenario"):
            d.content_slide(sec["headline"], body=_bullets(sec.get("body", [])),
                            left_title=sec.get("left_title"), **common)
        elif kind == "chart":
            c = sec["chart"]
            spec = ChartSpec(kind=c["kind"], categories=c["categories"],
                             series=c["series"],
                             number_format=c.get("number_format", "#,##0"),
                             legend=c.get("legend", True),
                             y_title=c.get("y_title"))
            d.chart_slide(sec["headline"], chart=spec,
                          chart_title=sec.get("chart_title"), **common)
        elif kind == "mekko":
            cols = [MekkoColumn(lbl, w, segs) for (lbl, w, segs) in sec["mekko"]]
            d.marimekko_slide(sec["headline"], columns=cols,
                              chart_title=sec.get("chart_title"), **common)
        elif kind == "harvey":
            rows = [HarveyRow(lbl, cells) for (lbl, cells) in sec["rows"]]
            d.harvey_matrix_slide(sec["headline"], columns=sec["columns"],
                                  rows=rows, row_label_header=sec.get("row_header", ""),
                                  **common)
        else:
            raise ValueError(f"unknown section kind: {kind!r}")

    # Sources & confidence
    bullets = [Bullet(f"{src}  —  confidence {conf}/5  —  {note}")
               for (src, conf, note) in content["sources"]]
    d.content_slide(
        "Sources & confidence", body=bullets,
        eyebrow=("Appendix", "Sources & confidence"),
        source="Confidence: 5 primary · 4 credible secondary · 3 triangulated "
               "(news cap) · 2 weak · 1 estimate")
    d.save(path)
    return len(d.prs.slides._sldIdLst)


def main():
    for module, content in MODULES.items():
        name = f"{module}-deck-template.pptx"
        n = build_deck(content, os.path.join(SHARED, name))
        print(f"wrote {name}  ({n} slides)")


if __name__ == "__main__":
    main()
