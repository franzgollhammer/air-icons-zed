# Air Icons

A clean, minimal file icon theme for Zed, inspired by the JetBrains New UI (Air) icon set.

> **Pairs with [Air Theme](https://github.com/franzgollhammer/air-theme-zed)** — companion color theme (dark + light) ported from JetBrains Air. Designed to look right next to these icons.

![Air Icons preview](preview-air-icons.png)

## Features

- 112 file type icons, dark + light variants
- Wide language, framework, and config file coverage
- Crisp monochrome-accent style, tuned for compact tree UIs

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
./scripts/sync_from_air.sh   # re-sync icons from local Air.app
```

See [`scripts/`](scripts) for sync automation.

## Attribution

Icons derived from JetBrains Air. Review licensing before redistribution.

## License

Apache 2.0
