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

_BALLS = {0.0: "○", 0.25: "◔", 0.5: "◑", 0.75: "◕", 1.0: "●"}


def _ball(fill):
    q = round(max(0.0, min(1.0, fill)) * 4) / 4
    return _BALLS[q]


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
            f'<td style="text-align:center;font-size:18px;color:var(--brand)">{_ball(v)}</td>'
            for v in cells)
        body.append(f"<tr><td><b>{esc(label)}</b></td>{tds}</tr>")
    return ("<table><thead>" + head + "</thead><tbody>"
            + "".join(body) + "</tbody></table>")


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
        if kind in ("chart", "mekko"):
            cid = f"chart{len(charts) + 1}"
            opt = chart_option(sec["chart"]) if kind == "chart" else mekko_option(sec["mekko"])
            charts.append((cid, opt))
            cap = sec.get("chart_title", "")
            illus = " · ILLUSTRATIVE" if sec.get("illustrative") else ""
            parts.append(f'<figure><div id="{cid}" class="chart"></div>'
                         f'<figcaption>{esc(cap)} · Source: {esc(sec.get("source",""))}{illus}</figcaption></figure>')
        elif kind == "harvey":
            parts.append(_harvey_table(sec))
            parts.append(_source_line(sec.get("source", "")))
        parts.append(_insight_html(sec.get("so_whats", []), sec.get("watchout")))
        if kind not in ("chart", "mekko", "harvey"):
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
