# Aqmen Report Design System (shared)

The house look for aqmen output reports. All report types use this same system so
every deliverable is a consistent, executive-grade document. Start from this
skill's populated **`<module>-report-template.html`** example (it implements
everything below, filled with representative content) and replace the placeholder
content. (That example is generated from the canonical `report-template.html`
shell in `shared/`, which is the single source of the CSS/head/JS.)

> Shared verbatim across all aqmen report skills. Keep in sync via
> `scripts/sync-shared.mjs`.

## What a report is

An **executive deliverable**: it leads with the answer, surfaces insights and the
things to watch, and backs them with clean charts and a source trail. It is not a
data dump. Every section earns its place by informing a decision.

## Format & constraints

Reports render in a sandboxed, cross-origin iframe (the aqmen artifact viewer).

- **One `.html` file.** All CSS in an inline `<style>`; your JS inline in
  `<script>`.
- **Charts use ECharts, loaded from the cdnjs CDN** (see below) — the only
  permitted external resource. Everything else (data, styles, images) is inline;
  images as `data:` URIs.
- The template ships a `<meta http-equiv="Content-Security-Policy">` that allows
  scripts only from `cdnjs.cloudflare.com` plus inline — **don't loosen it** and
  don't add other external hosts.
- **Print-friendly** — consultants export to PDF. Keep the `@media print` rules.

## Charts — ECharts via cdnjs

The template already includes ECharts, pinned with an integrity hash. **Do not
change the include line:**

```html
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/echarts/6.0.0/echarts.min.js"
  integrity="sha512-4/g9GAdOdTpUP2mKClpKsEzaK7FQNgMjq+No0rX8XZlfrCGtbi4r+T/p5fnacsEC3zIAmHKLJUL7sh3/yVA4OQ=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer"
></script>
```

Render each chart into a sized `<div>` with `echarts.init(el)` + `setOption(...)`.
Guidelines:

- **Chart types by job:** line/area (time series), bar & grouped/stacked bar,
  **waterfall** (margin bridge — a transparent "base" series under visible
  deltas), **tornado** (sensitivity — horizontal diverging bars), **scatter**
  (positioning), **heatmap** (e.g. WACC × terminal sensitivity), **funnel**
  (TAM/SAM/SOM), gauge/pie sparingly.
- **Palette** (set `color: [...]` on the option) — the **blue-dominant brand
  ramp**, matching the deck: `#03045E, #0728A3, #2E6FD6, #6BAED6, #ADE8F3,
  #8A8A8A` (navy → blue → azure → steel → cyan → grey). No decorative orange or
  purple. Use one hue ramped light→dark for sequential/heatmap.
- **Always** set a title or `<figcaption>` with units and source, enable
  `tooltip`, and label axes. Keep `textStyle.fontFamily` matching the page.
- Make charts responsive: call `chart.resize()` on `window` resize.
- Don't rely on color alone — label series directly where practical.

## Layout

Centered column, `max-width: 900px`. Order: **cover → bottom line → executive
summary → numbered sections (each may carry an insight and/or watch-out) →
Sources & confidence.**

## Typography & color tokens

System font stack (no web fonts): `ui-sans-serif, -apple-system, "Segoe UI",
Roboto, Helvetica, Arial, sans-serif`. Base 15–16px, line-height ~1.6. Light,
document-like theme (reports print) — do not build a dark report.

```
--brand:#03045E;        /* Aqmen navy (matches the deck theme) — headings, brand bar, section numbers, KPI accents */
--brand-tint:#E9EBF7;   /* light navy wash for the bottom-line / insight panels */
--accent:#2E6FD6;       /* azure — secondary / links / interactive / accent */
--ink:#302E2E; --muted:#5b6472; --line:#DCE0EC; --bg:#ffffff;
--panel:#F2F3F7; --amber:#b7791f; --amber-bg:#fdf6e7; --good:#1e874b;
```

The **Aqmen navy leads** the look. Headings, section numbers, the bottom-line
block, and KPI accents are navy; the brighter accent is for links and one chart
series.

## Components (all in the template)

- **Brand bar** — the Aqmen logo mark + `Aqmen` wordmark (navy) and the report
  type. Plus a thin navy top bar and a **footer** (logo + "Prepared with Aqmen ·
  Confidential"). Keep the branding — don't strip the logo, bar, or footer.
- **Cover** — title (navy), one-line so-what subtitle, meta (project · date ·
  author · overall confidence).
- **Bottom line** — a prominent block near the top: the answer + the decision it
  informs + a confidence badge. The single most important element.
- **Executive summary** — 3–5 tight bullets.
- **KPI tiles** — big value, small label, optional delta (▲/▼ colored).
- **Insight callout** (accent left-border) — the "so-what" for a section.
- **Watch-out callout** (amber, ⚠) — things to scrutinize: low-confidence
  figures, the assumptions that most move the result, aggressive inputs, data
  gaps. Every report should surface a few.
- **Numbered section** — `1. Title` + body, optionally an insight/watch-out and a
  chart.
- **Scenario tabs** — buttons that switch a region between Base / bull / bear
  (vanilla JS `data-*` toggling; Base shown first).
- **Data table** — thin rules, muted header, `tabular-nums`.
- **Confidence badge** — 1–5 chip, color-graded (5 green … 1 red).
- **Sources & confidence table** — closing section: claim · source (type + URL) ·
  confidence · note.

## Do / don't

- **Do** keep the Aqmen brand bar / footer / logo / navy palette, lead with the
  bottom line, surface watch-outs, cite everything, keep it one file, use ECharts.
- **Don't** add external hosts beyond the pinned cdnjs ECharts, loosen the CSP,
  strip the branding, invent numbers, imply completeness, or ship a dark report.
