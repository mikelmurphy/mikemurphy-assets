"""Apply V28 CFO bridge figures (16 Nov 2026) to the normalized plan HTML."""
h = open("/home/claude/build/norm.html", encoding="utf-8").read()

def rep(old, new, n=1):
    global h
    c = h.count(old)
    assert c == n, (c, old[:80])
    h = h.replace(old, new)

# Cover glance table rows
rep("<td>€5 million including staged additions and €750,000 of protected cash</td>",
    "<td>€5,067,767.86: the €5,000,000 attraction programme (including €750,000 protected cash) plus a €67,767.86 first-year creator content allowance</td>")
rep("Test a first-year paid-visitor case near 210,000 and potential",
    "210,709 first-year paid visits at €27 clears the 15% target with a year-15 sale; underwriting case 215,000 at €28; potential")

# Section 9 opening
rep("firm planning ceiling of €5 million for the full staged programme, including protected cash.",
    "revised planning ceiling of €5,067,767.86 for the full staged programme: the original €5,000,000 attraction budget, including protected cash, plus a €67,767.86 first-year creator content allowance.")

# Capital table: add creator row before total, update total
rep("<td>TOTAL INVESTMENT LIMIT</td> <td>€5,000,000</td> <td>No additional attraction money assumed outside the cap</td>",
    "<td>First-year creator content (weekly YouTube show, Feb 2027 to Jan 2028)</td> <td>€67,767.86</td> <td>Editor €23,214.29, tools €8,928.57, travel €26,785.71, 15% reserve €8,839.29. Unquoted; released against invoices. No founder salary</td> </tr> <tr class=\"even\"> "
    "<td>TOTAL INVESTMENT LIMIT</td> <td>€5,067,767.86</td> <td>No additional attraction money assumed outside the cap</td>")

rep("The modeled first cash call is €1 million: €250,000 for early site and market work and €750,000 for the protected cash reserve.",
    "The modeled first cash call is €1,067,767.86: €250,000 for early site and market work, €750,000 for the protected cash reserve and the €67,767.86 creator allowance. The creator money is called on day one in the model but paid to suppliers over 12 months against signed invoices. The €750,000 reserve is never used for videos or salaries.")

# Investment target callout
rep("To aim for a 15% annual return to the attraction investor at the full €5 million programme, we use about 210,000 first-year paying visits as a provisional attendance target. This is a sensitivity estimate, not an independently recalculated scenario or a proven ticket market.",
    "The target is a 15% annual return (IRR) to the attraction investor on the full €5,067,767.86 programme. At 200,000 first-year paid visits and a €27 average gross ticket, the model gives 13.86% with a sale after year 15, so the base case misses the target. Clearing 15% needs 210,709 first-year paid visits at €27, or 208,000 visits at €27.50 (15.10%). Our preferred underwriting case is 215,000 visits at €28 (16.15%). These are solver outputs from the CFO model, not a proven ticket market.")

# Founder pay disclosure + IRR table inserted before "What could change the result?"
rep('<h2 id="what-could-change-the-result">',
    '<table class="irr"><colgroup><col style="width:46%"/><col style="width:18%"/><col style="width:18%"/><col style="width:18%"/></colgroup><thead><tr><th>Investor return case (6× EBITDA sale unless stated)</th><th class="num">Sale after year 5</th><th class="num">Sale after year 10</th><th class="num">Sale after year 15</th></tr></thead><tbody>'
    '<tr><td>Base: 200,000 visits, €27 ticket, €5,067,767.86</td><td class="num">16.52%</td><td class="num">14.46%</td><td class="num">13.86%</td></tr>'
    '<tr><td>208,000 visits, €27.50 ticket</td><td class="num">n/a</td><td class="num">n/a</td><td class="num">15.10%</td></tr>'
    '<tr><td>Underwriting case: 215,000 visits, €28 ticket</td><td class="num">n/a</td><td class="num">n/a</td><td class="num">16.15%</td></tr>'
    '<tr><td>Base case, 8× EBITDA sale</td><td class="num">n/a</td><td class="num">n/a</td><td class="num">14.64%</td></tr>'
    '<tr><td>Base case, no buyer (distributions only)</td><td class="num">n/a</td><td class="num">n/a</td><td class="num">10.65%</td></tr>'
    '</tbody></table>'
    '<p class="src">Source: CFO founder and creator budget bridge, V28, 16 November 2026. Model outputs, not forecasts. 15% threshold at year 10: 204,196 paid visits at €27.</p>'
    '<table><colgroup><col style="width:100%"/></colgroup><thead><tr><th><strong>FOUNDER PAY IS NOT IN THE ATTRACTION BUDGET<br/></strong>'
    'Mike and Nastja are not paid from the €5,067,767.86. Their pay for the 36 months from February 2027 to January 2030 sits in the separate Phase Zero budget '
    '(€612,000 allowance against a current employer cost of €542,772.72), which is not yet funded. If the attraction is funded without Phase Zero, it needs a further '
    '€665,866.08 for founder pay and company overhead, taking it to €5,733,633.94. Any shared-team charge to the attraction will be reconciled so no person-month is paid twice.'
    '</th></tr></thead><tbody></tbody></table>'
    '<h2 id="what-could-change-the-result">')

# Call schedule
rep('>The complete €5 million investor call schedule<', '>The complete €5.07 million investor call schedule<')
rep("Investors approve a total €5 million ceiling", "Investors approve a total €5,067,767.86 ceiling")
rep("The first €1 million includes €750,000 of", "The first €1,067,767.86 includes €750,000 of")
rep("<td>Start / month 0</td> <td>€1,000,000</td> <td>€250k site and research; €750k restricted cash</td>",
    "<td>Start / month 0</td> <td>€1,067,767.86</td> <td>€250k site and research; €750k restricted cash; €67,767.86 creator content</td>")
rep("<td>€5,000,000</td> <td>Includes €750k protected reserve</td>",
    "<td>€5,067,767.86</td> <td>Includes €750k protected reserve</td>")

# Goal callouts
rep("support around 210,000 paid first-year visits and the planned average ticket price",
    "support at least 210,709 paid first-year visits at €27 (the 15% threshold), ideally the 215,000 at €28 underwriting case")
rep("legally clear €5m attraction funding plan", "legally clear €5.07m attraction funding plan")

# Sources
rep("supplies the €5m capital ceiling,", "supplies the €5m attraction capital,")
rep("investor cash-sharing rules and the 15% conditional return goal.",
    "investor cash-sharing rules and the 15% conditional return goal. The CFO founder and creator budget bridge (V28, 16 November 2026) adds the €67,767.86 creator allowance, the revised €5,067,767.86 ceiling, the founder-pay treatment and the return figures in section 9.")

open("/home/claude/build/plan_v28.html", "w", encoding="utf-8").write(h)
print("revised ok")
