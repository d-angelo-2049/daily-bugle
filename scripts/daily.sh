#!/bin/zsh
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

git pull origin main
uv run run.py
claude --dangerously-skip-permissions -p "/digest"

# 最新ファイルへのリダイレクト index.html を生成
LATEST=$(ls -t output/*.html 2>/dev/null | grep -v 'output/index.html' | head -1 | xargs basename)
cat > output/index.html << EOF
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=${LATEST}">
  <title>Daily Bugle</title>
</head>
<body>
  <p><a href="${LATEST}">最新のダイジェストを開く</a></p>
</body>
</html>
EOF

git add output/
git diff --staged --quiet && echo "No changes to commit" && exit 0
git commit -m "Daily digest $(date +%Y-%m-%d)"
git push origin main
