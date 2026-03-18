# JetBrains Air Icons for Zed

A Zed icon theme extension built from the file icons bundled with the locally installed `Air.app`.

## Included themes

- `JetBrains Air Icons Dark`
- `JetBrains Air Icons Light`

## Local install

1. Open Zed.
2. Run `zed: install dev extension`.
3. Select this repository.
4. Run `icon theme selector: toggle` and choose a JetBrains Air Icons variant.

To switch automatically with system appearance, set this in your Zed settings:

```json
{
  "icon_theme": {
    "mode": "system",
    "light": "JetBrains Air Icons Light",
    "dark": "JetBrains Air Icons Dark"
  }
}
```

## Sync from Air

```sh
./scripts/sync_from_air.sh
```

## Notes

- The icon assets are extracted from JetBrains Air. Review JetBrains licensing before publishing or redistributing this extension.
- Update `repository` in `extension.toml` if you publish this repo.
