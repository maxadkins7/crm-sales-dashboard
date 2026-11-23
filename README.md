# Revenue Studio — CRM Sales Dashboard

An interactive dashboard for exploring sales outcomes, team performance, product mix, and open opportunities using a historical CRM sample dataset. The dashboard connects account, product, sales-team, and opportunity records in one browser-based reporting experience.

**[Open the live dashboard](https://maxadkins7.github.io/crm-sales-dashboard/)**

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

Thirty sales agents have opportunity records in the supplied data. Engagement dates run from October 20, 2016 through December 27, 2017; recorded closes run from March 1 through December 31, 2017. The dashboard presents this historical snapshot, with open opportunities shown at their supplied status.

### Data preparation

- Join opportunity records to accounts by `account`, products by `product`, and team assignments by `sales_agent` in JavaScript when the dashboard loads.
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
- **CSV export** uses the global filters in every view. In Opportunities, it also applies the current search and stage selection and includes every matching record across all table pages.
- **Reset** clears the global filters, opportunity search, and stage selection.
- A segment without closed deals has no defined win rate and displays a dash.

### Interpretation limits

The stage chart shows the distribution of current record statuses; it is not a conversion funnel or a history of stage transitions. The data does not supply open-deal dollar values, quota, forecast probabilities, product quantities, or opportunity-creation dates. The dashboard does not estimate these fields. A won opportunity is a deal record, not a count of units sold.

Account annual revenue is a separate firmographic field measured in millions of USD. Catalog list prices are reference values and are not used to value open opportunities. Average time to win starts at engagement, rather than opportunity creation.

Q1 contains close records only for March 2017. Quarterly comparisons therefore cover unequal numbers of observed months. The data is a static sample; it does not establish current sales performance or a live forecast.

## Snapshot results

| Measure | Unfiltered result |
| --- | ---: |
| Total opportunities | 8,800 |
| Won revenue | $10,005,534 |
| Won opportunities | 4,238 |
| Lost opportunities | 2,473 |
| Open opportunities | 2,089 |
| Win rate | 63.2% |
| Average won deal | $2,360.91 |
| Average time to win | 51.8 calendar days |
| Opportunities without an assigned account | 1,425 |

In this sample:

- **GTX Pro** contributes the most won revenue at **$3,510,578**, or **35.1%** of the total.
- **West** leads regional won revenue at **$3,568,647**, or **35.7%** of the total.
- **1,425 opportunities (16.2%)** have no assigned account. All remain open in the supplied snapshot, limiting account and sector comparisons for that part of the pipeline.

These are descriptive findings from the supplied records.

## Technology

- HTML and CSS for the interface and responsive layout.
- JavaScript for joins, filters, aggregations, sorting, dialogs, and CSV export.
- Inline SVG for charts.
- Python 3 standard-library modules for rebuilding the portable HTML file.

The delivered `index.html` embeds its data and assets. It requires no external JavaScript or CSS, package installation, backend, or account connection.

## Run locally

Download and extract the repository, or clone it, then open the top-level **`index.html`** in a modern browser. The completed dashboard works offline and requires no local server or Python installation.

## Rebuild after editing the template or CSVs

The editable source is `dashboard.template.html`. The builder reads `accounts.csv`, `products.csv`, `sales_teams.csv`, and `sales_pipeline.csv` from `data/`; `data_dictionary.csv` documents the source fields.

After editing the template or those four source tables, run this command from the repository root:

```sh
python build_dashboard.py
```

If your system uses the `python3` command, run `python3 build_dashboard.py` instead. The script regenerates `index.html` in the repository root. Python is needed only for this rebuild; visitors opening the finished dashboard do not need Python.

The current interface and monthly chart are configured for the supplied 2016–2017 snapshot. To use a different date range, update the monthly chart logic and snapshot labels in `dashboard.template.html` as well as the data. Recalculate the figures and dates documented in this README after changing the source tables.

## Deployment

The dashboard is hosted on **GitHub Pages**: **[View the live dashboard](https://maxadkins7.github.io/crm-sales-dashboard/)**.

GitHub Pages serves the committed `index.html` from the root of `main`. After changing the template or source data, rebuild and commit the updated `index.html` to update the published dashboard.

## Validation

Checks reviewed on **November 23, 2026**:

- Compared the dashboard's JavaScript calculations with independent CSV calculations across nine scenarios, including product-name normalization, unassigned accounts, sector and manager filters, and empty filter intersections.
- Confirmed 8,800 unique opportunity IDs, successful joins for all nonempty account names and sales agents, and successful product joins after normalizing `GTXPro`.
- Recalculated record counts, date ranges, stage totals, revenue, win rate, average won deal, average time to win, product rankings, regional rankings, and all four quarter totals from the source CSVs.
- Confirmed that all four embedded data tables match the source CSVs and that rebuilding produces a byte-for-byte match of the committed `index.html`.
- Checked the published dashboard's four views, region and Q1 filtering, reset behavior, opportunity search and stage selection, record details, and methodology panel. Q1 shows 647 closed opportunities, including 531 wins and $1,134,672 in won revenue.
- Confirmed that an **Acme Corporation / Won** selection returns 34 opportunities across three table pages.

## Main project files

| Path | Purpose |
| --- | --- |
| `index.html` | Complete, runnable dashboard |
| `dashboard.template.html` | Editable interface and JavaScript source, with a data placeholder |
| `build_dashboard.py` | Embeds the source tables into the template |
| `data/` | Supplied sample CSVs and field dictionary |
| `.nojekyll` | Serves the static files directly with GitHub Pages |
| `.gitignore` | Excludes common Python and operating-system temporary files |

## Data credit

Dataset: **CRM Sales Opportunities**, distributed through [Maven Analytics Data Playground](https://mavenanalytics.io/data-playground/crm-sales-opportunities). The data source is credited separately from this dashboard implementation.
