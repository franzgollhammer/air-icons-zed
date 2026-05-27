#!/usr/bin/env python3
"""Generate icon_themes/water-icons.json from MIT theme JSON + bundled Water Icons.

Reads file/folder mappings from Material Icon Theme (vscode-material-icon-theme)
and filters them to icons present in icons/water/dark/. Emits Zed v0.3.0 schema
with two themes (dark + light) pointing at icons/water/{dark,light}/.

Light variants are baked into icons/water/light/ (base SVGs overwritten with their
*_light counterparts at restructure time), so theme JSON keeps identical mappings
across appearances.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WATER_DARK = REPO / "icons" / "water" / "dark"
MIT_JSON = Path("/tmp/mit-pkg/package/dist/material-icons.json")
OUT = REPO / "icon_themes" / "water-icons.json"

available = {p.stem for p in WATER_DARK.glob("*.svg")}
mit = json.loads(MIT_JSON.read_text())


def icon_path(appearance: str, name: str) -> str:
    return f"./icons/water/{appearance}/{name}.svg"


def build_theme(appearance: str) -> dict:
    file_icons = {n: {"path": icon_path(appearance, n)} for n in sorted(available)}
    file_icons["default"] = {"path": icon_path(appearance, mit.get("file", "file"))}

    def resolve(base: dict) -> dict:
        return {k: v for k, v in base.items() if v in available}

    file_suffixes = dict(sorted(resolve(mit.get("fileExtensions", {})).items()))
    file_stems = dict(sorted(resolve(mit.get("fileNames", {})).items()))

    folder_c = resolve(mit.get("folderNames", {}))
    folder_e = resolve(mit.get("folderNamesExpanded", {}))
    named_dirs = {}
    for name in sorted(set(folder_c) | set(folder_e)):
        c, e = folder_c.get(name), folder_e.get(name)
        if not (c and e):
            continue
        named_dirs[name] = {
            "collapsed": icon_path(appearance, c),
            "expanded": icon_path(appearance, e),
        }

    df = mit.get("folder", "folder")
    do = mit.get("folderExpanded", "folder-open")
    if df not in available:
        df = "folder"
    if do not in available:
        do = "folder-open"

    return {
        "name": f"Water Icons {'Dark' if appearance == 'dark' else 'Light'}",
        "appearance": appearance,
        "directory_icons": {
            "collapsed": icon_path(appearance, df),
            "expanded": icon_path(appearance, do),
        },
        "named_directory_icons": named_dirs,
        "chevron_icons": {
            "collapsed": f"./icons/air/{appearance}/chevron-right.svg",
            "expanded": f"./icons/air/{appearance}/chevron-down.svg",
        },
        "file_stems": file_stems,
        "file_suffixes": file_suffixes,
        "file_icons": file_icons,
    }


theme = {
    "$schema": "https://zed.dev/schema/icon_themes/v0.3.0.json",
    "name": "Water Icons",
    "author": "fg",
    "themes": [build_theme("dark"), build_theme("light")],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(theme, indent=2) + "\n")
print(f"wrote {OUT}")
print(f"icons available: {len(available)}")
for t in theme["themes"]:
    print(
        f"  {t['name']}: "
        f"suffixes={len(t['file_suffixes'])} "
        f"stems={len(t['file_stems'])} "
        f"folders={len(t['named_directory_icons'])} "
        f"icons={len(t['file_icons'])}"
    )
