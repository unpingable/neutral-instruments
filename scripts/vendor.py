#!/usr/bin/env python3
"""Check or explicitly update a product's pinned generated snapshot."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

p = argparse.ArgumentParser()
p.add_argument("upstream", type=Path, help="local neutral-instruments checkout")
p.add_argument("product", type=Path, help="product repository root")
p.add_argument("--update", action="store_true", help="copy after verification; never implicit")
args = p.parse_args()
source = args.upstream / "dist"
manifest = json.loads((source / "neutral-instruments.manifest.json").read_text())
for relative, expected in manifest["files"].items():
    actual = hashlib.sha256((source / relative).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f"upstream build does not match its manifest: {relative}")
target = args.product / "vendor" / "neutral-instruments"
drift = []
for relative, expected in manifest["files"].items():
    path = target / relative
    actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "missing"
    if actual != expected:
        drift.append(relative)
target_manifest = target / "neutral-instruments.manifest.json"
if not target_manifest.is_file() or target_manifest.read_bytes() != (source / target_manifest.name).read_bytes():
    drift.append(target_manifest.name)
if not args.update:
    if drift:
        raise SystemExit("vendored snapshot drift: " + ", ".join(drift) + "; rerun with --update explicitly")
    print(f"vendored snapshot matches {manifest['source_commit']}")
else:
    target.mkdir(parents=True, exist_ok=True)
    for relative in [*manifest["files"], target_manifest.name]:
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, destination)
    print(f"updated {target} from neutral-instruments@{manifest['source_commit']}")
