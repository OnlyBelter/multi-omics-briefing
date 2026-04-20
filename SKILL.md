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
3. 保存到 `~/Documents/bioinformatics-frontier/reports/YYYY/MM/YYYY-Wxx/`
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

---

## ⚠️ 去重机制（v1.1 新增）

为避免重复发送相同文章，建立了去重机制。

### 工作原理

1. **发送前检查**：每次生成报告前，读取 `sent-papers.json`，检查候选文章是否已发送过
2. **只发一次**：每篇文章只发送一次，除非有正当理由（如后续进展、趋势更新）
3. **强制理由**：重新发送时必须说明原因

### 去重列表文件

```
~/.qclaw/workspace/skills/multi-omics-briefing/sent-papers.json
```

**格式**：
```json
{
  "papers": [
    {
      "title": "文章标题",
      "sent_date": "2026-04-13",
      "reason": "为什么选这篇",
      "notes": "备注"
    }
  ]
}
```

### 重新发送的正当理由

| 理由 | 示例 |
|------|------|
| 后续进展 | 「本文于 4月8日 发送，今天因其被 Nature 亮点报道有新进展」 |
| 被其他研究引用 | 「该研究被另一篇 Cell 文章引用和验证」 |
| 趋势变化 | 「近期该方向连续发表 3 篇重要论文，值得汇总评述」 |
| 新数据集 | 「作者团队发布了配套的大规模数据集」 |

### 时间过滤规则

- 只选最近 7 天内发表的论文
- 发表日期超过 7 天的不发送
- 日期从论文的 published/posted date 判断，不是从搜索日期

---

**版本**: 1.1.0
**更新**: 2026-04-13
