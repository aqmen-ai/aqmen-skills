#!/usr/bin/env python
"""
Build the aqmen CDD deliverable set from one content JSON.

    python build_cdd.py content.json <outdir> [--pdf] [--final] [--only deck|html|summary]

Writes into <outdir>:
    <slug>.pptx                      the deck (editable, native charts)
    <slug>.html                      the self-contained HTML report
    <slug> - Executive Summary.docx  the 2-page Word leave-behind
    <slug> - Executive Summary.pdf   (with --pdf, Windows + Word only)

    <slug>.build.json                the content hash each format was built from

--final drops the DRAFT tag from the deck. --only restricts to one format and
warns when a skipped format on disk was built from different content.
Requires python-pptx and python-docx.
"""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import cdd_render as R  # noqa: E402

FORMATS = ("deck", "html", "summary")


def content_hash(path):
    """Hash of the content as data, so reformatting the JSON doesn't count."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    content = R.load_content(argv[1])
    outdir = Path(argv[2]); outdir.mkdir(parents=True, exist_ok=True)
    want_pdf = "--pdf" in argv
    final = "--final" in argv
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    base = R.slug(content)
    if only is not None and only not in FORMATS:
        raise SystemExit(f"--only takes one of {', '.join(FORMATS)}")
    files = {"deck": outdir / f"{base}.pptx", "html": outdir / f"{base}.html",
             "summary": outdir / f"{base} - Executive Summary.docx"}
    manifest_path = outdir / f"{base}.build.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    digest = content_hash(argv[1])

    if only in (None, "deck"):
        n = R.build_deck(content, str(files["deck"]), draft=not final)
        print(f"deck     {files['deck']}  ({n} slides)")
    if only in (None, "html"):
        files["html"].write_text(R.build_html(content), encoding="utf-8")
        print(f"html     {files['html']}")
    if only in (None, "summary"):
        docx = files["summary"]
        R.build_summary_docx(content, str(docx))
        print(f"summary  {docx}")
        if want_pdf:
            pdf = docx.with_suffix(".pdf")
            ok = R.docx_to_pdf(str(docx.resolve()), str(pdf.resolve()))
            print(f"pdf      {pdf if ok else 'FAILED (Word not available?)'}")

    built = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for fmt in FORMATS:
        if only in (None, fmt):
            manifest[fmt] = {"hash": digest, "built": built}
        elif files[fmt].exists() and manifest.get(fmt, {}).get("hash") != digest:
            print(f"warning  {files[fmt].name} is stale: built from other content; "
                  f"rebuild with --only {fmt} or without --only", file=sys.stderr)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv)
