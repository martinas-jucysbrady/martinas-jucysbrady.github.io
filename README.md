# martinas-jucysbrady.github.io

Source code for my personal ePortfolio, built with [Quarto](https://quarto.org/), version-controlled with Git, and deployed via GitHub Pages.

🔗 **Live site:** [martinas-jucysbrady.github.io](https://martinas-jucysbrady.github.io)

---

## What's in here

A four-year academic portfolio combining business and data analytics work from Dublin City University and Kobe University, alongside personal sections for travel writing, books and software skills.

The site is fully reproducible; most charts on the project pages is generated from live Python code that runs at render time, so the visualisations update automatically when the underlying analysis changes.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Quarto** | Static site generator; renders `.qmd` files to HTML |
| **Python** | Live code execution for charts (matplotlib, plotly, pandas, scikit-learn) |
| **SCSS** | Custom theme on top of the Bootstrap `flatly` base |
| **Git + GitHub Pages** | Version control and hosting |
| **Leaflet** | Interactive travel map on `/travel` |
| **Mermaid** | Flowcharts and ERDs |
| **DataTables** | Sortable certifications table |
| **Font Awesome + Bootstrap Icons** | Icons throughout |

---

## Repository Structure

```
.
├── _quarto.yml                  # Site config — navbar, resources, theme
├── index.qmd                    # Landing page (about/trestles layout)
├── about.qmd                    # About page with year cards and skill tiles
├── projects.qmd                 # Project listing with filterable categories
├── books.qmd                    # Book reviews with star ratings
├── certificates.qmd             # Tabbed cert list with sortable Kubicle table
├── reflection.qmd               # Final reflection on the portfolio itself (In module tab in Year 4)
├── 404.qmd                      # Custom 404 page
├── .gitignore
├── .nojekyll
│
├── assets/                      # Static assets (CSS, fonts, files, images)
│   ├── custom.scss              # All site-wide custom styling
│   ├── mjb_favicon.png          # Favicon and navbar logo
│   ├── CV.pdf                   # Downloadable CV
│   ├── misc. files
│   ├── files/                   # Project PDFs and Tableau workbook
│   └── module_image/            # Module thumbnails for the year pages
│
├── projects/                    # Project pages (one folder each)
│   ├── business_analytics/      # Year 2 — banking case study (live Python)
│   ├── business_strategy/       # Year 4 — Siemens Healthineers consultancy
│   ├── data_analytics_pv/       # Year 4 — EcoEnergy Corp (live Python)
│   ├── digital_transformation/  # Year 4 — Revolut vs Ulster Bank essay
│   ├── global_group/            # Year 1 — Volkswagen AG group analysis
│   ├── international_economy/   # Year 3 — Trump policies & Mundell-Fleming
│   ├── KIMAP/                   # Year 3 — EU Commission consultancy report
│   ├── legal_system/            # Year 3 — Japanese criminal justice analysis
│   ├── life/                    # Year 1 — Applegreen group project
│   ├── ml_python/               # Year 4 — Brain tumour classification (live Python)
│   ├── portfolio_management/    # Year 3 — 6-week investment portfolio
│   └── psychology/              # Year 2 — Maslow & Herzberg essay
│
├── software/                    # Tool-specific skills pages (all live code)
│   ├── excel_progress.qmd       # Work done using Excel
│   ├── python_progress.qmd      # Work done using Python
│   ├── r_progress.qmd           # Work done using R
│   ├── sql_progress.qmd         # Work done using SQL
│   └── tableau_progress.qmd     # Work done using Tableau
│
├── studies/                     # Module breakdowns by year
│   ├── yearone/                 # DCU Year 1 modules
│   ├── yeartwo/                 # DCU Year 2 modules
│   ├── yearthree/               # Kobe Uni exchange modules
│   └── yearfour/                # DCU Year 4 modules
│
├── travel/                      # Travel writing — see breakdown below
│   ├── index.qmd
│   └── individual travel folders
│
├── docs/                        # Build output (served by GitHub Pages)
└── _extensions/
    └── quarto-ext/fontawesome/  # Font Awesome shortcode extension
```

---

## Travel Section — File Map

The travel section drills down by region. Each location page has its own folder with prose, image grids, and (for some) embedded videos hosted on GitHub Releases.

### Top level
- **`travel/index.qmd`** — Interactive Leaflet world map with click-to-drill regions, polaroid markers, and inset maps for Madeira and Okinawa.

### Europe — `travel/europe/`
- **`alg_anda/`** — Algarve & Andalusia (Lagos, Faro, Cádiz, Gibraltar, Málaga, Granada)
- **`balkans/`** — Croatia & Montenegro (Split, Dubrovnik, Budva, Perast)
- **`c_europe/`** — Central Europe (Budapest, Vienna, Bratislava)
- **`city_breaks/`** — Mixed European city trips (London, Edinburgh, Liverpool, Paris, Amsterdam, Madrid, Cologne, Venice, Rome)
- **`ireland/`** — Ulster, Leinster, Connacht
- **`madeira/`** — Madeira island (linked from Iberia inset on the main map)
- **`milan_nice/`** — Italy / France F1 trip (Milan, Como, Genoa, Monaco, Nice, Cannes) — **includes F1 race videos with click-to-unmute**
- **`switzerland/`** — Switzerland & Liechtenstein (Grindelwald, Vaduz)

### East Asia — `travel/e_asia/`
Japanese prefectural breakdown plus South Korea:
- **`hokkaido/`** — Sapporo, Otaru
- **`tohoku/`** — Iwate, Miyagi, Akita, Yamagata, Fukushima
- **`kanto/`** — Tokyo, Kanagawa, Chiba
- **`chubu/`** — Aichi, Nagano, Ishikawa, Fukui, Gifu, Mie, Shizuoka, Yamanashi
- **`kansai/`** — Osaka, Kyoto, Nara, Hyogo, Shiga, Wakayama
- **`chugoku_shikoku/`** — Hiroshima, Okayama, Tottori, Shimane, Tokushima, Ehime
- **`kyushu/`** — Fukuoka, Saga, Nagasaki, Kumamoto, Kagoshima, Miyazaki, Oita
- **`okinawa/`** — Okinawa (linked from East Asia inset)
- **`s_korea/`** — Seoul, Busan, Gyeongju

### Southeast Asia — `travel/se_asia/`
- Taipei, Hanoi, Ha Long Bay — **includes auto-playing Ha Long Bay drone videos and Hanoi Train Street**

### Australia — `travel/australia/`
- Busselton, Perth, Sydney — **includes Manly Ferry and Bondi videos hosted on GitHub Releases**

---

## Where the Live Code Runs

Pages with executable Python chunks (these regenerate on every build):

- `projects/business_analytics/index.qmd` — banking regression
- `projects/data_analytics_pv/index.qmd` — full EcoEnergy regional analysis
- `projects/ml_python/index.qmd` — ML pipeline, classifier comparison
- `software/excel_progress.qmd` — Sharpe ratio, efficient frontier, dashboards
- `software/python_progress.qmd` — NumPy/Pandas/Plotly demos plus PCA
- `software/r_progress.qmd` — econometrics replicated in Python
- `software/sql_progress.qmd` — SQLite running queries live in the page

---

## Niche Bits Worth Knowing

A few things that aren't obvious from a casual look at the repo:

- **Video assets** are stored as a tagged release (`v1.0-media`) on this repo rather than in the working tree, to keep the repo size manageable. The `<video>` tags reference the release URLs directly. Don't delete the release.
- **The travel map** (`travel/index.qmd`) uses inline JS rather than an external file. ~360 lines of Leaflet config, polaroid marker generation, region rectangles, and inset maps.
- **The `about.qmd` page** has a click-to-open language modal — Languages tile on the page expands a popup with flag icons and proficiency levels.
- **The `certificates.qmd` page** uses [DataTables](https://datatables.net/) for sortable column headers on the Kubicle list, loaded from CDN via `include-in-header`.
- **The Monaco F1/F2 videos** on `travel/europe/milan_nice/` are muted by default with a click-to-unmute icon overlay — the only travel page using that pattern.
- **The Tableau page** is text-only — Tableau workbooks don't embed in Quarto, so the actual `.twbx` is provided as a download.
- **Inline `<style>` blocks** appear at the top of most travel pages and skill pages. They override `_quarto.yml` defaults for that page only (mostly to constrain page width and reposition the TOC).
- **Module thumbnails** in `studies/yearone/index.qmd` etc. mix locally hosted (`/assets/module_image/`) and externally hosted images. The external ones are wrapped with `onerror="this.style.display='none'"` so they fail gracefully.

---

## Local Development

```bash
# Render everything once
quarto render

# Live preview — auto-rebuilds on save
quarto preview

# Render a single file
quarto render projects/ml_python/index.qmd
```

The preview server runs at `http://localhost:port` and watches for file changes.

---

## Deployment

GitHub Pages serves from the `docs/` folder on the `main` branch.

```bash
# After making changes
git add .
git commit -m "<descriptive message>"
git push

# GitHub Pages picks up the change in ~30 seconds
```

`.nojekyll` (empty file at repo root) tells GitHub Pages to skip Jekyll processing — Quarto's output goes straight through as-is.

---

## Author

**Martinas Jucys Brady**
Final-year BA Business Studies International — Dublin City University

📧 [martinas.jucysbrady2@mail.dcu.ie](mailto:martinas.jucysbrady2@mail.dcu.ie)
💼 [LinkedIn](https://www.linkedin.com/in/martinasjucysbrady/)

---

*Built with [Quarto](https://quarto.org/) · Managed with Git · Published on GitHub Pages*