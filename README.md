# Air Icons

Two icon themes for Zed in one extension:

- **Air Icons** — clean, minimal, inspired by the JetBrains New UI (Air) icon set
- **Water Icons** — colorful Material Icon Theme subset (910 icons)

> **Pairs with [Air Theme](https://github.com/franzgollhammer/air-theme-zed)** — companion color theme (dark + light) ported from JetBrains Air.

![Air Icons preview](preview-air-icons.png)

## Themes

### Air Icons (Dark + Light)

- 112 file type icons, monochrome-accent style, tuned for compact tree UIs
- Derived from JetBrains Air (Apache 2.0)

### Water Icons (Dark + Light)

- 910 icons covering ~850 file extensions, ~1600 file names, ~2500 folder names
- Material Icon Theme subset
- Light theme bakes in 34 `_light` variants for icons that ship a light-mode counterpart

## Repository layout

```
icons/
├── air/
│   ├── dark/    # 112 Air SVGs (dark)
│   └── light/   # 112 Air SVGs (light)
└── water/
    ├── dark/    # 910 Material SVGs (dark)
    ├── light/   # 910 Material SVGs (light variants applied where available)
    └── LICENSE.md
icon_themes/
├── air-icons.json
└── water-icons.json
```

## Install

### Zed Extensions

1. `cmd-shift-p` / `ctrl-shift-p` → `zed: extensions`
2. Search `Air Icons`
3. Install
4. `cmd-shift-p` / `ctrl-shift-p` → `icon theme selector: toggle` → pick `Air Icons Dark`/`Light` or `Water Icons Dark`/`Light`

### Auto-switch with system appearance

Add to Zed settings:

```json
{
  "icon_theme": {
    "mode": "system",
    "light": "Air Icons Light",
    "dark": "Air Icons Dark"
  }
}
```

Or with Water Icons:

```json
{
  "icon_theme": {
    "mode": "system",
    "light": "Water Icons Light",
    "dark": "Water Icons Dark"
  }
}
```

### Manual (dev extension)

1. Clone this repo
2. `cmd-shift-p` / `ctrl-shift-p` → `zed: install dev extension`
3. Select repo folder
4. Pick theme via `icon theme selector: toggle`

## Supported file types

Languages: JavaScript, TypeScript, React, Vue, Svelte, Python, Rust, Go, Java, Kotlin, Swift, C/C++, C#, Ruby, PHP, Dart, Elixir, Haskell, Scala, Clojure, Erlang, Lua, R, Julia, Zig, Nim, OCaml, F#, Groovy, Perl, and more.

Configs: Docker, Git, Webpack, Vite, Rollup, ESLint, Prettier, Babel, TSConfig, npm, pnpm, yarn, bun, Cargo, Maven, Gradle, Bazel, Terraform, Bicep, CMake, and more.

## Development

```sh
./scripts/sync_from_air.sh           # re-sync Air Icons from local Air.app
./scripts/generate_water_icons.py    # regenerate Water Icons theme JSON
```

See [`scripts/`](scripts) for sync automation.

## Attribution

- **Air Icons** — derived from JetBrains Air (Apache 2.0)
- **Water Icons** — Material Icon Theme by Philipp Kief (MIT), filename subset

See [`NOTICE`](NOTICE) for full attribution and [`icons/water/LICENSE.md`](icons/water/LICENSE.md) for the MIT text.

## License

Apache 2.0 (extension code + Air Icons assets). Water Icons assets MIT.
