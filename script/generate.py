import csv, os, pathlib

IN = "docs/industries.csv"
OUT = "docs/pages"
pathlib.Path(OUT).mkdir(parents=True, exist_ok=True)
HF = "<HF_LINK>"
GM = "<GUMROAD_LINK>"

with open(IN, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        slug = row["slug"]
        content = f"# {row['title']}\n"                   f"**Doc type:** {row['doc_type']}  \n"                   f"**Industry:** {row['industry']} | **Region:** {row['region']} | **Standards:** {row['standards']}\n\n"                   f"Use the free generator [{HF}]({HF})  \n"                   f"Need editable DOCX/PDF? [{GM}]({GM})\n\n"                   "## What you'll get\n"                   "- Scope & RACI  \n"                   "- Procedures step by step  \n"                   "- KPIs & Metrics  \n"                   "- Appendices (IOC, Timeline, Forms)\n"
        open(os.path.join(OUT, f"{slug}.md"), "w", encoding="utf-8").write(content)
