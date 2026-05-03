# Multi-Omics Daily Briefing

🧬 每日多组学研究简报自动生成工具

## 功能

- 搜索 Nature.com + ArXiv **当天**发表的论文
- 精选 3-5 篇高价值研究
- 生成结构化 Markdown 简报
- 自动推送到 GitHub
- 当天无相关论文时发送跳过通知

## 快速开始

```bash
# 运行生成器
python scripts/generate_briefing.py

# 推送到 GitHub
bash scripts/auto-push-briefing.sh
```

## 定时任务

每天 **06:30** (Asia/Shanghai) 自动运行，超时 600 秒。

## 报告保存路径

```
~/Documents/bioinformatics-frontier/reports/YYYY/MM/YYYY-Wxx/YYYY-MM-DD-multiomics-briefing.md
```

## 输出示例

见 `~/Documents/bioinformatics-frontier/reports/`

## 作者

胖达 🐼

---

## 更新日志

### v1.5.0 (2026-04-29)

**去重列表自动清理 + 动态维护**

- 🔧 去重列表 (`sent-papers.json`) 自动清理：**保留最近 30 天**记录
- 🔧 每次更新时，用 Python 删除超过 30 天的文章（搜索仅当天，超期论文不会重复出现）
- 🔧 保持去重列表精简（约 30-50 篇），提升调用效率
- 📝 更新 cron prompt，加入自动清理逻辑（3.5 节）

### v1.4.0 (2026-04-25)

**搜索策略重构 + 时间调整**

- 🔧 搜索策略：从「最近 7 天」改为**仅当天**
- 🔧 无相关论文时：不发简报，发送简短跳过通知
- 🔧 执行时间：07:30 → **06:30** (Asia/Shanghai)，避开模型高峰
- 🔧 超时：维持 600s，试运行一周后评估
- 📝 去重机制保留但定位变化：主要防止跨源重复（Nature + ArXiv 同一论文）
- 📝 SKILL.md 全面重写，移除内联补丁，逻辑统一

### v1.3.0 (2026-04-22)

- 强化报告保存路径说明，增加正确/错误示例
- 避免 cron 任务将文件误存到 `reports/` 根目录

### v1.2.0 (2026-04-17)

- 报告归档路径更新为 `YYYY/MM/YYYY-Wxx/` 结构
- auto-push-briefing.sh 升级至 v1.2.0

### v1.1.0 (2026-04-13)

- 新增去重机制（sent-papers.json）
- 重新发送需正当理由（后续进展、被引用、趋势变化、新数据集）

### v1.0.0 (2026-04-08)

- 初始版本
- 搜索 Nature + ArXiv 最近 7 天论文
- 每日 8:30 AM 自动运行
- 精选 3-5 篇，生成 Markdown 简报
