#!/bin/bash
# auto-push-briefing.sh
# 自动推送多组学简报到 GitHub
# 用法: bash auto-push-briefing.sh

set -euo pipefail

REPO_DIR="$HOME/Documents/bioinformatics-frontier"
DATE=$(date +%Y-%m-%d)
REPORT_FILE="$REPO_DIR/reports/$DATE-multiomics-briefing.md"

# 检查文件是否存在
if [ ! -f "$REPORT_FILE" ]; then
  echo "[auto-push] 报告文件不存在: $REPORT_FILE" >&2
  exit 1
fi

# 推送到 GitHub
cd "$REPO_DIR"
git add "reports/$DATE-multiomics-briefing.md"

if git diff --cached --quiet; then
  echo "[auto-push] 内容无变化，跳过推送"
  exit 0
fi

git commit -m "Add multiomics briefing for $DATE"
git push origin main
echo "[auto-push] 已推送到 GitHub ✅"