SUMMARY_CSS = r"""
.sum h1.doctitle { font-size: 21pt; margin-bottom: 1pt; }
.sum .subtitle { margin-bottom: 8pt; font-size: 10pt; }
.sum .intro { font-size: 9.4pt; margin-bottom: 9pt; }
.tiles { display: flex; gap: 6pt; margin: 0 0 10pt 0; }
.tile { flex: 1; background: var(--forest); color: #fff; padding: 7pt 8pt 7pt 8pt; border-bottom: 2.4pt solid var(--gold); }
.tile .k { font-family: "Montserrat", sans-serif; font-size: 5.8pt; letter-spacing: .12em; text-transform: uppercase; color: #D9CFA8; }
.tile .v { font-family: "Montserrat", sans-serif; font-size: 14pt; font-weight: 700; line-height: 1.15; margin: 2pt 0 1pt 0; }
.tile .s { font-size: 7.6pt; line-height: 1.25; color: #EDE8DA; }
.cols { display: flex; gap: 14pt; }
.cols > div { flex: 1; min-width: 0; }
.sum h3 { margin: 6pt 0 3pt 0; font-size: 7.6pt; }
.sum table { font-size: 7.9pt; margin: 2pt 0 5pt 0; }
.sum thead th { font-size: 6.4pt; padding: 3pt 5pt; }
.sum tbody td { padding: 2.4pt 5pt; }
.sum p.small, .sum li { font-size: 8.2pt; line-height: 1.36; }
.sum ul { margin: 1pt 0 4pt 0; padding-left: 10pt; }
.sum li { margin-bottom: 1.2pt; }
.sum .callout { padding: 5pt 8pt; margin: 4pt 0; }
.sum .callout p { font-size: 8.1pt; line-height: 1.35; text-align: left; }
.sum .fine { font-size: 6.6pt; font-style: italic; color: var(--muted); line-height: 1.35; margin-top: 5pt; border-top: .5pt solid var(--rule); padding-top: 3pt; text-align: left; }
"""

SUMMARY_HTML = r"""
<div class="sum">
<div class="masthead"><div><img class="wm" src="img/wordmark.png"/>
<div class="wordsub">THE DRAGON EXPERIENCE · LJUBLJANA</div></div>
<div class="meta">INVESTMENT SUMMARY<br/>CONFIDENTIAL INVESTOR DISCUSSION<br/>16 NOVEMBER 2026</div></div>

<h1 class="doctitle">The Dragon Experience</h1>
<p class="subtitle">A premium walk-through fantasy world in Ljubljana. The first Vilagozd business.</p>
<p class="intro">A 90 to 120-minute indoor attraction in a leased Ljubljana building, built in the spirit of Meow Wolf around Slovenia's dragon stories.
It earns money from tickets, a shop, optional paid add-ons and group events. It is a stand-alone business: no resort, hotel or licensing income is counted.</p>

<div class="tiles">
 <div class="tile"><div class="k">Total investment</div><div class="v">€5.07M</div><div class="s">€5,067,767.86, called in six gated stages</div></div>
 <div class="tile"><div class="k">Target investor return</div><div class="v">15% IRR</div><div class="s">Base case 16.52% / 14.46% / 13.86% with a sale after year 5 / 10 / 15</div></div>
 <div class="tile"><div class="k">Investor distributions</div><div class="v">70% → 20%</div><div class="s">70% of distributions until capital is returned, then 20%</div></div>
 <div class="tile"><div class="k">Timeline</div><div class="v">Feb 2029</div><div class="s">24-month build from Feb 2027; first trading year to Jan 2030</div></div>
</div>

<div class="cols">
<div>
<h3>Use of funds</h3>
<table><colgroup><col style="width:66%"/><col style="width:34%"/></colgroup>
<thead><tr><th>Item</th><th class="num">EUR</th></tr></thead><tbody>
<tr><td>Opening art, effects, fit-out and equipment</td><td class="num">3,410,000.00</td></tr>
<tr><td>Protected cash reserve (never spent on build, video or pay)</td><td class="num">750,000.00</td></tr>
<tr><td>Year 2: Pust realm and Iskra device</td><td class="num">590,000.00</td></tr>
<tr><td>Year 3: optional dragon thrill</td><td class="num">250,000.00</td></tr>
<tr><td>First-year creator content (weekly YouTube show)</td><td class="num">67,767.86</td></tr>
<tr class="total"><td>Total</td><td class="num">5,067,767.86</td></tr>
</tbody></table>

<h3>Capital calls (released only when each gate is met)</h3>
<table><colgroup><col style="width:66%"/><col style="width:34%"/></colgroup>
<thead><tr><th>When</th><th class="num">EUR</th></tr></thead><tbody>
<tr><td>Month 0: site, research, reserve, creator</td><td class="num">1,067,767.86</td></tr>
<tr><td>Month 6: design, engineering, lease</td><td class="num">450,000.00</td></tr>
<tr><td>Month 12: construction and installation</td><td class="num">1,650,000.00</td></tr>
<tr><td>Month 18: completion and opening</td><td class="num">1,060,000.00</td></tr>
<tr><td>Trading year 2: Pust and Iskra</td><td class="num">590,000.00</td></tr>
<tr><td>Trading year 3: dragon thrill (optional)</td><td class="num">250,000.00</td></tr>
</tbody></table>

<h3>How investors get paid</h3>
<ul>
<li>Bills, tax, repairs and reserves are paid first. The model then distributes 75% of free cash flow.</li>
<li>The investor receives 70% of distributions until its funded capital is returned, then 20%.</li>
<li>On a sale, unpaid investor capital is returned first, then the residual split applies.</li>
<li>Year 1 model: €1.38M distributable, so about €0.97M to the investor. Capital is returned during trading year 5 (estimate from the model's distributable cash).</li>
</ul>
</div>

<div>
<h3>Return to the investor (IRR)</h3>
<table><colgroup><col style="width:58%"/><col style="width:14%"/><col style="width:14%"/><col style="width:14%"/></colgroup>
<thead><tr><th>Case, 6× EBITDA sale</th><th class="num">Yr 5</th><th class="num">Yr 10</th><th class="num">Yr 15</th></tr></thead><tbody>
<tr><td>Base: 200K visits, €27 ticket</td><td class="num">16.52%</td><td class="num">14.46%</td><td class="num">13.86%</td></tr>
<tr><td>208K visits, €27.50</td><td class="num"></td><td class="num"></td><td class="num">15.10%</td></tr>
<tr><td>Underwriting: 215K visits, €28</td><td class="num"></td><td class="num"></td><td class="num">16.15%</td></tr>
<tr><td>Base, 8× EBITDA sale</td><td class="num"></td><td class="num"></td><td class="num">14.64%</td></tr>
<tr><td>Base, no buyer</td><td class="num"></td><td class="num"></td><td class="num">10.65%</td></tr>
</tbody></table>
<div class="callout warn"><div class="h">What it takes to reach 15%</div>
<p>210,709 first-year paid visits at €27 (sale after year 15), or 204,196 (sale after year 10). At 200,000 visits the ticket would need to be €28.51.</p></div>

<h3>Year 1 operating model (200K visits)</h3>
<table><colgroup><col style="width:66%"/><col style="width:34%"/></colgroup><tbody>
<tr><td>Net sales after VAT</td><td class="num">€6.32M</td></tr>
<tr><td>EBITDA</td><td class="num">€2.53M</td></tr>
<tr><td>Free cash flow after tax and capex</td><td class="num">€1.84M</td></tr>
<tr><td>Year 15 EBITDA (2% annual visit growth)</td><td class="num">€3.50M</td></tr>
</tbody></table>

<h3>Not included in the €5.07M</h3>
<ul>
<li>Founder pay. It sits in the separate, unfunded Phase Zero budget. Without Phase Zero, add €665,866.08 (total €5,733,633.94).</li>
<li>Bank debt, food and drink sales, school grants, licensing or second sites.</li>
</ul>

<h3>Status and main risks</h3>
<ul>
<li>No site, lease, supplier quotes or demand study yet. Legal terms unsigned.</li>
<li>Risks: attendance, ticket yield, build cost, and no guaranteed buyer.</li>
</ul>
</div>
</div>
<p class="fine">All figures are CFO model outputs (V26 base, V28 bridge, 16 November 2026), not forecasts, offers or guarantees. IRR depends on the signed investor terms, timing and a hypothetical sale. Full detail: The Dragon Experience strategic plan, section 9.</p>
</div>
"""
