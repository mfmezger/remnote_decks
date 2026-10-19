"""Check deck format, duplicate questions across decks, and README card counts."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARD = re.compile(r"^- (.+?) == (.+)$")
README_ROW = re.compile(r"^\| \[[^\]]+\]\((decks/[^)]+\.md)\) \|.*\| (\d+) \|$")


def normalize(question: str) -> str:
    return re.sub(r"[^a-z0-9^@]+", " ", question.lower()).strip()


def main() -> int:
    errors = []
    counts = {}
    seen = {}

    for path in sorted(ROOT.glob("decks/*/*.md")):
        rel = path.relative_to(ROOT).as_posix()
        lines = path.read_text().splitlines()
        if not lines or not lines[0].startswith("# Flashcards: "):
            errors.append(f"{rel}:1: first line must be '# Flashcards: ...'")
        counts[rel] = 0
        for n, line in enumerate(lines[1:], start=2):
            if not line or line.startswith("## "):
                continue
            match = CARD.match(line)
            if not match or line.count(" == ") != 1:
                errors.append(f"{rel}:{n}: not a '- Question == Answer' card")
                continue
            counts[rel] += 1
            key = normalize(match.group(1))
            if key in seen:
                errors.append(f"{rel}:{n}: duplicate question, first seen at {seen[key]}")
            else:
                seen[key] = f"{rel}:{n}"

    listed = {}
    for line in (ROOT / "README.md").read_text().splitlines():
        match = README_ROW.match(line)
        if match:
            listed[match.group(1)] = int(match.group(2))
    for rel, count in counts.items():
        if rel not in listed:
            errors.append(f"README.md: {rel} missing from the deck index")
        elif listed[rel] != count:
            errors.append(f"README.md: {rel} lists {listed[rel]} cards, deck has {count}")
    for rel in listed.keys() - counts.keys():
        errors.append(f"README.md: {rel} listed but does not exist")

    for error in errors:
        print(error)
    print(f"{len(counts)} decks, {sum(counts.values())} cards, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
