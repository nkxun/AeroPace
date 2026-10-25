"""Check every skills/*/SKILL.md against the Agent Skills spec (agentskills.io/specification)."""
import re, sys
from pathlib import Path

ok = True
for md in sorted(Path("skills").glob("*/SKILL.md")):
    text = md.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    errs = []
    if not m:
        errs.append("missing YAML front matter")
    else:
        f = dict(re.findall(r"^([a-z-]+):\s*(.*)$", m.group(1), re.M))
        name, desc = f.get("name", "").strip("\"'"), f.get("description", "").strip("\"'")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            errs.append(f"invalid name: {name!r}")
        if name != md.parent.name:
            errs.append(f"name {name!r} must match folder {md.parent.name!r}")
        if not desc or len(desc) > 1024:
            errs.append("description must be 1-1024 characters")
    if text.count("\n") > 500:
        errs.append("SKILL.md should stay under 500 lines")
    print(("FAIL " if errs else "ok   ") + str(md), *errs)
    ok &= not errs
sys.exit(0 if ok else 1)
