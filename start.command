#!/bin/bash
set -e
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 が必要です。インストール後に再実行してください。"
  exit 1
fi
echo "http://localhost:8000 をブラウザーで開いてください。停止: Control+C"
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
