#!/usr/bin/env python3
"""Generate icons/air-material/{dark,light}/ + icon_themes/air-material-icons.json.

Pulls all icons from PKief's material-icon-theme npm package (Material Icon
Theme, MIT). Reads /tmp/mit-air/package/ produced by `npm pack`.

Light variants are baked into icons/air-material/light/ so the theme JSON keeps
identical mappings across appearances. Specifically: for every entry in the
upstream theme's `light.*` overrides that points at a `*_light` icon, the
corresponding base-named SVG in light/ is overwritten with the light variant.
"""
import json
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PKG = Path("/tmp/mit-air/package")
MIT_JSON = PKG / "dist" / "material-icons.json"
OUT_DARK = REPO / "icons" / "air-material" / "dark"
OUT_LIGHT = REPO / "icons" / "air-material" / "light"
OUT_THEME = REPO / "icon_themes" / "air-material-icons.json"

mit = json.loads(MIT_JSON.read_text())
defs = mit["iconDefinitions"]

if OUT_DARK.exists():
    shutil.rmtree(OUT_DARK)
if OUT_LIGHT.exists():
    shutil.rmtree(OUT_LIGHT)
OUT_DARK.mkdir(parents=True)
OUT_LIGHT.mkdir(parents=True)


def src_path(rel: str) -> Path:
    return PKG / rel.replace("./../", "")


# 1. Copy every icon definition to both dark/ and light/ using the def name.
for name, info in defs.items():
    src = src_path(info["iconPath"])
    data = src.read_bytes()
    (OUT_DARK / f"{name}.svg").write_bytes(data)
    (OUT_LIGHT / f"{name}.svg").write_bytes(data)

# 2. Bake light overrides: light.<section>[key] = "<base>_light" -> overwrite
#    light/<base>.svg with the _light variant's contents.
light_sections = [
    "fileExtensions",
    "fileNames",
    "folderNames",
    "folderNamesExpanded",
    "rootFolderNames",
    "rootFolderNamesExpanded",
    "languageIds",
]
baked = set()
for sec in light_sections:
    for key, light_name in mit.get("light", {}).get(sec, {}).items():
        if not light_name.endswith("_light"):
            continue
        base = light_name[: -len("_light")]
        if base not in defs:
            continue
        src = src_path(defs[light_name]["iconPath"])
        (OUT_LIGHT / f"{base}.svg").write_bytes(src.read_bytes())
        baked.add(base)

available = {p.stem for p in OUT_DARK.glob("*.svg")}


def icon_path(appearance: str, name: str) -> str:
    return f"./icons/air-material/{appearance}/{name}.svg"


def build_theme(appearance: str) -> dict:
    file_icons = {n: {"path": icon_path(appearance, n)} for n in sorted(available)}
    default_file = mit.get("file", "file")
    if default_file not in available:
        default_file = "file"
    file_icons["default"] = {"path": icon_path(appearance, default_file)}

    def resolve(mapping: dict) -> dict:
        return {k: v for k, v in mapping.items() if v in available}

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
        "name": f"Air Material Icons {'Dark' if appearance == 'dark' else 'Light'}",
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
    "name": "Air Material Icons",
    "author": "fg",
    "themes": [build_theme("dark"), build_theme("light")],
}

OUT_THEME.parent.mkdir(parents=True, exist_ok=True)
OUT_THEME.write_text(json.dumps(theme, indent=2) + "\n")

print(f"icons available: {len(available)} (baked {len(baked)} light variants)")
print(f"wrote {OUT_THEME}")
for t in theme["themes"]:
    print(
        f"  {t['name']}: "
        f"suffixes={len(t['file_suffixes'])} "
        f"stems={len(t['file_stems'])} "
        f"folders={len(t['named_directory_icons'])} "
        f"icons={len(t['file_icons'])}"
    )
