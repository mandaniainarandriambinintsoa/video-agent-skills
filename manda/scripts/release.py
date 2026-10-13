"""Validate and package the allowlisted Markdown skills, with no network or install."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile

NAMES = (
    "manda-hyperframes-production",
    "manda-hyperframes-review",
    "manda-video-reference",
)
ROOT = Path(__file__).resolve().parents[2]


def payload(root=ROOT):
    source = root / "manda" / "skills"
    if {p.name for p in source.iterdir()} != set(NAMES):
        raise ValueError("Unexpected skill entry")
    result = {}
    for name in NAMES:
        folder = source / name
        if folder.is_symlink() or not folder.is_dir():
            raise ValueError("Invalid skill directory")
        main = (folder / "SKILL.md").read_text(encoding="utf-8")
        if not main.startswith("---\nname: " + name + "\n"):
            raise ValueError("Skill name/frontmatter mismatch")
        if not re.search(r"^description: .+", main, re.M):
            raise ValueError("Missing description")
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise ValueError("Symlink forbidden")
            if path.is_dir():
                continue
            if path.suffix != ".md" or path.stat().st_size > 100_000:
                raise ValueError("Only bounded Markdown files allowed")
            text = path.read_text(encoding="utf-8")
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in link or link.startswith("#"):
                    continue
                target = (path.parent / link.split("#")[0]).resolve()
                if not target.is_relative_to(folder.resolve()) or not target.is_file():
                    raise ValueError("Broken or escaping local link: " + link)
            key = path.relative_to(source).as_posix()
            result[key] = text.replace("\r\n", "\n").encode("utf-8")
        result[name + "/LICENSE"] = (root / "LICENSE").read_bytes()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true")
    action.add_argument("--output", type=Path)
    args = parser.parse_args()
    files = payload()
    manifest = {p: hashlib.sha256(b).hexdigest() for p, b in files.items()}
    if args.output:
        dest = args.output.resolve()
        if dest.is_relative_to(ROOT):
            raise ValueError("Release artifacts must be outside the repository")
        dest.mkdir(parents=True, exist_ok=True)
        manifest_bytes = (json.dumps(manifest, indent=2) + "\n").encode()
        archive = dest / "manda-video-skills.tar"
        with archive.open("xb") as stream, tarfile.open(fileobj=stream, mode="w") as tar:
            for name, content in {**files, "manifest.json": manifest_bytes}.items():
                item = tarfile.TarInfo(name)
                item.size = len(content)
                item.mode = 0o640
                item.mtime = 0
                tar.addfile(item, io.BytesIO(content))
        print(json.dumps({"archive": str(archive), "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}))
    print(f"Validated {len(NAMES)} skills, {len(files)} payload files")


if __name__ == "__main__":
    main()
