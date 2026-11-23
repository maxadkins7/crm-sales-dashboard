# Revenue Studio — CRM Sales Dashboard

An interactive dashboard for exploring sales outcomes, team performance, product mix, and open opportunities using a historical CRM sample dataset. The dashboard connects account, product, sales-team, and opportunity records in one browser-based reporting experience.

**[Open the live dashboard](https://max-crm-revenue-studio.shiningbagel2.chatgpt.site/)**

The project uses [Maven Analytics’ CRM Sales Opportunities dataset](https://mavenanalytics.io/data-playground/crm-sales-opportunities). The records describe a fictitious computer-hardware business. This repository contains sample data; no employer or client business records are included.

## Purpose

The dashboard helps explore questions a sales manager might ask:

- How much revenue has been recorded from won opportunities?
- How do outcomes differ by region, manager, sales agent, and product?
- Which products contribute the most revenue, and how do their win rates compare?
- How many opportunities remain open in the supplied snapshot?
- How long do won opportunities take to move from engagement to close?
- Which opportunity records explain the summary metrics?

## Dashboard views

| View | What it shows |
| --- | --- |
| Overview | Revenue and win-rate KPIs, monthly won revenue, opportunity-stage distribution, leading products and agents, sales-cycle and account-coverage highlights |
| Sales team | Regional summaries, manager comparisons, and a sortable sales-agent leaderboard |
| Products | Revenue rankings, series contribution, product win rates, average won deals, reference list prices, and open opportunity counts |
| Opportunities | Searchable and sortable opportunity records, stage selection, pagination, record details, and CSV export |

Global filters cover close quarter, region, manager, product, and account sector. Product bars filter the dashboard; sales-agent links open that agent’s opportunity records. The interface includes responsive navigation, keyboard focus indicators, chart descriptions, metric definitions, and explicit handling of empty selections.

## Data

| File | Grain | Records |
| --- | --- | ---: |
| `data/sales_pipeline.csv` | One sales opportunity | 8,800 |
| `data/accounts.csv` | One account | 85 |
| `data/products.csv` | One product | 7 |
| `data/sales_teams.csv` | One sales-agent/team assignment | 35 |
| `data/data_dictionary.csv` | One documented field | 21 |

Thirty sales agents have opportunity records in the supplied data. Engagement dates run from October 2016 through December 2017; recorded closes run from March through December 2017. The dashboard represents this historical snapshot and does not connect to a live CRM.

### Data preparation

- Join opportunity records to accounts by `account`, products by `product`, and team assignments by `sales_agent`.
- Normalize the opportunity product name `GTXPro` to the catalog name `GTX Pro`.
- Display the account-sector spelling `technolgy` as `Technology`.
- Retain all 1,425 opportunities with a blank account name as **Unassigned account**.
- Preserve missing dates and close values. There are 2,089 open records without a close date or value, including 500 Prospecting records without an engagement date.
- Generate quarter-filter options from the recorded close dates. The supplied data provides `2017-Q1` through `2017-Q4`.
- Keep the source CSV files unchanged.

## Metric definitions

| Metric | Calculation |
| --- | --- |
| Won revenue | Sum of `close_value` for opportunities marked Won, in USD |
| Win rate | Won opportunities ÷ (Won + Lost opportunities) |
| Open opportunities | Count of Engaging + Prospecting records |
| Average won deal | Won revenue ÷ Won opportunities |
| Average time to win | Mean calendar days between `engage_date` and `close_date` for Won records with both dates |
| Monthly won revenue | Won revenue grouped by close month |

### Filter behavior

- **Full snapshot** includes all opportunity records, including undated open deals.
- **Close-quarter filters** use `close_date`, so undated open opportunities are excluded.
- **Search and stage selection** apply to the opportunity table and its CSV export. KPI cards retain their global-filter scope.
- **CSV export** includes every matching record, across all table pages.
- A segment without closed deals has no defined win rate and displays a dash.

### Interpretation limits

The stage chart shows the distribution of current record statuses; it is not a conversion funnel or a history of stage transitions. The data does not supply open-deal dollar values, quota, forecast probabilities, product quantities, or opportunity-creation dates. The dashboard does not estimate these fields. A won opportunity is a deal record, not a count of units sold.

Account annual revenue is a separate firmographic field measured in millions of USD. Catalog list prices are reference values and are not used to value open opportunities. Average time to win starts at engagement, rather than opportunity creation.

## Snapshot results

| Measure | Unfiltered result |
| --- | ---: |
| Won revenue | $10,005,534 |
| Won opportunities | 4,238 |
| Lost opportunities | 2,473 |
| Open opportunities | 2,089 |
| Win rate | 63.2% |
| Average won deal | $2,360.91 |
| Average time to win | 51.8 calendar days |

In this sample, GTX Pro contributes the most won revenue at $3,510,578. West is the leading region at $3,568,647. These are descriptive findings from the supplied records.

## Technology

- HTML and CSS for the interface and responsive layout.
- JavaScript for joins, filters, aggregations, sorting, dialogs, and CSV export.
- Inline SVG for charts.
- Python 3 standard-library modules for rebuilding the portable HTML file.

The delivered `index.html` embeds its data and assets. It requires no external JavaScript or CSS, package installation, backend, or account connection.

## Run locally

Download the repository and open **`index.html`** in a modern browser. It works offline.

## Rebuild after editing the template or CSVs

Edit `dashboard.template.html` or files in `data/`, then run:

```sh
python build_dashboard.py
```

If your system uses the `python3` command, run `python3 build_dashboard.py` instead. The script regenerates `index.html` in the repository root. Python is needed only for this rebuild; visitors opening the finished dashboard do not need Python.

## Publish with GitHub Pages

1. Put `index.html` and the other project files in the repository root.
2. Open **Settings → Pages** in the repository.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select **main** and **/(root)**, then save.
5. After deployment completes, use the website URL shown by GitHub. You can add it to the repository’s About section and use it as the live-demo link above.

GitHub’s [publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) explains these settings.

## Validation

- Compared dashboard calculations with independent CSV calculations across nine scenarios, including product-name normalization, missing accounts, and empty filter intersections.
- Checked each quarter selection and reset behavior in the browser. Q1 contains 647 closed opportunities, including 531 wins and $1,134,672 in won revenue.
- Checked search, stage selection, sorting, pagination, record details, metric definitions, and desktop/mobile navigation.
- Verified an Acme Corporation/Won export against the source data: all 34 matching records were included across three table pages.

## Repository contents

| Path | Purpose |
| --- | --- |
| `index.html` | Complete, runnable dashboard |
| `dashboard.template.html` | Editable interface and JavaScript source, with a data placeholder |
| `build_dashboard.py` | Embeds the source tables into the template |
| `data/` | Original sample CSVs and field dictionary |
| `.nojekyll` | Serves the static files directly with GitHub Pages |
| `.gitignore` | Excludes common Python and operating-system temporary files |

## Data credit

Dataset: **CRM Sales Opportunities**, distributed through [Maven Analytics Data Playground](https://mavenanalytics.io/data-playground/crm-sales-opportunities). The data source is credited separately from this dashboard implementation.
