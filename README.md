# Air Icons

Clean, minimal file icons for Zed, inspired by the JetBrains New UI (Air) icon set. Ships with two themes: the minimal **Air Icons** and the expansive **Air Material Icons**.

> **Pairs with [Air Theme](https://github.com/franzgollhammer/air-theme-zed)** — companion color theme (dark + light) ported from JetBrains Air.

![Air Icons preview](preview-air-icons.png)

## Themes

- **Air Icons Dark / Light** — 112 monochrome-accent file icons, tuned for compact tree UIs. Derived from JetBrains Air (Apache 2.0).
- **Air Material Icons Dark / Light** — 1245 colorful icons covering 1368 file suffixes, 2124 file stems, 4648 named folders. Full set from Material Icon Theme (MIT).

## Repository layout

```
icons/
├── air/                # Air Icons (112 SVGs per appearance)
│   ├── dark/
│   └── light/
└── air-material/       # Air Material Icons (1245 SVGs per appearance)
    ├── dark/
    ├── light/
    └── LICENSE.md
icon_themes/
├── air-icons.json
└── air-material-icons.json
```

## Install

### Zed Extensions

1. `cmd-shift-p` / `ctrl-shift-p` → `zed: extensions`
2. Search `Air Icons`
3. Install
4. `cmd-shift-p` / `ctrl-shift-p` → `icon theme selector: toggle` → pick one of:
   - `Air Icons Dark` / `Air Icons Light`
   - `Air Material Icons Dark` / `Air Material Icons Light`

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

Swap in `Air Material Icons Light` / `Air Material Icons Dark` to use the Material set.

### Manual (dev extension)

1. Clone this repo
2. `cmd-shift-p` / `ctrl-shift-p` → `zed: install dev extension`
3. Select repo folder
4. Pick theme via `icon theme selector: toggle`

## Supported file types

**Air Icons** — Languages: JavaScript, TypeScript, React, Vue, Svelte, Python, Rust, Go, Java, Kotlin, Swift, C/C++, C#, Ruby, PHP, Dart, Elixir, Haskell, Scala, Clojure, Erlang, Lua, R, Julia, Zig, Nim, OCaml, F#, Groovy, Perl, and more. Configs: Docker, Git, Webpack, Vite, Rollup, ESLint, Prettier, Babel, TSConfig, npm, pnpm, yarn, bun, Cargo, Maven, Gradle, Bazel, Terraform, Bicep, CMake, and more.

**Air Material Icons** — the full Material Icon Theme catalog: every language, framework, config format, build tool, and named folder shipped by `material-icon-theme` upstream (1245 icons, 4648 named folders).

## Development

```sh
./scripts/sync_from_air.sh             # re-sync Air Icons from local Air.app
./scripts/generate_air_material_icons.py  # rebuild Air Material set from material-icon-theme
```

The Material generator expects `material-icon-theme` extracted to `/tmp/mit-air/package/`:

```sh
mkdir -p /tmp/mit-air && cd /tmp/mit-air \
  && npm pack material-icon-theme \
  && tar -xzf material-icon-theme-*.tgz
```

See [`scripts/`](scripts) for sync automation.

## Attribution

- **Air Icons** — Derived from JetBrains Air (Apache 2.0).
- **Air Material Icons** — Full set from [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme) (MIT).

See [`NOTICE`](NOTICE) and [`icons/air-material/LICENSE.md`](icons/air-material/LICENSE.md) for full attribution.

## License

Apache 2.0 (this extension). Bundled icon sets retain their upstream licenses.
