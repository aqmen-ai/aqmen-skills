#!/usr/bin/env python
"""
Render an Aqmen scope / proposal from a JSON spec into an editable Word document
in the aqmen brand (Montserrat, navy #03045E palette, A4, header/footer, wordmark).

Usage:
    python build_scope.py spec.json output.docx

The spec is a plain JSON document (see ../references/spec-format.md and
../assets/example-meridian.json). The renderer only lays things out — every word
of content comes from the spec, so the consultant edits the JSON (or the Word
file afterwards), never this script.

Requires python-docx (pip install python-docx).
"""
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Emu

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
TEMPLATE = ASSETS / "scope-template.docx"
LOGO = ASSETS / "logo_deepblue.png"

# Aqmen brand palette (shared/deck-style.md) — blue-dominant, azure as the accent
FONT = "Montserrat"
NAVY = "03045E"        # titles, section headings, table header fill
BLUE = "0728A3"        # labels, sub-headings, hypothesis ids
AZURE = "2E6FD6"       # single accent — rules under headings, cover bar
INK = "302E2E"         # body text
GREY = "8A8A8A"        # captions, kicker, footer lines
BORDER = NAVY          # table/box borders — same navy as the header row
FILL = "D6EEF5"        # callout / hypothesis box fill (cyan muted)
GANTT_BAR = NAVY
GANTT_MILESTONE = "2E6FD6"
GANTT_GRID = "D6EEF5"
WHITE = "FFFFFF"
TEXT = INK
LIGHT_GREY = GREY

TEXT_WIDTH = 9411  # dxa; A4 minus the template's margins


# --------------------------------------------------------------------------- #
# Low-level helpers
# --------------------------------------------------------------------------- #
def rgb(hexstr):
    return RGBColor.from_string(hexstr.upper())


def set_spacing(p, before=None, after=None):
    pf = p.paragraph_format
    if before is not None:
        pf.space_before = Pt(before / 20)  # values given in twentieths (Word's w:spacing)
    if after is not None:
        pf.space_after = Pt(after / 20)


def add_border(p, side, sz=8, space=2, color=NAVY):
    """Paragraph border on one side (top/bottom/left/right)."""
    pPr = p._p.get_or_add_pPr()
    pBdr = pPr.find(qn("w:pBdr"))
    if pBdr is None:
        pBdr = OxmlElement("w:pBdr")
        # pBdr must precede spacing/jc in pPr; insert after pStyle/keepNext etc.
        pPr.insert(0, pBdr)
    el = OxmlElement(f"w:{side}")
    el.set(qn("w:val"), "single")
    el.set(qn("w:sz"), str(sz))
    el.set(qn("w:space"), str(space))
    el.set(qn("w:color"), color)
    pBdr.append(el)


def keep_with_next(p):
    p.paragraph_format.keep_with_next = True


INLINE = re.compile(r"(\*\*.+?\*\*|_.+?_)")


def add_runs(p, text, size=None, color=None, bold=None, italic=None):
    """Add text to a paragraph, honouring **bold** and _italic_ inline markup.

    `bold`/`italic` set the baseline; markup toggles on top of it. Keeping the
    markup minimal (two markers) means consultants can write the spec by hand.
    """
    for part in INLINE.split(text):
        if not part:
            continue
        b, i = bold, italic
        if part.startswith("**") and part.endswith("**"):
            part, b = part[2:-2], True
        elif part.startswith("_") and part.endswith("_") and len(part) > 2:
            part, i = part[1:-1], True
        r = p.add_run(part)
        r.font.name = FONT
        rPr = r._r.get_or_add_rPr()
        rFonts = rPr.find(qn("w:rFonts"))
        if rFonts is None:
            rFonts = OxmlElement("w:rFonts")
            rPr.insert(0, rFonts)
        for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rFonts.set(qn(attr), FONT)
        if size is not None:
            r.font.size = Pt(size / 2)  # half-points, as in the XML
        if color is not None:
            r.font.color.rgb = rgb(color)
        if b is not None:
            r.font.bold = b
        if i is not None:
            r.font.italic = i
    return p


def para(doc, text="", size=None, color=None, bold=None, italic=None, before=None, after=160, style=None):
    p = doc.add_paragraph(style=style)
    set_spacing(p, before, after)
    if text:
        add_runs(p, text, size, color, bold, italic)
    return p


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def cell_borders(cell, color=BORDER, sz=4):
    tcPr = cell._tc.get_or_add_tcPr()
    old = tcPr.find(qn("w:tcBorders"))
    if old is not None:
        tcPr.remove(old)  # replace, never stack two border definitions
    borders = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tcPr.append(borders)


def cell_margins(cell, top=70, bottom=70, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tcPr.append(mar)


def set_col_widths(table, widths):
    """Fixed layout with explicit widths (dxa) so Word doesn't autofit."""
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    jc = OxmlElement("w:jc")
    jc.set(qn("w:val"), "center")
    tblPr.append(jc)
    grid = table._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(w))
    for row in table.rows:
        for cell, w in zip(row.cells, widths):
            cell.width = Emu(w * 635)  # 1 dxa = 635 EMU


def fill_cell(cell, content, size=None, color=None, bold=None, italic=None, after=40):
    """content: str or list[str]; each item becomes a paragraph."""
    items = content if isinstance(content, list) else [content]
    first = True
    for item in items:
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        set_spacing(p, None, after)
        add_runs(p, str(item), size, color, bold, italic)


def new_table(doc, rows, cols, widths, header=False):
    t = doc.add_table(rows=rows, cols=cols)
    set_col_widths(t, widths)
    for i, row in enumerate(t.rows):
        # Never split a row across pages: boxes and table rows read as units.
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        if header and i == 0:
            trPr.append(OxmlElement("w:tblHeader"))  # repeats if the table breaks
        for c in row.cells:
            cell_borders(c)
    return t


def glue_rows(table, n=2):
    """Keep the first n rows together (header + first body row) so a table
    never opens with an orphaned header at the foot of a page."""
    for row in list(table.rows)[: max(n - 1, 0)]:
        for c in row.cells:
            for p in c.paragraphs:
                keep_with_next(p)


def spacer(doc, after=120):
    p = doc.add_paragraph()
    set_spacing(p, 0, after)
    return p


# --------------------------------------------------------------------------- #
# Block renderers
# --------------------------------------------------------------------------- #
def render_para(doc, b):
    para(doc, b["text"], after=b.get("after", 160))


def render_label(doc, b):
    # Small navy caps label that introduces a group (e.g. "THE DECISION ARES FACES")
    p = para(doc, b["text"].upper(), size=18, color=BLUE, bold=True, before=220, after=80)
    keep_with_next(p)


def render_bullets(doc, b, style="List Bullet"):
    for item in b["items"]:
        p = doc.add_paragraph(style=style)
        add_runs(p, item)


def render_numbered(doc, b):
    render_bullets(doc, b, style="List Number")


def render_callout(doc, b):
    """Light-blue box listing short items; optional **lead** per item."""
    t = new_table(doc, 1, 1, [TEXT_WIDTH])
    c = t.cell(0, 0)
    shade(c, FILL)
    cell_margins(c, 100, 100, 140, 140)
    fill_cell(c, b["items"])
    spacer(doc)


def render_hypotheses(doc, b):
    """The hypotheses box: H1/H2… in navy, statement in italics, optional ratings.

    Ratings (confidence × importance) follow the 80/20 discipline: they tell the
    team where to start and tell the client which assertions we are least sure of.
    """
    t = new_table(doc, 1, 1, [TEXT_WIDTH])
    c = t.cell(0, 0)
    shade(c, FILL)
    cell_margins(c, 100, 100, 140, 140)
    first = True
    for i, h in enumerate(b["items"], 1):
        p = c.paragraphs[0] if first else c.add_paragraph()
        first = False
        set_spacing(p, None, 40)
        hid = h.get("id") or f"H{i}"
        add_runs(p, f"{hid}.  ", color=BLUE, bold=True)
        add_runs(p, h["text"], italic=True)
        tags = []
        if h.get("confidence"):
            tags.append(f"confidence {h['confidence'].lower()}")
        if h.get("importance"):
            tags.append(f"importance {h['importance'].lower()}")
        if tags:
            add_runs(p, "  [" + ", ".join(tags) + "]", size=17, color=GREY)
        if h.get("action"):
            p2 = c.add_paragraph()
            set_spacing(p2, None, 60)
            add_runs(p2, "Unlocks: " + h["action"], size=18, color=GREY)
    spacer(doc)


def render_subheading(doc, b):
    p = para(doc, b["text"], size=18, color=BLUE, bold=True, before=60, after=40)
    keep_with_next(p)


def render_workstream(doc, b):
    p = para(doc, b["title"], size=22, color=NAVY, bold=True, before=260, after=80)
    add_border(p, "left", sz=20, space=6, color=AZURE)
    keep_with_next(p)
    render_blocks(doc, b.get("blocks", []))


def render_table(doc, b):
    cols = b["columns"]
    n = len(cols)
    widths = b.get("widths")
    if not widths:
        # Default: first column narrow, remainder shared
        first = 2400 if n > 1 else TEXT_WIDTH
        rest = (TEXT_WIDTH - first) // max(n - 1, 1)
        widths = [first] + [rest] * (n - 1) if n > 1 else [first]
    header = b.get("header", True)
    rows = b["rows"]
    t = new_table(doc, len(rows) + (1 if header else 0), n, widths, header=header)
    r0 = 0
    if header:
        for j, name in enumerate(cols):
            c = t.cell(0, j)
            shade(c, NAVY)
            cell_margins(c)
            fill_cell(c, str(name).upper(), size=17, color=WHITE, bold=True)
        r0 = 1
        glue_rows(t, 2)
    for i, row in enumerate(rows):
        for j in range(n):
            c = t.cell(r0 + i, j)
            cell_margins(c)
            val = row[j] if j < len(row) else ""
            # First column reads as a row label
            fill_cell(c, val, size=19, bold=True if (j == 0 and b.get("bold_first", True)) else None)
    spacer(doc)


def render_columns(doc, b):
    """Side-by-side boxes with a navy title row (e.g. Month 1 | Month 2 | Month 3)."""
    cols = b["columns"]  # list of {"title": str, "items": [str]}
    n = len(cols)
    w = TEXT_WIDTH // n
    t = new_table(doc, 2, n, [w] * n, header=True)
    for j, col in enumerate(cols):
        h = t.cell(0, j)
        shade(h, NAVY)
        cell_margins(h)
        fill_cell(h, col["title"], size=19, color=WHITE, bold=True)
        c = t.cell(1, j)
        cell_margins(c)
        fill_cell(c, ["•  " + it for it in col.get("items", [])], size=19)
    glue_rows(t, 2)
    spacer(doc)


def render_quote(doc, b):
    p = para(doc, b["text"], color=GREY, italic=True, after=120)
    add_border(p, "left", sz=12, space=8, color=AZURE)


def render_page_break(doc, b):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def render_signature(doc, b):
    parties = b["parties"]  # [{"party": "Aqmen AI", "name": ..., "title": ...}, ...]
    w = TEXT_WIDTH // len(parties)
    t = new_table(doc, 1, len(parties), [w] * len(parties))
    for j, pty in enumerate(parties):
        c = t.cell(0, j)
        cell_margins(c, 120, 120, 140, 140)
        fill_cell(
            c,
            [
                f"**{pty['party']}**",
                "",
                "Signature: ________________________",
                f"Name: {pty.get('name', '')}",
                f"Title: {pty.get('title', '')}",
                "Date:",
            ],
            size=19,
            after=60,
        )


def render_gantt(doc, b):
    """A Gantt chart drawn as a table: one row per workstream, one narrow column
    per week; navy cells are work, azure cells with a diamond are milestones
    (gates, client sessions). Reads faster than a week-by-week text grid and
    stays editable in Word.

    Spec: {"type": "gantt", "columns": ["W1 6 Oct", ...],
           "rows": [{"name": "WS1 Market", "bars": [[1, 3]], "owner": "Ignacio"}],
           "milestones": [{"column": 2, "label": "Gate 1"}, ...]}
    Bars are inclusive 1-based column ranges. `owner` is optional and prints
    in grey under the row name.
    """
    cols = b["columns"]
    rows = b["rows"]
    milestones = b.get("milestones", [])
    n = len(cols)
    label_w = b.get("label_width", 2400)
    week_w = (TEXT_WIDTH - label_w) // n
    widths = [label_w] + [week_w] * n
    has_ms = bool(milestones)
    t = new_table(doc, len(rows) + 1 + (1 if has_ms else 0), n + 1, widths, header=True)
    # header
    h = t.cell(0, 0); shade(h, NAVY); cell_margins(h, 50, 50, 90, 90)
    fill_cell(h, b.get("label", "WORKSTREAM"), size=15, color=WHITE, bold=True)
    for j, name in enumerate(cols, 1):
        c = t.cell(0, j); shade(c, NAVY); cell_margins(c, 50, 50, 30, 30)
        fill_cell(c, str(name), size=13, color=WHITE, bold=True)
        c.paragraphs[0].alignment = 1  # centre
    # rows
    for i, row in enumerate(rows, 1):
        c = t.cell(i, 0); cell_margins(c, 60, 60, 90, 90)
        items = [f"**{row['name']}**"]
        fill_cell(c, items, size=16)
        if row.get("owner"):
            p = c.add_paragraph(); set_spacing(p, 0, 0)
            add_runs(p, row["owner"], size=13, color=GREY)
        active = set()
        for a, z in row.get("bars", []):
            active.update(range(a, z + 1))
        for j in range(1, n + 1):
            c = t.cell(i, j); cell_margins(c, 60, 60, 20, 20)
            cell_borders(c, color=GANTT_GRID)
            if j in active:
                shade(c, GANTT_BAR)
            fill_cell(c, "", size=12)
    # milestones row
    if has_ms:
        r = len(rows) + 1
        c = t.cell(r, 0); cell_margins(c, 60, 60, 90, 90)
        fill_cell(c, "**Milestones**", size=16)
        by_col = {}
        for m in milestones:
            by_col.setdefault(m["column"], []).append(m["label"])
        for j in range(1, n + 1):
            c = t.cell(r, j); cell_margins(c, 40, 40, 20, 20)
            cell_borders(c, color=GANTT_GRID)
            if j in by_col:
                shade(c, GANTT_MILESTONE)
                fill_cell(c, ["◆"] + by_col[j], size=11, color=WHITE, bold=True)
                for p in c.paragraphs:
                    p.alignment = 1
            else:
                fill_cell(c, "", size=12)
    glue_rows(t, 2)
    spacer(doc)


RENDERERS = {
    "para": render_para,
    "label": render_label,
    "bullets": render_bullets,
    "numbered": render_numbered,
    "callout": render_callout,
    "hypotheses": render_hypotheses,
    "subheading": render_subheading,
    "workstream": render_workstream,
    "table": render_table,
    "columns": render_columns,
    "gantt": render_gantt,
    "quote": render_quote,
    "page_break": render_page_break,
    "signature": render_signature,
}


def render_blocks(doc, blocks):
    for b in blocks:
        kind = b.get("type")
        if kind not in RENDERERS:
            raise SystemExit(f"Unknown block type: {kind!r} in {json.dumps(b)[:120]}")
        RENDERERS[kind](doc, b)


# --------------------------------------------------------------------------- #
# Document-level pieces
# --------------------------------------------------------------------------- #
def render_cover(doc, cover):
    p = doc.add_paragraph()
    set_spacing(p, 600, 1200)
    if LOGO.exists():
        p.add_run().add_picture(str(LOGO), width=Emu(2194560))
    para(doc, cover["kicker"].upper(), size=20, color=GREY, bold=True, after=280)
    para(doc, cover["title"], size=52, color=NAVY, bold=True, after=120)
    if cover.get("subtitle"):
        para(doc, cover["subtitle"], size=28, color=BLUE, bold=True, after=280)
    if cover.get("summary"):
        para(doc, cover["summary"], size=21, color=INK, after=3400)
    p = para(doc, cover.get("confidentiality", "Strictly private & confidential"),
             size=18, color=NAVY, bold=True, after=60)
    add_border(p, "top", sz=8, space=6, color=AZURE)
    para(doc, cover["date"], size=19, color=GREY, after=240)
    for line in cover.get("footer_lines", []):
        para(doc, line, size=15, color=GREY, after=40)
    render_page_break(doc, None)


def render_section(doc, s):
    p = para(doc, s["heading"], size=26, color=NAVY, bold=True, before=320, after=160)
    add_border(p, "bottom", sz=8, space=2, color=AZURE)
    keep_with_next(p)
    render_blocks(doc, s.get("blocks", []))


def set_header_footer(doc, spec):
    sec = doc.sections[0]
    # The Header/Footer styles carry Word's default centre (4680) and right
    # (9360) tab stops, so a single tab lands mid-page. Clear them and keep only
    # a right stop at the text edge.
    for p in (sec.header.paragraphs[0], sec.footer.paragraphs[0]):
        _fix_tabs(p)
    hdr = spec.get("header", {})
    if hdr:
        hp = sec.header.paragraphs[0]
        # Rebuild the runs (the template's tab lives inside the first run, so
        # editing run text would drop it). pPr (border, tab stop) is kept.
        for r in list(hp.runs):
            r._r.getparent().remove(r._r)
        add_runs(hp, hdr.get("left", ""), size=15, color=NAVY, bold=True)
        hp.add_run().add_tab()
        add_runs(hp, hdr.get("right", "Strictly private & confidential"), size=15, color=GREY)
    ftr = spec.get("footer")
    if ftr:
        fp = sec.footer.paragraphs[0]
        # Footer = "<text> <tab> <PAGE field>"; replace only the text run.
        for r in fp.runs:
            if r.text.strip() and not r._r.findall(qn("w:fldChar")) and not r._r.findall(qn("w:instrText")):
                r.text = ftr
                break


def _fix_tabs(p):
    pPr = p._p.get_or_add_pPr()
    tabs = pPr.find(qn("w:tabs"))
    if tabs is not None:
        pPr.remove(tabs)
    tabs = OxmlElement("w:tabs")
    for pos in ("4680", "9360"):
        t = OxmlElement("w:tab")
        t.set(qn("w:val"), "clear")
        t.set(qn("w:pos"), pos)
        tabs.append(t)
    t = OxmlElement("w:tab")
    t.set(qn("w:val"), "right")
    t.set(qn("w:pos"), str(TEXT_WIDTH))
    tabs.append(t)
    # w:tabs must come after w:pBdr and before w:spacing in pPr's sequence
    bdr = pPr.find(qn("w:pBdr"))
    style = pPr.find(qn("w:pStyle"))
    anchor = bdr if bdr is not None else style
    if anchor is not None:
        anchor.addnext(tabs)
    else:
        pPr.insert(0, tabs)


def build(spec_path, out_path):
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    doc = Document(str(TEMPLATE))
    render_cover(doc, spec["cover"])
    for s in spec["sections"]:
        render_section(doc, s)
    if spec.get("closing"):
        para(doc, spec["closing"], size=17, color=GREY, before=400, after=0)
    set_header_footer(doc, spec)
    doc.core_properties.title = spec["cover"]["title"]
    doc.core_properties.author = "Aqmen AI"
    doc.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    build(sys.argv[1], sys.argv[2])
