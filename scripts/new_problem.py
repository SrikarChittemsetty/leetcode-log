from __future__ import annotations

import re
import shutil
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"
TEMPLATES_DIR = ROOT / "templates"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled-problem"


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/new_problem.py "Problem Title" [difficulty]')
        return 1

    title = sys.argv[1].strip()
    difficulty = sys.argv[2].strip().title() if len(sys.argv) > 2 else ""
    folder_name = f"{date.today().isoformat()}-{slugify(title)}"
    destination = PROBLEMS_DIR / folder_name

    if destination.exists():
        print(f"Problem folder already exists: {destination}")
        return 1

    destination.mkdir(parents=True)

    readme_template = (TEMPLATES_DIR / "problem-template.md").read_text()
    readme = (
        readme_template.replace("{{TITLE}}", title)
        .replace("- Difficulty:", f"- Difficulty: {difficulty}")
        .replace("- Date:", f"- Date: {date.today().isoformat()}")
    )
    (destination / "README.md").write_text(readme)
    shutil.copyfile(TEMPLATES_DIR / "solution.py", destination / "solution.py")
    shutil.copyfile(TEMPLATES_DIR / "alternatives.md", destination / "alternatives.md")

    print(f"Created {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

