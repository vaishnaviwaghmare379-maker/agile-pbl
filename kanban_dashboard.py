"""
ShopEase Kanban Dashboard Generator
-----------------------------------
Reads stories.csv and creates dashboard.html (opens in your browser).

Usage:   python kanban_dashboard.py
Update:  edit the 'status' column in stories.csv, then run it again.
No extra libraries needed (Python 3.8+).
"""
import csv
import html
import webbrowser
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent
CSV_FILE = BASE / "stories.csv"
OUT_FILE = BASE / "dashboard.html"

COLUMNS = ["Backlog", "To Do", "In Progress", "In Review", "Done"]
PRIORITIES = ["High", "Medium", "Low"]
COL_COLORS = {"Backlog": "#8b949e", "To Do": "#2f81f7", "In Progress": "#d29922",
              "In Review": "#db61a2", "Done": "#8957e5"}
PRI_COLORS = {"High": "#e5484d", "Medium": "#f08c1a", "Low": "#2fa84f"}


def load_stories():
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        stories = list(csv.DictReader(f))
    for s in stories:
        if s["status"] not in COLUMNS:
            raise ValueError(f"{s['id']}: unknown status '{s['status']}'. Use one of {COLUMNS}")
        if s["priority"] not in PRIORITIES:
            raise ValueError(f"{s['id']}: unknown priority '{s['priority']}'. Use one of {PRIORITIES}")
    return stories


def kpi(label, value, color):
    return (f'<div class="kpi"><div class="kpi-v" style="color:{color}">{value}</div>'
            f'<div class="kpi-l">{label}</div></div>')


def status_bars(by_status, total):
    rows = ""
    for c in COLUMNS:
        n = by_status[c]
        pct = n / total * 100 if total else 0
        rows += (f'<div class="bar-row"><span class="bar-name">{c}</span>'
                 f'<div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;'
                 f'background:{COL_COLORS[c]}"></div></div><span class="bar-n">{n}</span></div>')
    return rows


def donut(by_pri, total):
    stops, start, legend = [], 0.0, ""
    for p in PRIORITIES:
        pct = by_pri[p] / total * 100 if total else 0
        stops.append(f"{PRI_COLORS[p]} {start:.2f}% {start + pct:.2f}%")
        start += pct
        legend += (f'<div class="lg"><span class="dot" style="background:{PRI_COLORS[p]}"></span>'
                   f'{p} <b>{by_pri[p]}</b></div>')
    return (f'<div class="donut" style="background:conic-gradient({", ".join(stops)})">'
            f'<div class="donut-hole">{total}<small>stories</small></div></div>'
            f'<div class="legend">{legend}</div>')


def board(stories):
    out = ""
    for c in COLUMNS:
        cards = ""
        for s in (x for x in stories if x["status"] == c):
            cards += (f'<div class="card" style="border-left-color:{PRI_COLORS[s["priority"]]}">'
                      f'<div class="card-id">{html.escape(s["id"])} &middot; #{html.escape(s["issue"])}</div>'
                      f'<div class="card-t">{html.escape(s["title"])}</div>'
                      f'<span class="tag" style="background:{PRI_COLORS[s["priority"]]}">{s["priority"]}</span></div>')
        n = sum(1 for x in stories if x["status"] == c)
        out += (f'<div class="col"><div class="col-h" style="border-bottom-color:{COL_COLORS[c]}">'
                f'{c} <span class="cnt">{n}</span></div>{cards}</div>')
    return out


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ShopEase Kanban Dashboard</title>
<style>
:root{--bg:#f6f8fa;--panel:#fff;--text:#1f2328;--muted:#656d76;--line:#d0d7de}
@media (prefers-color-scheme: dark){:root{--bg:#0d1117;--panel:#161b22;--text:#e6edf3;--muted:#8b949e;--line:#30363d}}
*{box-sizing:border-box}
body{margin:0;padding:24px;background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
h1{margin:0 0 4px;font-size:24px}.sub{color:var(--muted);margin-bottom:20px}
.grid{display:grid;gap:16px}
.kpis{grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}
.two{grid-template-columns:repeat(auto-fit,minmax(300px,1fr));margin-top:16px}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px}
.panel h2{font-size:15px;margin:0 0 14px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px;text-align:center}
.kpi-v{font-size:32px;font-weight:700}.kpi-l{color:var(--muted);font-size:13px}
.bar-row{display:flex;align-items:center;gap:10px;margin-bottom:10px;font-size:13px}
.bar-name{width:90px}.bar-track{flex:1;height:14px;background:var(--line);border-radius:7px;overflow:hidden}
.bar-fill{height:100%;border-radius:7px}.bar-n{width:24px;text-align:right;font-weight:600}
.donut-wrap{display:flex;align-items:center;gap:24px;flex-wrap:wrap}
.donut{width:150px;height:150px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.donut-hole{width:92px;height:92px;border-radius:50%;background:var(--panel);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:26px;font-weight:700}
.donut-hole small{font-size:11px;color:var(--muted);font-weight:400}
.lg{margin-bottom:8px;font-size:14px}.dot{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:8px}
.progress{height:18px;background:var(--line);border-radius:9px;overflow:hidden;margin-top:6px}
.progress div{height:100%;background:#2fa84f}
.board{display:grid;grid-template-columns:repeat(5,minmax(190px,1fr));gap:12px;overflow-x:auto;margin-top:16px;padding-bottom:8px}
.col{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px}
.col-h{font-weight:700;font-size:14px;padding-bottom:8px;margin-bottom:10px;border-bottom:3px solid}
.cnt{background:var(--line);border-radius:10px;padding:1px 8px;font-size:12px;margin-left:4px}
.card{background:var(--bg);border:1px solid var(--line);border-left:5px solid;border-radius:6px;padding:8px 10px;margin-bottom:8px}
.card-id{font-size:11px;color:var(--muted)}.card-t{font-size:13px;margin:2px 0 6px}
.tag{color:#fff;font-size:10px;padding:2px 7px;border-radius:9px}
footer{color:var(--muted);font-size:12px;margin-top:16px;text-align:center}
</style></head><body>
<h1>ShopEase Kanban Dashboard</h1>
<div class="sub">Agile Methodology PBL &middot; Online Shopping System</div>
<div class="grid kpis">{{KPIS}}</div>
<div class="grid two">
  <div class="panel"><h2>Stories by Status</h2>{{BARS}}</div>
  <div class="panel"><h2>Stories by Priority</h2><div class="donut-wrap">{{DONUT}}</div></div>
</div>
<div class="panel" style="margin-top:16px"><h2>Overall Progress: {{PCT}}% complete</h2>
<div class="progress"><div style="width:{{PCT}}%"></div></div></div>
<div class="board">{{BOARD}}</div>
<footer>Priority colors: red = High, orange = Medium, green = Low &middot; Generated from stories.csv</footer>
</body></html>"""


def main():
    stories = load_stories()
    total = len(stories)
    by_status = Counter(s["status"] for s in stories)
    by_pri = Counter(s["priority"] for s in stories)
    pct = round(by_status["Done"] / total * 100) if total else 0

    kpis = (kpi("Total Stories", total, "#2f81f7")
            + kpi("Done", by_status["Done"], "#8957e5")
            + kpi("In Progress + Review", by_status["In Progress"] + by_status["In Review"], "#d29922")
            + kpi("High Priority", by_pri["High"], "#e5484d")
            + kpi("Completion", f"{pct}%", "#2fa84f"))

    page = (TEMPLATE.replace("{{KPIS}}", kpis)
            .replace("{{BARS}}", status_bars(by_status, total))
            .replace("{{DONUT}}", donut(by_pri, total))
            .replace("{{PCT}}", str(pct))
            .replace("{{BOARD}}", board(stories)))
    OUT_FILE.write_text(page, encoding="utf-8")

    print("=== ShopEase Kanban Summary ===")
    for c in COLUMNS:
        print(f"{c:<12}: {by_status[c]}")
    print(f"Total       : {total}  |  Completion: {pct}%")
    print(f"Dashboard saved to: {OUT_FILE}")
    webbrowser.open(OUT_FILE.as_uri())


if __name__ == "__main__":
    main()
