#!/usr/bin/env python3
"""Generate the aqmen **HTML report** starter templates — one populated,
self-contained `.html` per module, saved to `shared/`:

    shared/market-sizing-report-template.html
    shared/competitive-landscape-report-template.html
    shared/company-analysis-report-template.html

Content comes from `example_content.py` — the SAME single source the PPTX deck
templates use — so a module's report and deck show the same information, only in
a different format. The page reuses the head/CSS and chart helper from
`report-template.html` (the canonical shell), so styling stays single-sourced.

Run after editing content or the shell, then re-sync:

    python3 plugins/aqmen/scripts/build-templates.py       # PPTX
    python3 plugins/aqmen/scripts/build-html-examples.py   # HTML
    node   plugins/aqmen/scripts/sync-shared.mjs
"""

import html
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(HERE, "..", "shared")
sys.path.insert(0, HERE)

from example_content import MODULES  # noqa: E402

YEAR = str(date.today().year)
SHELL = os.path.join(SHARED, "report-template.html")


def esc(s):
    return html.escape(str(s))


# --------------------------------------------------------------------------- #
# Shell reuse — pull the head (CSS, CSP, logo, ECharts include) and the chart  #
# helper JS from report-template.html so styling stays single-sourced.         #
# --------------------------------------------------------------------------- #

def shell_parts(title):
    txt = open(SHELL, encoding="utf-8").read()
    # Head: everything through </head>. Drop the leading skeleton-instruction
    # comment and fill the <title> so the populated example is clean.
    head = txt[: txt.index("</head>") + len("</head>")]
    head = re.sub(r"<!--.*?-->\s*", "", head, count=1, flags=re.S)
    head = head.replace("{{REPORT_TITLE}}", esc(title))
    # Helper JS is the LAST <script> block — NOT the "<script>" that the leading
    # comment mentions (that earlier match previously swallowed the whole shell).
    open_idx = txt.rindex("<script>") + len("<script>")
    script = txt[open_idx: txt.rindex("</script>")]
    helpers = script[: script.index("// Example")].rstrip()
    scenario_js = script[script.index("// --- Scenario tabs ---"):].rstrip()
    return head, helpers, scenario_js


# --------------------------------------------------------------------------- #
# ECharts option builders (mirror the deck's native charts with the same data) #
# --------------------------------------------------------------------------- #

def _series_bar(series, stacked=False, horizontal=False):
    out = []
    for name, vals in series:
        s = {"name": name, "type": "bar", "data": list(vals),
             "label": {"show": True, "fontSize": 10,
                       "position": "right" if horizontal else "top"}}
        if stacked:
            s["stack"] = "total"
            s["label"]["position"] = "inside"
        out.append(s)
    return out


def chart_option(chart):
    kind = chart["kind"]
    cats = list(chart["categories"])
    series = chart["series"]
    multi = len(series) > 1
    legend = chart.get("legend", True) and multi
    opt = {"tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
           "grid": {"left": 48, "right": 24, "top": 20,
                    "bottom": 48 if legend else 28}}
    if legend:
        opt["legend"] = {"bottom": 0}
    if kind == "line":
        opt["xAxis"] = {"type": "category", "data": cats}
        opt["yAxis"] = {"type": "value"}
        opt["series"] = [{"name": n, "type": "line", "smooth": False,
                          "data": list(v), "label": {"show": True, "fontSize": 10,
                          "position": "top"}} for n, v in series]
    elif kind == "bar":  # horizontal
        opt["yAxis"] = {"type": "category", "data": cats}
        opt["xAxis"] = {"type": "value"}
        opt["series"] = _series_bar(series, stacked=False, horizontal=True)
    else:  # column / stacked_column
        stacked = kind == "stacked_column"
        opt["xAxis"] = {"type": "category", "data": cats}
        opt["yAxis"] = {"type": "value"}
        opt["series"] = _series_bar(series, stacked=stacked, horizontal=False)
    return opt


def mekko_option(mekko):
    """Render the Marimekko data as a stacked column (same numbers, native to
    ECharts): region categories × segment series."""
    cats = [lbl for (lbl, _w, _segs) in mekko]
    seg_names = [s for (s, _v) in mekko[0][2]]
    series = []
    for i, seg in enumerate(seg_names):
        vals = [dict(segs)[seg] for (_lbl, _w, segs) in mekko]
        series.append({"name": seg, "type": "bar", "stack": "total",
                       "data": vals,
                       "label": {"show": True, "fontSize": 10, "position": "inside"}})
    return {"tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {"bottom": 0},
            "grid": {"left": 48, "right": 24, "top": 20, "bottom": 48},
            "xAxis": {"type": "category", "data": cats},
            "yAxis": {"type": "value"},
            "series": series}


# --------------------------------------------------------------------------- #
# HTML body builders                                                           #
# --------------------------------------------------------------------------- #

def _ball(fill):
    """A consistent-size harvey ball as inline SVG: navy ring + navy pie wedge for
    the fill fraction (0–1). Uniform 15px box regardless of fill (unlike the
    unicode glyphs, which vary in size)."""
    import math
    f = max(0.0, min(1.0, fill))
    nv = "#03045E"
    ring = (f'<circle cx="8" cy="8" r="6.6" fill="#fff" stroke="{nv}" '
            f'stroke-width="1.3"/>')
    if f <= 0:
        wedge = ""
    elif f >= 1:
        wedge = f'<circle cx="8" cy="8" r="6.6" fill="{nv}"/>'
    else:
        ang = 2 * math.pi * f
        ex, ey = 8 + 6.6 * math.sin(ang), 8 - 6.6 * math.cos(ang)
        large = 1 if f > 0.5 else 0
        wedge = (f'<path d="M8,8 L8,1.4 A6.6,6.6 0 {large} 1 {ex:.2f},{ey:.2f} Z" '
                 f'fill="{nv}"/>')
    return (f'<svg width="15" height="15" viewBox="0 0 16 16" '
            f'style="vertical-align:middle">{ring}{wedge}</svg>')


def _bullets_html(body):
    lis = []
    for (text, bold, level) in body:
        inner = f"<strong>{esc(text)}</strong>" if bold else esc(text)
        ml = f' style="margin-left:{level*18}px"' if level else ""
        lis.append(f"<li{ml}>{inner}</li>")
    return "<ul>\n" + "\n".join(lis) + "\n</ul>"


def _insight_html(so_whats, watchout):
    out = []
    if so_whats:
        out.append('<div class="callout insight"><span class="tag">Insight</span>'
                   + esc(" · ".join(so_whats)) + "</div>")
    if watchout:
        out.append('<div class="callout watchout"><span class="tag">⚠ Watch-out</span>'
                   + esc(watchout) + "</div>")
    return "\n".join(out)


def _source_line(source):
    return (f'<p style="font-size:12.5px;color:var(--muted);margin:6px 0 0">'
            f'Source: {esc(source)}</p>') if source else ""


def _harvey_table(sec):
    cols = sec["columns"]
    head = ("<tr><th>" + esc(sec.get("row_header", "")) + "</th>"
            + "".join(f"<th>{esc(c)}</th>" for c in cols) + "</tr>")
    body = []
    for (label, cells) in sec["rows"]:
        tds = "".join(
            f'<td style="text-align:center">{_ball(v)}</td>'
            for v in cells)
        body.append(f"<tr><td><b>{esc(label)}</b></td>{tds}</tr>")
    return ("<table><thead>" + head + "</thead><tbody>"
            + "".join(body) + "</tbody></table>")


def _driver_tree_html(sec):
    """Expression tree: columns of two-tone nodes; each node shows its formula and
    an operator chip for how its children combine. Segments noted, not exploded."""
    cols = sec["tree"]
    parts = ['<div class="dtree">']
    for col in cols:
        parts.append('<div class="dtcol">')
        parts.append(f'<div class="dthead">{esc(col["header"])}</div>')
        for node in col["nodes"]:
            cert = node.get("certainty")
            cdot = f'<span class="cert cert-{cert}"></span>' if cert is not None else ""
            expr = f'<div class="expr">{esc(node["expr"])}</div>' if node.get("expr") else ""
            val = f'<div class="val">{esc(node["value"])}</div>' if node.get("value") is not None else ""
            op = f'<span class="op">{esc(node["operator"])}</span>' if node.get("operator") else ""
            parts.append(f'<div class="dtnode">{cdot}{op}'
                         f'<div class="lab">{esc(node["label"])}</div>{expr}{val}</div>')
        parts.append("</div>")
    parts.append("</div>")
    parts.append('<div class="dtkey"><span>Certainty of assumptions:</span>'
                 '<span><i class="cert-0"></i>Low</span>'
                 '<span><i class="cert-1"></i>Medium</span>'
                 '<span><i class="cert-2"></i>High</span></div>')
    if sec.get("note"):
        parts.append(f'<div class="dtnote">▸ {esc(sec["note"])}</div>')
    return "\n".join(parts)


def _positioning_html(sec):
    """2-axis positioning matrix: size-scaled, numbered boxes on a plane."""
    items = sec["items"]
    xt = sec.get("x_ticks", [])
    yt = sec.get("y_ticks", [])
    cells = []
    for it in items:
        badge = f'<span class="badge">{esc(it["num"])}</span>' if it.get("num") else ""
        pts = it.get("points") or []
        pad = it.get("pad", 0.05)
        if pts:
            minx = max(0.0, min(p[0] for p in pts) - pad)
            maxx = min(1.0, max(p[0] for p in pts) + pad)
            miny = max(0.0, min(p[1] for p in pts) - pad)
            maxy = min(1.0, max(p[1] for p in pts) + pad)
        else:
            hw = 0.5 * it.get("size", 0.5) * 0.5
            minx, maxx = it.get("x", 0.5) - hw, it.get("x", 0.5) + hw
            miny, maxy = it.get("y", 0.5) - hw * 1.2, it.get("y", 0.5) + hw * 1.2
        cells.append(
            f'<div class="pmitem" style="left:{minx*100:.1f}%;bottom:{miny*100:.1f}%;'
            f'width:{(maxx-minx)*100:.1f}%;height:{(maxy-miny)*100:.1f}%">'
            f'{badge}<div class="arch">{esc(it["label"])}</div></div>')
        if it.get("show_points", True):
            for (fx, fy) in pts:
                cells.append(f'<div class="pmdot" style="left:{fx*100:.1f}%;'
                             f'bottom:{fy*100:.1f}%"></div>')
    for i, tk in enumerate(xt):
        if tk:
            cells.append(f'<div class="pmxtick" style="left:{(i+0.5)/len(xt)*100:.1f}%">{esc(tk)}</div>')
    for i, tk in enumerate(yt):
        if tk:
            cells.append(f'<div class="pmytick" style="bottom:{(i+0.5)/len(yt)*100:.1f}%">{esc(tk)}</div>')
    return (f'<div class="pmatrix"><div class="pmytitle">{esc(sec["y_title"])}</div>'
            f'<div class="pmarea">{"".join(cells)}</div></div>'
            f'<div class="pmxtitle">{esc(sec["x_title"])}</div>')


_MK_PALETTE = ["#03045E", "#0728A3", "#2E6FD6", "#6BAED6", "#ADE8F3", "#8A8A8A"]


def _mekko_html(sec):
    """A true variable-width Marimekko: column widths ∝ one dimension, stack
    heights ∝ another. 'Whitespace' segments render hatched (SAM vs whitespace)."""
    mekko = sec["mekko"]  # [(label, width, [(seg, val), ...]), ...]
    seg_names = [s for s, _ in mekko[0][2]]
    color, ci = {}, 0
    for s in seg_names:
        if "whitespace" in s.lower():
            color[s] = None
        else:
            color[s] = _MK_PALETTE[ci % len(_MK_PALETTE)]
            ci += 1
    total_w = sum(w for _, w, _ in mekko) or 1.0
    max_total = max(sum(v for _, v in segs) for _, _, segs in mekko) or 1.0
    cols = []
    for (lab, w, segs) in mekko:
        ctot = sum(v for _, v in segs) or 1.0
        segdivs = []
        for (s, v) in segs:
            h = v / ctot * 100
            cls = "mkseg ws" if color[s] is None else "mkseg"
            bg = "" if color[s] is None else f";background:{color[s]}"
            segdivs.append(f'<div class="{cls}" style="height:{h:.1f}%{bg}">{v:g}</div>')
        colpct = sum(v for _, v in segs) / max_total * 100
        cols.append(
            f'<div class="mkcol" style="flex:{w:.4f} 1 0">'
            f'<div class="mkhead">{sum(v for _, v in segs):g}'
            f'<span>({w / total_w * 100:.0f}%)</span></div>'
            f'<div class="mkstackarea"><div class="mkstack" style="height:{colpct:.1f}%">'
            f'{"".join(segdivs)}</div></div>'
            f'<div class="mkxlab">{esc(lab)}</div></div>')
    leg = []
    for s in seg_names:
        sw = '<i class="wslegend"></i>' if color[s] is None else f'<i style="background:{color[s]}"></i>'
        leg.append(f"<span>{sw}{esc(s)}</span>")
    return (f'<div class="mekko">{"".join(cols)}</div>'
            f'<div class="mklegend">{"".join(leg)}</div>')


def _revenue_build_html(sec):
    """Competitive-landscape revenue build: players grouped by archetype, each with
    revenue × % addressable → market-specific revenue (bar), summed bottom-up."""
    info_cols = sec.get("info_cols", [["hq", "HQ"], ["employees", "Employees"]])
    unit = sec.get("unit", "$m")
    groups = sec["groups"]
    total = sec.get("total")
    fmt = lambda v: f"{v:,.0f}"  # noqa: E731
    ncols = len(info_cols) + 4
    all_m = [p.get("market_rev") or 0 for g in groups for p in g["players"]]
    mx = max(all_m) or 1.0  # scale player bars to the largest player

    def bar(v, full=False):
        w = 100.0 if full else ((v / mx * 100) if v is not None else 0)
        val = fmt(v) if v is not None else "—"
        return (f'<div class="rbar"><span class="rtrack"><span class="rfill" '
                f'style="width:{min(w,100):.1f}%"></span></span><b>{val}</b></div>')

    heads = ('<th class="l">Company</th>'
             + "".join(f'<th class="l">{esc(h)}</th>' for _, h in info_cols)
             + f'<th>Revenue ({unit})</th><th>% to market</th>'
             + f'<th class="l">Market revenue ({unit})</th>')
    rows = []
    for g in groups:
        rows.append(f'<tr class="grp"><td colspan="{ncols}">{esc(g["archetype"])}</td></tr>')
        for p in g["players"]:
            info_tds = "".join(f'<td>{esc(str(p.get(k, "")))}</td>' for k, _ in info_cols)
            rev, pct, m = p.get("revenue"), p.get("pct"), p.get("market_rev")
            rev_td = f'<td class="num">{fmt(rev) if rev is not None else "—"}</td>'
            pct_td = f'<td class="num">{pct:g}%</td>' if pct is not None else '<td class="num">—</td>'
            rows.append(f'<tr><td><b>{esc(p.get("name",""))}</b></td>{info_tds}'
                        f'{rev_td}{pct_td}<td>{bar(m)}</td></tr>')
    if total is not None:
        lbl = esc(sec.get("total_label", "Total addressable (bottom-up market)"))
        rows.append(f'<tr class="total"><td colspan="{ncols-1}">{lbl}</td>'
                    f'<td>{bar(total, full=True)}</td></tr>')
    cols = ('<colgroup>' + '<col>' * (ncols - 1) + '<col class="mrev"></colgroup>')
    return (f'<table class="rbuild">{cols}<thead><tr>{heads}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>')


def _heatmap_html(sec):
    """Sensitivity matrix: rows × cols grid shaded light→navy, base cell outlined."""
    rows, cols, vals = sec["rows"], sec["cols"], sec["values"]
    base = sec.get("base")
    fmt = sec.get("value_fmt", "{:.0f}")
    flat = [v for r in vals for v in r]
    lo, hi = min(flat), max(flat)
    span = (hi - lo) or 1.0

    def cellcol(t):  # light cyan (#ADE8F3) → navy (#03045E)
        a, b = (0xAD, 0xE8, 0xF3), (0x03, 0x04, 0x5E)
        return "#%02X%02X%02X" % tuple(int(a[k] + (b[k] - a[k]) * t) for k in range(3))

    head = (f'<tr><th class="rowlab">{esc(sec.get("row_header",""))}</th>'
            + "".join(f'<th class="collab">{esc(c)}</th>' for c in cols) + "</tr>")
    body = []
    for i, rlab in enumerate(rows):
        tds = [f'<td class="rowlab">{esc(rlab)}</td>']
        for j, c in enumerate(cols):
            v = vals[i][j]
            t = (v - lo) / span
            isb = base and tuple(base) == (i, j)
            ink = "#302E2E" if t <= 0.55 else "#fff"
            tds.append(f'<td class="cell{" base" if isb else ""}" '
                       f'style="background:{cellcol(t)};color:{ink}">{esc(fmt.format(v))}</td>')
        body.append("<tr>" + "".join(tds) + "</tr>")
    return (f'<div class="hmaxis col">{esc(sec.get("col_header",""))}</div>'
            '<div class="hmwrap"><table class="heatmap"><thead>' + head
            + "</thead><tbody>" + "".join(body) + "</tbody></table></div>")


def build_body(content, charts):
    """Return (body_html, chart_js_calls). Appends chart specs to `charts`."""
    parts = []
    parts.append('<div class="topbar"></div>')
    parts.append('<div class="page">')
    # brand bar
    parts.append('<div class="brandbar">'
                 '<span class="logo" role="img" aria-label="Aqmen"></span>'
                 '<span class="wordmark">Aqmen</span>'
                 f'<span class="doctype">{esc(content["doctype"])}</span></div>')
    # cover
    conf = content.get("confidence", 4)
    parts.append('<header class="cover">'
                 f'<h1>{esc(content["title"])}</h1>'
                 f'<p class="subtitle">{esc(content["subtitle"])}</p>'
                 '<div class="meta">'
                 '<span><b>Project:</b> [project]</span>'
                 f'<span><b>Date:</b> {YEAR}</span>'
                 '<span><b>Prepared by:</b> [author]</span>'
                 f'<span><b>Overall confidence:</b> <span class="cf cf-{conf}">{conf}</span></span>'
                 '</div></header>')
    # bottom line
    parts.append('<section class="bottomline"><span class="lbl">Bottom line</span>'
                 f'<p>{esc(content["bottom_line"])}</p></section>')
    # executive summary (grouped, nested)
    groups = []
    for (label, bullets) in content["exec_summary"]:
        subs = "".join(f"<li>{esc(b)}</li>" for b in bullets)
        groups.append(f"<li><b>{esc(label)}</b><ul>{subs}</ul></li>")
    parts.append('<section class="exec"><h2>Executive summary</h2><ul>'
                 + "".join(groups) + "</ul></section>")
    # KPI tiles
    tiles = []
    for (val, label, delta) in content.get("kpis", []):
        d = (f'<div class="delta up">▲ {esc(delta.lstrip("▲ "))}</div>'
             if delta else "")
        tiles.append(f'<div class="kpi"><div class="val">{esc(val)}</div>'
                     f'<div class="lbl">{esc(label)}</div>{d}</div>')
    if tiles:
        parts.append('<div class="kpis">' + "".join(tiles) + "</div>")
    # numbered sections
    for i, sec in enumerate(content["sections"], start=1):
        parts.append("<section>")
        parts.append(f'<h2><span class="num">{i}.</span>{esc(sec["title"])}</h2>')
        parts.append(f"<p><strong>{esc(sec['headline'])}</strong></p>")
        if sec.get("left_title"):
            parts.append(f"<p style=\"font-weight:600;color:var(--brand);margin:12px 0 4px\">{esc(sec['left_title'])}</p>")
        if sec.get("body"):
            parts.append(_bullets_html(sec["body"]))
        kind = sec["kind"]
        if kind == "chart":
            cid = f"chart{len(charts) + 1}"
            charts.append((cid, chart_option(sec["chart"])))
            cap = sec.get("chart_title", "")
            illus = " · ILLUSTRATIVE" if sec.get("illustrative") else ""
            parts.append(f'<figure><div id="{cid}" class="chart"></div>'
                         f'<figcaption>{esc(cap)} · Source: {esc(sec.get("source",""))}{illus}</figcaption></figure>')
        elif kind == "mekko":
            parts.append(_mekko_html(sec))
            cap = sec.get("chart_title", "")
            illus = " · ILLUSTRATIVE" if sec.get("illustrative") else ""
            parts.append(f'<figcaption>{esc(cap)} · Source: '
                         f'{esc(sec.get("source",""))}{illus}</figcaption>')
        elif kind == "harvey":
            parts.append(_harvey_table(sec))
            parts.append(_source_line(sec.get("source", "")))
        elif kind == "driver_tree":
            parts.append(_driver_tree_html(sec))
            parts.append(_source_line(sec.get("source", "")))
        elif kind == "positioning":
            parts.append(_positioning_html(sec))
            parts.append(_source_line(sec.get("source", "")))
        elif kind == "heatmap":
            parts.append(_heatmap_html(sec))
            parts.append(_source_line(sec.get("source", "")))
        elif kind == "revenue_build":
            parts.append(_revenue_build_html(sec))
            parts.append(_source_line(sec.get("source", "")))
        parts.append(_insight_html(sec.get("so_whats", []), sec.get("watchout")))
        if kind not in ("chart", "mekko", "harvey", "driver_tree", "positioning",
                        "heatmap", "revenue_build"):
            parts.append(_source_line(sec.get("source", "")))
        parts.append("</section>")
    # sources & confidence
    rows = []
    for (src, conf, note) in content["sources"]:
        rows.append(f'<tr><td>{esc(src)}</td><td><span class="cf cf-{conf}">{conf}</span></td>'
                    f"<td>{esc(note)}</td></tr>")
    parts.append('<section><h2><span class="num">'
                 f'{len(content["sections"]) + 1}.</span>Sources &amp; confidence</h2>'
                 '<table><thead><tr><th>Source</th><th>Conf.</th><th>Note</th></tr></thead>'
                 '<tbody>' + "".join(rows) + '</tbody></table></section>')
    # footer
    parts.append('<div class="footer"><span class="logo" aria-hidden="true"></span>'
                 f'<span>Prepared with Aqmen</span><span class="spacer">Confidential · {YEAR}</span></div>')
    parts.append("</div>")  # .page

    chart_js = "\n".join(
        f"aqChart({json.dumps(cid)}, {json.dumps(opt)});" for cid, opt in charts)
    return "\n".join(parts), chart_js


def build_html(content):
    head, helpers, scenario_js = shell_parts(content["title"])
    charts = []
    body, chart_js = build_body(content, charts)
    return (head + "\n<body>\n" + body + "\n<script>\n" + helpers + "\n\n"
            + chart_js + "\n\n" + scenario_js + "\n</script>\n</body>\n</html>\n")


def main():
    for module, content in MODULES.items():
        name = f"{module}-report-template.html"
        out = os.path.join(SHARED, name)
        open(out, "w", encoding="utf-8").write(build_html(content))
        print(f"wrote {name}")


if __name__ == "__main__":
    main()
