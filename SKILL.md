# Multi-Omics Daily Briefing Skill

每日多组学研究简报自动生成 Skill。搜索 Nature 和 ArXiv 最新论文，生成结构化简报并推送到 GitHub。

## 功能

- 🔍 自动搜索 Nature.com + ArXiv 最新论文
- 📊 精选 3-5 篇高价值研究
- 📝 生成结构化 Markdown 简报
- 🚀 自动推送到 GitHub 仓库
- ⏰ 定时任务：每天 8:30 AM (Asia/Shanghai)

## 覆盖领域

- 多组学数据分析
- 计算生物学 / 生物信息学
- 基因组学 / 转录组学 / 蛋白质组学
- AI 在生物学中的应用
- 空间转录组 / 单细胞组学

## 安装

```bash
# 克隆到 skills 目录
cd ~/.qclaw/workspace/skills
git clone https://github.com/OnlyPandaX/multi-omics-briefing.git

# 安装依赖（如需）
cd multi-omics-briefing
pip install -r requirements.txt  # 如有依赖
```

## 配置

### 1. GitHub 仓库设置

确保 `~/Documents/bioinformatics-frontier/` 是 Git 仓库且已配置远程：

```bash
cd ~/Documents/bioinformatics-frontier
git remote -v
# 应显示 origin 指向你的 GitHub 仓库
```

### 2. 定时任务配置

在 `~/.qclaw/cron/jobs.json` 中添加：

```json
{
  "id": "83b6aea6-6ed0-4fd0-866f-b857803c99f6",
  "name": "每日多组学研究简报",
  "enabled": true,
  "schedule": {
    "kind": "cron",
    "expr": "30 8 * * *",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "wakeMode": "now",
  "payload": {
    "kind": "agentTurn",
    "message": "运行 multi-omics-briefing skill，生成今日多组学研究简报",
    "timeoutSeconds": 600
  },
  "delivery": {
    "mode": "announce",
    "channel": "qqbot",
    "to": "YOUR_QQ_ID"
  }
}
```

## 使用方法

### 手动运行

```bash
cd ~/.qclaw/workspace/skills/multi-omics-briefing
python scripts/generate_briefing.py
```

### 自动运行

定时任务会在每天 8:30 自动执行：
1. 搜索 Nature.com 和 ArXiv
2. 生成简报
3. 保存到 `~/Documents/bioinformatics-frontier/reports/`
4. 推送到 GitHub

## 输出格式

简报包含：
- 📚 精选论文 3-5 篇
- 每篇论文：标题、作者、期刊、链接、概要、贡献、Critical 简评
- 📊 整体趋势评述

## 文件结构

```
multi-omics-briefing/
├── SKILL.md              # 本文件
├── scripts/
│   ├── generate_briefing.py    # 主生成脚本
│   └── auto-push-briefing.sh   # 自动推送脚本
├── config/
│   └── keywords.json     # 搜索关键词配置
└── templates/
    └── briefing_template.md    # 简报模板
```

## 依赖

- Python 3.8+
- Git
- 网络搜索工具（web_fetch）

## 许可证

MIT

## 作者

胖达 🐼
