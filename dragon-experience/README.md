# The Dragon Experience: PDF build kit (V28, 16 Nov 2026)

Location: github.com/mikelmurphy/mikemurphy-assets, folder dragon-experience/. Fetch with git clone or the codeload tarball. Pointer: Supabase projects/vilagozd-integrated/ljubljana-dragon-experience-strategy-16nov2026/PDF_BUILD_KIT_MANIFEST_16NOV2026.md

Rebuilds two PDFs:
- Vilagozd-The-Dragon-Experience-Strategic-Plan-V28-16NOV2026.pdf (38 pages, investment summary as page 1)
- Vilagozd-The-Dragon-Experience-Investment-Summary-16NOV2026.pdf (1 page)

## Files in this folder
- build.py: turns plan_v28.html into dragon.html (strategy) and onepager.html, in the Vilagozd house style (stylesheet v2, inlined)
- summary.py: the page-1 investment summary (HTML + CSS). Edit figures here
- plan_v28.html: plan body text with the V28 figures already applied (pandoc output of the original .docx, whitespace normalised)
- revise.py: record of the V28 text edits. It reads norm.html (the normalised original), which is NOT stored; use it as an edit log only
- img/: the 8 images (raw files)

## Rebuild steps
1. mkdir -p /home/claude/build/img && cd /home/claude/build
2. Put build.py, summary.py and plan_v28.html in /home/claude/build (build.py reads /home/claude/build/plan_v28.html)
3. Copy img/ from this repo folder to /home/claude/build/img
4. pip install weasyprint --break-system-packages
5. Fonts: Montserrat[wght].ttf, Montserrat-Italic[wght].ttf, CormorantGaramond[wght].ttf and CormorantGaramond-Italic[wght].ttf from github.com/google/fonts (ofl/montserrat, ofl/cormorantgaramond) into ~/.fonts, then fc-cache -f
6. python3 build.py
7. python3 -m weasyprint dragon.html dragon.pdf && python3 -m weasyprint onepager.html onepager.pdf
8. Verify: no page xMax above 545pt (pdftotext -bbox), and all V28 values present

## Images
- map_regional.jpg / map_locations.jpg: Mike's annotated Google Maps images (credit: Google Maps, ©2026 Google). Labels misspell "Musuem"; fix in the source image
- meowwolf.jpg: Meow Wolf, House of Eternal Return. Third-party photo; licence or permission needed before external release
- image3.png: capital-call chart, redrawn for V28 (€1.07m first call)
- image4/5/6.png: charts from the original .docx
- wordmark.png: Vilagozd-Text__White_Backgroun_.eps via Ghostscript, polarity mean 0.753 (pass)

## V28 figures used (source: CFO founder and creator budget bridge, 16 Nov 2026)
Museum €5,067,767.86 = €5,000,000 + €67,767.86 creator allowance. First call €1,067,767.86.
IRR at 200K visits, €27, 6× sale: 16.52% (yr 5), 14.46% (yr 10), 13.86% (yr 15). 208K at €27.50: 15.10%. 215K at €28: 16.15%. 8×: 14.64%. No buyer: 10.65%.
15% thresholds: 210,709 visits (yr 15), 204,196 (yr 10), €28.51 ticket at 200K.
Founder pay outside the museum budget (Phase Zero €612,000, unfunded). Without P0: +€665,866.08 = €5,733,633.94.

## Open flags
1. Investor payout year 1 about €0.97M and payback in trading year 5 are derived from the plan's distributable-cash table at 70%; CFO to confirm
2. IRRs are shown to two decimals to match the CFO workbook (the house rule is one decimal)
3. Map label typos; Meow Wolf photo rights
4. Footer reads Vilagozd Holdings Limited · Co. No. 17109348; change it if the attraction sits in another entity
