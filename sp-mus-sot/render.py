"""Render SP-MUS from TEXT.md + LAYOUT.md + fact values. Usage: render.py out.pdf ["For <investor>"]"""
import re, sys, json, subprocess, datetime, yaml
from bs4 import BeautifulSoup, NavigableString

import os
KIT = os.path.dirname(os.path.abspath(__file__))
D = os.environ.get("SPMUS_DIR", KIT)  # folder holding TEXT.md, LAYOUT.md, facts.json
text = open(f"{D}/TEXT.md", encoding="utf-8").read()
layout = open(f"{D}/LAYOUT.md", encoding="utf-8").read()
facts = json.load(open(f"{D}/facts.json"))
spec = yaml.safe_load(re.search(r"```yaml\n(.*?)```", layout, re.S).group(1))
override = re.search(r"```css\n(.*?)```", layout, re.S).group(1)
base = open(f"{KIT}/base_css.css").read()          # = stylesheet v2 CSS block
IMG = f"{KIT}/img"
ASSETS = {"img-vilagozd-wordmark": f"{IMG}/wordmark.png", "img-mus-map-regional": f"{IMG}/map_regional.jpg",
          "img-mus-map-locations": f"{IMG}/map_locations_v2.jpg", "img-mus-meowwolf": f"{IMG}/meowwolf_cc.jpg",
          "img-mus-design-sequence": f"{IMG}/image4.png", "img-mus-meowwolf-revenue-mix": f"{IMG}/image6.png",
          "chart-mus-gates": f"{D}/chart-mus-gates.png"}

# ---------- front matter ----------
fm = yaml.safe_load(re.match(r"---\n(.*?)\n---\n", text, re.S).group(1))
text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
text = re.sub(r"^# SP-MUS \|.*\n", "", text, flags=re.M)

# ---------- tokens ----------
def fmt(key, mode):
    v, unit = facts[key]
    if unit == "date":
        import datetime; d = datetime.date.fromisoformat(v); return f"{d.day} {d:%B %Y}"
    if unit == "USD":
        return f"US${int(round(v)):,}"
    if unit == "x":
        return f"{v:.2f}×"
    if unit == "EUR/USD":
        return f"{v:.2f}"
    if unit == "slots":
        return f"{int(v)}"
    if unit == "%":
        s = (f"{abs(v):.0f}%" if float(abs(v)).is_integer() else f"{abs(v):g}%") if mode == "pct0" else f"{abs(v):.2f}%"
        return ("−" if v < 0 else "") + s
    if unit in ("visits", "year", "years", "days", "people", "guests", "per hour", "keys"):
        return f"{int(round(v)):,}"
    if unit == "FTE":
        return f"{v:.2f}".rstrip("0").rstrip(".")
    if mode == "exact":
        return f"€{v:,.2f}"
    if abs(v) >= 1e9: s = f"{v/1e9:.2f}".rstrip("0").rstrip("."); return f"€{s}B"
    if abs(v) >= 1e6: s = f"{v/1e6:.2f}".rstrip("0").rstrip("."); return f"€{s}M"
    if abs(v) < 1000 and v != int(v): return f"€{v:,.2f}"
    return f"€{int(round(v)):,}"
used = set()
def tok(m):
    used.add(m.group(1)); return fmt(m.group(1), m.group(2))
text = re.sub(r"\{\{f:([a-z0-9_.]+)(?:\\?\|(\w+))?\}\}", tok, text)
text = re.sub(r"\[\[PENDING-FACT:[a-z0-9_.]+\]\]", "", text)
assert "{{f:" not in text

# ---------- chart from fact keys ----------
def chart():
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, numpy as np
    c = spec["charts"]["chart-mus-gates"]
    full = [facts[k][0] / 1e6 for k in c["series"]["Full"]["keys"]]
    lean = [facts[k][0] / 1e6 for k in c["series"]["Lean"]["keys"]]
    x = np.arange(len(full)); w = 0.38
    fig, ax = plt.subplots(figsize=tuple(c["size_in"]), dpi=c["dpi"])
    lg = [l.replace("{mus.full}", fmt("mus.full", None)).replace("{mus.lean}", fmt("mus.lean", None)) for l in c["legend"]]
    b1 = ax.bar(x - w/2, full, w, color=c["series"]["Full"]["color"], label=lg[0])
    b2 = ax.bar(x + w/2, lean, w, color=c["series"]["Lean"]["color"], label=lg[1])
    for bars in (b1, b2):
        for r_ in bars: ax.text(r_.get_x() + r_.get_width()/2, r_.get_height() + 0.03, f"€{r_.get_height():.2f}m", ha="center", fontsize=7.5, color="#1E3A2B")
    ax.set_xticks(x); ax.set_xticklabels([l.replace(" / ", "\n") for l in c["x_labels"]], fontsize=8.5)
    ax.set_ylabel(c["y_label"]); ax.set_ylim(0, c["y_max"])
    for s_ in ["top", "right"]: ax.spines[s_].set_visible(False)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left"); ax.grid(axis="y", color="#eeeeee"); ax.set_axisbelow(True)
    ax.set_title(c["title"], fontsize=9.5, loc="left", color="#1E3A2B")
    plt.tight_layout(); plt.savefig(ASSETS["chart-mus-gates"]); plt.close()
chart()

# ---------- split page 1 (s0) from the body ----------
i0 = text.index("## Museum strategy summary {#SP-MUS-s0}")
i1 = text.index("::: kicker")
s0_md, body_md = text[i0:i1], text[i1:]

def pandoc(md):
    return subprocess.run(["pandoc", "-f", "markdown+pipe_tables+fenced_divs+header_attributes+implicit_figures+link_attributes-smart",
                           "-t", "html5", "--wrap=preserve"], input=md, capture_output=True, text=True, check=True).stdout

def callouts(soup):
    for bq in soup.find_all("blockquote"):
        p = bq.find("p"); raw = p.decode_contents()
        m = re.match(r"\s*\[!(NOTE|RISK|HISTORICAL)\]\s*([^\n]*)\n?(.*)", raw, re.S)
        if not m: continue
        kind, head, rest = m.groups()
        cls = "callout" if kind == "NOTE" else "callout warn"
        if kind == "HISTORICAL": head = "HISTORICAL: " + head
        extra = "".join(str(x) for x in bq.find_all("p")[1:])
        new = BeautifulSoup(f'<div class="{cls}"><div class="h">{head}</div><p>{rest.strip()}</p>{extra}</div>', "html.parser")
        bq.replace_with(new)

def apply_table(t, ts):
    w = ts.get("widths") or []
    for c in t.find_all("colgroup"): c.decompose()
    for td in t.find_all(["td", "th"]):
        if td.has_attr("style"): del td["style"]
    if w:
        cg = BeautifulSoup('<colgroup>' + "".join(f'<col style="width:{x}%"/>' for x in w) + '</colgroup>', "html.parser")
        t.insert(0, cg)
    for r_i, tr in enumerate(t.find("tbody").find_all("tr", recursive=False), 1):
        tds = tr.find_all("td", recursive=False)
        for c in ts.get("num", []):
            if len(tds) >= c: tds[c-1]["class"] = ["num"]
        if r_i in ts.get("total_rows", []): tr["class"] = ["total"]
    if t.find("thead"):
        ths = t.find("thead").find_all("th")
        for c in ts.get("num", []):
            if len(ths) >= c: ths[c-1]["class"] = ["num"]
        if ts.get("hide_header"): t.find("thead").decompose()
    if ts.get("long"): t["class"] = ["long"]

def figures(soup):
    for fig in soup.find_all("figure"):
        img = fig.find("img"); aid = img["src"].split("asset:")[1]
        cfg = spec["images"][aid]
        img["src"] = ASSETS[aid]
        for a in ("alt", "title"):
            if img.has_attr(a) and a == "title": del img[a]
        if cfg["class"] in ("portrait", "photo"): fig["class"] = [cfg["class"]]
        cap = fig.find("figcaption")
        if cap and not cfg["caption"]: cap.decompose()

# ---------- body ----------
bs = BeautifulSoup(pandoc(body_md), "html.parser")
callouts(bs); figures(bs)
notes = {}
fli = bs.find_all("li", id=re.compile(r"^fn\d+$"))
if fli:
    box = fli[0].find_parent(["section", "div"]) or fli[0].find_parent("ol")
    for li in fli:
        for b in li.find_all("a", class_="footnote-back"): b.decompose()
        notes["#" + li["id"]] = li.find("p").decode_contents().strip()
    prev = box.find_previous_sibling("hr") if box.name == "ol" else None
    if prev: prev.decompose()
    box.decompose()
for a in bs.find_all("a", class_="footnote-ref"):
    a.replace_with(BeautifulSoup(f'<span class="fn">{notes[a["href"]]}</span>', "html.parser"))
for div in bs.find_all("div"):
    c = (div.get("class") or [None])[0]
    if c in ("kicker", "subtitle", "lead", "source", "fine"):
        p = div.find("p"); p["class"] = ["src" if c == "source" else c]; div.replace_with(p)
    elif c == "doctitle":
        h = bs.new_tag("h1"); h["class"] = ["doctitle"]
        lines = div.find("p").decode_contents().split("<br/>")
        for k, l in enumerate(lines):
            if k: h.append(bs.new_tag("br"))
            h.append(BeautifulSoup(l.strip(), "html.parser"))
        div.replace_with(h)
bs.find("p", class_="kicker")["class"] = ["kicker", "pb"]
for a in spec["page_break_before"]:
    h = bs.find(id=a); h["class"] = (h.get("class") or []) + ["pb"]
toc = bs.find(id="SP-MUS-s1").find_next(["ul", "ol"]); toc["class"] = ["toc"]
for t, ts in zip(bs.find_all("table"), spec["tables"]):
    apply_table(t, ts)
assert len(bs.find_all("table")) == len(spec["tables"]), (len(bs.find_all("table")), len(spec["tables"]))

# ---------- page 1 ----------
s0 = BeautifulSoup(pandoc(s0_md), "html.parser")
callouts(s0)
s0.find("h2").decompose()
sub = s0.find("div", class_="subtitle").find("p").decode_contents()
intro = s0.find("p", recursive=False)
tables = s0.find_all("table")
tiles_t = tables[0]
tiles = ""
for tr in tiles_t.find("tbody").find_all("tr"):
    k, v, n = [td.decode_contents() for td in tr.find_all("td")]
    tiles += f'<div class="tile"><div class="k">{k}</div><div class="v">{v}</div><div class="s">{n}</div></div>'
tiles_t.decompose()
p1 = {t["section"]: t for t in spec["first_page"]["tables"] if "section" in t}
def block(anchor):
    h = s0.find(id=anchor); parts = [h]
    for sib in h.find_next_siblings():
        if sib.name in ("h3",) or (sib.name == "div" and "fine" in (sib.get("class") or [])): break
        parts.append(sib)
    out = []
    for p_ in parts:
        if p_.name == "table" and anchor in p1: apply_table(p_, p1[anchor])
        if p_.name == "p" and anchor == "SP-MUS-s0-1": p_["class"] = ["small"]
        out.append(str(p_))
    return "".join(out)
cols = spec["first_page"]["columns"]
left = "".join(block(a) for a in cols["left"]); right = "".join(block(a) for a in cols["right"])
fine = s0.find("div", class_="fine").find("p").decode_contents()
d = datetime.date(2026, 11, 20)
meta = "<br/>".join(m.replace("{version}", str(fm["version"])).replace("{date_upper}", d.strftime("%d %B %Y").upper())
                    for m in spec["first_page"]["masthead"]["right_meta"])
page1 = f'''<div class="sum"><div class="masthead"><div><img class="wm" src="{ASSETS['img-vilagozd-wordmark']}"/>
<div class="wordsub">THE DRAGON MUSEUM · LJUBLJANA</div></div><div class="meta">{meta}</div></div>
<h1 class="doctitle">The Dragon Museum</h1><p class="subtitle">{sub}</p><p class="intro">{intro.decode_contents()}</p>
<div class="tiles">{tiles}</div><div class="cols"><div>{left}</div><div>{right}</div></div><p class="fine">{fine}</p></div>'''

# ---------- assemble ----------
who = sys.argv[2] if len(sys.argv) > 2 else "internal QC render"
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
stamp = f"VILAGOZD | SP-MUS v{fm['version']} | Canon {fm['canon_release']} | Models MUS-v2.4, PZ-V3.1 | Generated {now} | For {who} | Confidential"
page_css = f'''@page {{ @bottom-left {{ content: "{stamp}"; font-family: "Montserrat", sans-serif; font-size: 6.2pt; color: var(--muted); letter-spacing: .03em; width: 85%; }}
  @bottom-center {{ content: ""; }} @bottom-right {{ content: counter(page); font-family: "Montserrat", sans-serif; font-size: 7pt; color: var(--muted); }} }}
@page :first {{ @bottom-left {{ content: "{stamp}"; }} @bottom-right {{ content: ""; }} }}'''
html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Vilagozd: The Dragon Museum. Strategic Plan v{fm["version"]}</title><style>{base}\n{override}\n{page_css}</style></head><body>{page1}{bs.decode()}</body></html>'
open(f"{D}/render.html", "w", encoding="utf-8").write(html)
subprocess.run(["python3", "-m", "weasyprint", f"{D}/render.html", sys.argv[1]], check=True, capture_output=True)
json.dump(sorted(used), open(f"{D}/facts_used.json", "w"))
print("rendered", sys.argv[1], "| facts used", len(used))
