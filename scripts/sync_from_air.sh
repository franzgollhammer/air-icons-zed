#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_ZIP="/Applications/Air.app/Contents/app/code-cache/0477a001d111c7c2117f3d3b708a05eddc16cf0e0c54ed6bbe174db62cea4195/resources.zip"
TMP_DIR="$ROOT_DIR/.tmp-sync"

if [[ ! -f "$SOURCE_ZIP" ]]; then
  echo "Air resources archive not found at:"
  echo "  $SOURCE_ZIP"
  exit 1
fi

rm -rf "$TMP_DIR" "$ROOT_DIR/icons"
mkdir -p "$TMP_DIR"

unzip -q "$SOURCE_ZIP" \
  "icons/dark/file-types/*" \
  "icons/light/file-types/*" \
  "icons/dark/folder.svg" \
  "icons/light/folder.svg" \
  "icons/dark/chevron-right.svg" \
  "icons/dark/chevron-down.svg" \
  "icons/light/chevron-right.svg" \
  "icons/light/chevron-down.svg" \
  "icons/dark/docker.svg" \
  "icons/light/docker.svg" \
  -d "$TMP_DIR"

mv "$TMP_DIR/icons" "$ROOT_DIR/icons"
rm -rf "$TMP_DIR"

echo "Synced Air icons into:"
echo "  $ROOT_DIR/icons"
