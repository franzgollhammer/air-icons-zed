# Air Icons

Clean, minimal file icons for Zed, inspired by the JetBrains New UI (Air) icon set.

> **Pairs with [Air Theme](https://github.com/franzgollhammer/air-theme-zed)** — companion color theme (dark + light) ported from JetBrains Air.

![Air Icons preview](preview-air-icons.png)

## Themes

- **Air Icons Dark**
- **Air Icons Light**

112 file type icons, monochrome-accent style, tuned for compact tree UIs. Derived from JetBrains Air (Apache 2.0).

## Repository layout

```
icons/air/
├── dark/    # 112 Air SVGs (dark)
└── light/   # 112 Air SVGs (light)
icon_themes/
└── air-icons.json
```

## Install

### Zed Extensions

1. `cmd-shift-p` / `ctrl-shift-p` → `zed: extensions`
2. Search `Air Icons`
3. Install
4. `cmd-shift-p` / `ctrl-shift-p` → `icon theme selector: toggle` → pick `Air Icons Dark` or `Air Icons Light`

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
./scripts/sync_from_air.sh   # re-sync Air Icons from local Air.app
```

See [`scripts/`](scripts) for sync automation.

## Attribution

Derived from JetBrains Air (Apache 2.0). See [`NOTICE`](NOTICE) for full attribution.

## License

Apache 2.0.
