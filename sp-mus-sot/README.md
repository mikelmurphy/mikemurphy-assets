# SP-MUS render kit (Dragon Museum strategic plan, v2.3, 21 Nov 2026)

This kit rebuilds the Dragon Museum strategic plan PDF from the source of truth. Words live in Supabase, numbers live in the fact register, and the PDF is only an output.

## Sources of truth (Supabase project lpvhexptckgwszexqjqs, table project_files)
- `projects/vilagozd-sot/docs/SP-MUS/TEXT.md`: tokenised text, v2.3 (99,851 chars, md5 d9ba3f2eeb14aa95ec47368ff12cc3fa)
- `projects/vilagozd-sot/docs/SP-MUS/LAYOUT.md`: layout spec with CSS and yaml machine spec (18,967 chars, md5 140fba80e6825f14c1a7c3915f735b49)
- `projects/vilagozd-sot/docs/SP-MUS/MANIFEST.json`: hashes, facts used, assets, render check
- `projects/vilagozd-sot/canon/FACT_REGISTER.md`: fact values (CR-2026-11-21-03 at v2.3)
- `projects/vilagozd-sot/assets/ASSET_REGISTER.md`: rows SP-MUS-A01 to A07

## Files here
- `render.py`: renders TEXT.md + LAYOUT.md + facts.json to PDF (pandoc, WeasyPrint, matplotlib, PyYAML, BeautifulSoup)
- `pagestarts.py`: QC, prints page count and the page each h2 section starts on (compare with LAYOUT expected_output)
- `base_css.css`: the CSS block of `knowledge/creative/vilagozd-pdf-stylesheet-v2.md`
- `facts.json`: snapshot of the register values used at CR-2026-11-21-03. Regenerate from FACT_REGISTER.md when a new CR is cut.
- `structure.json`: section anchors for pagestarts.py
- `img/`: assets. `meowwolf_cc.jpg` is CC BY 4.0 (ObscuraNomad, Wikimedia Commons); keep the caption credit. `map_locations_v2.jpg` has the label typos fixed.

## Rebuild
1. Install: pandoc, WeasyPrint, matplotlib, pyyaml, beautifulsoup4; Montserrat and Cormorant Garamond in ~/.fonts.
2. Download TEXT.md and LAYOUT.md from Supabase into a folder; put an updated facts.json there (one entry per key: `[value, unit]`).
3. Run: `SPMUS_DIR=<folder> python3 render.py <folder>/out.pdf "For <investor>"`
4. QC: `python3 pagestarts.py <folder>/out.pdf` must match LAYOUT expected_output (38 pages at v2.3). No em dashes. No investor terms (the plan is strategy only).
5. Write changes back to Supabase only after Mike says approve: snapshot to os_file_versions, update, log os_changelog.

## Rules carried in the text
- Strategy only: no investor repayment, ownership, conversion or buyout terms. Those live in separate investor documents.
- Return figures are current-model values until the 15% IRR rebuild (Museum v3.0) is registered.
- Never name the proposed Phase Zero investor.
