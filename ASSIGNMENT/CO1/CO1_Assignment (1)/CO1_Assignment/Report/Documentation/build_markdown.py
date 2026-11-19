"""Writes one Markdown answer file per task folder, generated from content.json (same text as the report)."""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
data = json.load(open(os.path.join(os.path.dirname(__file__), "content.json")))
FOLDERS = {1: "Task_1_Algorithm_Design", 2: "Task_2_Basic_Operation", 3: "Task_3_Mathematical_Complexity",
           4: "Task_4_Case_Analysis", 5: "Task_5_Asymptotic_Analysis", 6: "Task_6_Recurrence_Formulation",
           7: "Task_7_Recurrence_Solution", 8: "Task_8_Implementation_Testing", 9: "Task_9_Experimental_Performance",
           10: "Task_10_Theory_vs_Experiment", 11: "Task_11_Final_Recommendation", 12: "Task_12_Design_Challenge"}

def md_block(b):
    t = b["t"]
    if t in ("h1", "h2", "h3"):
        return "#" * {"h1": 2, "h2": 3, "h3": 4}[t] + " " + b["x"]
    if t == "p":
        return b["x"]
    if t == "bul":
        return "\n".join("- " + i for i in b["items"])
    if t == "code":
        return "```\n" + b["x"] + "\n```"
    if t == "table":
        head = "| " + " | ".join(b["head"]) + " |\n|" + "---|" * len(b["head"])
        body = "\n".join("| " + " | ".join(r) + " |" for r in b["rows"])
        return head + "\n" + body + "\n\n*" + b["caption"] + "*"
    if t == "img":
        rel = os.path.relpath(b["src"], os.path.join(ROOT, "Task_X"))
        return f"![{b['caption']}]({os.path.relpath(b['src'], ROOT)})\n\n*{b['caption']}*"
    return ""

blocks = data["blocks"]
for n, folder in FOLDERS.items():
    out = []
    for b in blocks:
        if b.get("task") == n:
            out.append(md_block(b))
    if not out:
        continue
    text = "\n\n".join(out) + "\n"
    path = os.path.join(ROOT, folder, f"Task_{n}_Answer.md")
    open(path, "w", encoding="utf-8").write(text)
    print("wrote", os.path.relpath(path, ROOT), len(text), "chars")
