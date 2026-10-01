#!/usr/bin/env python
"""
Build the aqmen CDD deliverable set from one content JSON.

    python build_cdd.py content.json <outdir> [--pdf] [--final] [--only deck|html|summary]

Writes into <outdir>:
    <slug>.pptx                      the deck (editable, native charts)
    <slug>.html                      the self-contained HTML report
    <slug> - Executive Summary.docx  the 2-page Word leave-behind
    <slug> - Executive Summary.pdf   (with --pdf, Windows + Word only)

--final drops the DRAFT tag from the deck. --only restricts to one format.
Requires python-pptx and python-docx.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import cdd_render as R  # noqa: E402


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    content = R.load_content(argv[1])
    outdir = Path(argv[2]); outdir.mkdir(parents=True, exist_ok=True)
    want_pdf = "--pdf" in argv
    final = "--final" in argv
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    base = R.slug(content)

    if only in (None, "deck"):
        n = R.build_deck(content, str(outdir / f"{base}.pptx"), draft=not final)
        print(f"deck     {outdir / (base + '.pptx')}  ({n} slides)")
    if only in (None, "html"):
        (outdir / f"{base}.html").write_text(R.build_html(content), encoding="utf-8")
        print(f"html     {outdir / (base + '.html')}")
    if only in (None, "summary"):
        docx = outdir / f"{base} - Executive Summary.docx"
        R.build_summary_docx(content, str(docx))
        print(f"summary  {docx}")
        if want_pdf:
            pdf = docx.with_suffix(".pdf")
            ok = R.docx_to_pdf(str(docx.resolve()), str(pdf.resolve()))
            print(f"pdf      {pdf if ok else 'FAILED (Word not available?)'}")


if __name__ == "__main__":
    main(sys.argv)
