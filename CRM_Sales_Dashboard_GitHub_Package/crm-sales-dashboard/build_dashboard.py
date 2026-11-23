"""Embed the supplied CRM tables into a portable, dependency-free HTML dashboard."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'data'
TABLES = {
    'accounts': 'accounts.csv',
    'products': 'products.csv',
    'teams': 'sales_teams.csv',
    'opportunities': 'sales_pipeline.csv',
}
data = {}
for name, filename in TABLES.items():
    with (SOURCE / filename).open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.reader(stream)
        columns = next(reader)
        data[name] = {'columns': columns, 'rows': list(reader)}

payload = json.dumps(data, separators=(',', ':'), ensure_ascii=False).replace('<', '\\u003c')
template = (ROOT / 'dashboard.template.html').read_text(encoding='utf-8')
assert template.count('/*__CRM_DATA__*/') == 1
html = template.replace('/*__CRM_DATA__*/', payload)
(ROOT / 'index.html').write_text(html, encoding='utf-8')
print(f'Embedded {len(data["opportunities"]["rows"]):,} opportunities in {len(html.encode()):,} bytes.')
