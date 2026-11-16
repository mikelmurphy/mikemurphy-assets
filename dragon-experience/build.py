import re, sys
from bs4 import BeautifulSoup

SRC = "/home/claude/build/plan_v28.html"
from summary import SUMMARY_CSS, SUMMARY_HTML
OUT = "/home/claude/build/dragon.html"

CSS = r"""
:root {
  --forest: #1E3A2B; --forest2: #2C4E3A; --gold: #A8873E; --cream: #F6F2E7;
  --rule: #D8D3C4; --ink: #1A1A18; --muted: #6E6A60;
}
*, *::before, *::after { box-sizing: border-box; }

@page {
  size: A4; margin: 20mm 18mm;
  @bottom-center { content: counter(page); font-family: "Montserrat", sans-serif; font-size: 7pt; color: var(--muted); letter-spacing: .08em; }
  @bottom-left  { content: "VILAGOZD HOLDINGS LIMITED · CO. NO. 17109348"; font-family: "Montserrat", sans-serif; font-size: 6.2pt; color: var(--muted); letter-spacing: .07em; }
  @bottom-right { content: "CONFIDENTIAL"; font-family: "Montserrat", sans-serif; font-size: 6.2pt; color: var(--muted); letter-spacing: .12em; }
}
@page :first { @bottom-left { content: ""; } @bottom-center { content: ""; } @bottom-right { content: ""; } }

body { font-family: "Cormorant Garamond", "Liberation Serif", serif; font-size: 9.6pt;
  line-height: 1.52; color: var(--ink); margin: 0; font-weight: 400;
  font-variant-numeric: lining-nums tabular-nums; }
p { margin: 0 0 6pt 0; text-align: justify; }
strong { font-weight: 700; color: var(--forest); }

.masthead { display: flex; justify-content: space-between; align-items: flex-end;
  border-bottom: 1.6pt solid var(--forest); padding-bottom: 5pt; margin-bottom: 16pt; }
.masthead img.wm { height: 34pt; width: auto; display: block; margin-bottom: 2pt; }
.wordsub { font-family: "Montserrat", sans-serif; font-size: 5.9pt; color: var(--muted);
  letter-spacing: .34em; margin-top: 3pt; border-top: .6pt solid var(--rule); padding-top: 3pt; }
.meta { font-family: "Montserrat", sans-serif; font-size: 6.4pt; color: var(--muted);
  letter-spacing: .13em; text-align: right; line-height: 1.7; }

h1.doctitle { font-size: 23pt; font-weight: 700; color: var(--forest); margin: 0 0 2pt 0; line-height: 1.1; }
.subtitle { font-style: italic; font-size: 11pt; color: var(--forest2); margin: 0 0 14pt 0; }
h2 { font-family: "Montserrat", sans-serif; font-size: 11.2pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: .055em; color: var(--forest); border-left: 3.4pt solid var(--gold);
  padding: 1pt 0 1pt 8pt; margin: 20pt 0 9pt 0; page-break-after: avoid; }
h3 { font-family: "Montserrat", sans-serif; font-size: 8.5pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: .07em; color: var(--forest2); margin: 13pt 0 5pt 0; page-break-after: avoid; }
h4 { font-size: 10.4pt; font-weight: 700; color: var(--forest); margin: 10pt 0 4pt 0; page-break-after: avoid; }

table { width: 100%; border-collapse: collapse; margin: 7pt 0 8pt 0; font-size: 8.9pt;
  page-break-inside: avoid; table-layout: fixed; }
thead th { font-family: "Montserrat", sans-serif; font-size: 7.6pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: .055em; background: var(--forest); color: #fff; text-align: left;
  padding: 4.5pt 6pt; vertical-align: bottom; }
tbody td { padding: 4pt 6pt; border-bottom: .55pt solid var(--rule); vertical-align: top; }
tbody tr:nth-child(even) td { background: #FBFAF6; }
td.num { text-align: right; font-variant-numeric: lining-nums tabular-nums; white-space: nowrap; }
th.num { text-align: right; white-space: normal; }
tr.total td { background: var(--cream); font-weight: 700; color: var(--forest);
  border-top: 1pt solid var(--forest); border-bottom: 1pt solid var(--forest); }
tr.sub td { background: #EFEDE4; font-weight: 700; color: var(--forest2); }
table.kv thead { display: none; }
table.kv td:first-child { font-weight: 700; color: var(--forest); }
table.long { page-break-inside: auto; }
table.long tr { page-break-inside: avoid; }
thead { display: table-header-group; }

.callout { background: var(--cream); border-left: 3.4pt solid var(--forest); padding: 8pt 11pt;
  margin: 9pt 0; page-break-inside: avoid; }
.callout.warn { border-left-color: var(--gold); }
.callout .h { font-family: "Montserrat", sans-serif; font-size: 7.4pt; font-weight: 700;
  text-transform: uppercase; letter-spacing: .1em; color: var(--forest); margin-bottom: 5pt; }
.callout.warn .h { color: #7A5F1F; }
.callout p:last-child { margin-bottom: 0; }

.src { font-size: 7.4pt; font-style: italic; color: var(--muted); margin: -3pt 0 9pt 0; }
figure { margin: 9pt 0 11pt 0; page-break-inside: avoid; }
figure img { width: 100%; height: auto; display: block; border-bottom: 2pt solid var(--gold); }
figure figcaption { font-size: 7.8pt; font-style: italic; color: var(--muted); margin-top: 4pt;
  text-align: center; line-height: 1.35; }
.figrow { margin: 9pt 0 11pt 0; page-break-inside: avoid; font-size: 0; text-align: center; }
.figrow figure.half { width: calc((100% - 30px) / 2); display: inline-block; vertical-align: top; margin: 0 30px 0 0; }
.figrow figure.half.last { margin-right: 0; }
.figrow figure.half figcaption { min-height: 20pt; }

ul { margin: 4pt 0 7pt 0; padding-left: 13pt; }
li { margin-bottom: 2.5pt; }
.pb { page-break-before: always; }
.endnote { border-top: .6pt solid var(--rule); margin-top: 16pt; padding-top: 7pt;
  font-size: 7.4pt; font-style: italic; color: var(--muted); line-height: 1.5; }
.endnote p { text-align: left; margin-bottom: 4pt; }

/* document-specific additions, built on the canonical tokens */
.kicker { font-family: "Montserrat", sans-serif; font-size: 7pt; font-weight: 700; letter-spacing: .16em;
  color: var(--gold); margin: 26pt 0 8pt 0; text-align: left; }
.lead { font-size: 13pt; font-weight: 600; color: var(--forest); line-height: 1.3; margin: 0 0 10pt 0; text-align: left; }
.cover-hero { margin: 4pt 0 14pt 0; }
figure.portrait img { width: 46%; margin: 0 auto; }
figure.photo img { width: 80%; margin: 0 auto; }
ul.toc { list-style: none; padding-left: 0; columns: 2; column-gap: 24pt; margin: 6pt 0 10pt 0; }
ul.toc li { font-family: "Montserrat", sans-serif; font-size: 7.6pt; letter-spacing: .04em; color: var(--forest);
  border-bottom: .5pt solid var(--rule); padding: 3pt 0; margin: 0; break-inside: avoid; }
ul.toc a { color: var(--forest); text-decoration: none; }
a { color: var(--forest2); text-decoration: none; }
"""

s = BeautifulSoup(open(SRC, encoding="utf-8"), "html.parser")

def clean(t):
    return re.sub(r"\s+", " ", t).strip()

# 1. drop empty tables
for t in s.find_all("table"):
    if not clean(t.get_text()) and not t.find("img"):
        t.decompose()

# 2. callouts: one-column tables
for t in list(s.find_all("table")):
    rows = t.find_all("tr")
    cols = max(len(r.find_all(["td", "th"])) for r in rows) if rows else 0
    if cols != 1:
        continue
    cell = t.find(["th", "td"])
    st = cell.find("strong")
    head = clean(st.get_text()) if st else ""
    if st:
        st.decompose()
    div = s.new_tag("div", attrs={"class": "callout" + (" warn" if head.startswith(("THE INVESTMENT TARGET", "SITE RULE", "FOUNDER PAY")) else "")})
    h = s.new_tag("div", attrs={"class": "h"}); h.string = head; div.append(h)
    body = clean(cell.decode_contents().replace("<br/>", " "))
    p = BeautifulSoup(f"<p>{body}</p>", "html.parser"); div.append(p)
    t.replace_with(div)

# 3. data tables: num cells, long tables, header bold cleanup
NUM = re.compile(r"^[−\-–+]?[€$£]?\s?[\d.,]+\s?(%|×|x|m|k|bn|€m|M)?$|^(n/a|—|–)$")
for t in s.find_all("table"):
    rows = t.find_all("tr")
    if len(rows) > 11:
        t["class"] = t.get("class", []) + ["long"]
    body_rows = t.find("tbody").find_all("tr") if t.find("tbody") else []
    ncols = max((len(r.find_all(["td","th"])) for r in rows), default=0)
    for c in range(ncols):
        cells = [r.find_all("td")[c] for r in body_rows if len(r.find_all("td")) > c]
        vals = [clean(x.get_text()) for x in cells if clean(x.get_text())]
        if c > 0 and vals and sum(bool(NUM.match(v)) for v in vals) / len(vals) >= 0.8:
            for x in cells: x["class"] = x.get("class", []) + ["num"]
            hr = t.find("thead")
            if hr:
                ths = hr.find_all("th")
                if len(ths) > c: ths[c]["class"] = ths[c].get("class", []) + ["num"]
    for r in body_rows:
        first = clean(r.get_text())[:12].upper()
        if first.startswith("TOTAL"):
            r["class"] = r.get("class", []) + ["total"]
    for th in t.find_all("th"):
        for st in th.find_all("strong"): st.unwrap()

# 4. headings: h2->h3, h1->h2
for h in s.find_all("h2"): h.name = "h3"
for h in s.find_all("h1"): h.name = "h2"
for h in s.find_all(["h2", "h3"]):
    for n in list(h.strings): n.replace_with(re.sub(r"\s+", " ", n))

# 5. images
def fig(src, cap, cls=None):
    f = s.new_tag("figure", attrs={"class": cls} if cls else {})
    f.append(s.new_tag("img", attrs={"src": src}))
    fc = s.new_tag("figcaption"); fc.string = cap; f.append(fc)
    return f

caps = {
 "image1.png": ("img/map_regional.jpg", "Regional context. The planned resort location in the Medvode area, Ljubljana Airport, the highway corridor and Ljubljana city centre.", "portrait"),
 "image2.png": ("img/map_locations.jpg", "The four location areas under test: the Railway Museum complex, the city centre (Museum of Illusions area), the former Tobacco Factory district and BTC City.", None),
 "image6.png": ("img/image6.png", "", None),
 "image3.png": ("img/image3.png", "", None),
 "image4.png": ("img/image4.png", "", None),
 "image5.png": ("img/image5.png", "", None),
}
for img in s.find_all("img"):
    key = img["src"].split("/")[-1]
    src, cap, cls = caps[key]
    f = fig(src, cap, cls)
    if not cap: f.figcaption.decompose()
    img.parent.replace_with(f)

# map source line
for p in s.find_all("p"):
    if clean(p.get_text()).startswith("The maps show approximate geographic positions"):
        p["class"] = "src"
        p.append(" Map imagery: Google Maps, ©2026 Google.")
        break

# 6. Meow Wolf photo, after first paragraph of "Why Meow Wolf is the main model"
for h in s.find_all("h3"):
    if clean(h.get_text()).startswith("Why Meow Wolf is the main model"):
        p = h.find_next_sibling("p")
        p.insert_after(fig("img/meowwolf.jpg", "Meow Wolf, House of Eternal Return, Santa Fe. The immersive walk-through benchmark: hand-built worlds, secret passages and story found by exploring. Photo: Meow Wolf.", "photo"))
        break

# 7. cover
els = s.find_all(recursive=False)
kicker, title, sub, lead, note = els[0:5]
kicker["class"] = "kicker"
title.name = "h1"; title["class"] = "doctitle"
title.clear(); title.append("Vilagozd"); title.append(s.new_tag("br")); title.append("The Dragon Experience")
sub["class"] = "subtitle"
lead["class"] = "lead"
note["class"] = "src"
kicker.insert_before(BeautifulSoup(SUMMARY_HTML, "html.parser"))
kicker["class"] = ["kicker", "pb"]
# "At a glance" table as key-value
for t in s.find_all("table"):
    if clean(t.get_text()).startswith("At a glance"):
        t.decompose(); break

# 8. TOC
for h in s.find_all("h2"):
    if clean(h.get_text()) == "What is in this plan":
        ul = s.new_tag("ul", attrs={"class": "toc"})
        sib = h.find_next_sibling()
        while sib is not None and not sib.find("a"): sib = sib.find_next_sibling()
        first_toc = None
        while sib is not None and sib.name == "p" and (sib.find("a") or not clean(sib.get_text())):
            nxt = sib.find_next_sibling()
            if sib.find("a"):
                li = s.new_tag("li")
                a = sib.find("a"); a.string = clean(a.get_text()); li.append(a); ul.append(li)
                if first_toc is None: first_toc = sib
                sib.decompose() if sib is not first_toc else None
            sib = nxt
        first_toc.replace_with(ul)
        break
for u in s.find_all("span", class_="underline"): u.unwrap()

# 9. page breaks before main chapters
BREAK = re.compile(r"^(\d+\. |Prove that enough|After Ljubljana|The first 90 days|Sources and what)")
for h in s.find_all("h2"):
    if BREAK.match(clean(h.get_text())):
        h["class"] = (h.get("class") or [])
        if isinstance(h["class"], str): h["class"] = [h["class"]]
        if "pb" not in h["class"]: h["class"].append("pb")

CSS = CSS + SUMMARY_CSS
one = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Vilagozd: The Dragon Experience. Investment Summary</title><style>{CSS}@page {{ @bottom-left {{ content: ""; }} @bottom-center {{ content: ""; }} @bottom-right {{ content: ""; }} }}</style></head><body>{SUMMARY_HTML}</body></html>'
open("/home/claude/build/onepager.html", "w", encoding="utf-8").write(one)
html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Vilagozd: The Dragon Experience. Investor Plan</title><style>{CSS}</style></head><body>{s.decode()}</body></html>'
open(OUT, "w", encoding="utf-8").write(html)
print("ok", len(html))
