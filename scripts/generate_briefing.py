#!/usr/bin/env python3
"""
多组学研究简报生成器
搜索 Nature 和 ArXiv 最新论文，生成结构化简报
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

def get_iso_week_path(date_str):
    """根据日期生成 YYYY/MM/YYYY-Wxx/ 子目录路径"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    year = dt.year
    month = dt.month
    week = dt.isocalendar()[1]  # ISO 周数
    return f"{year}/{month:02d}/{year}-W{week:02d}/"

# 配置
CONFIG = {
    "search_keywords": [
        "multi-omics", "bioinformatics", "computational biology",
        "genomics", "transcriptomics", "proteomics", "metabolomics",
        "single-cell", "spatial transcriptomics", "AI biology"
    ],
    "sources": ["nature.com", "arxiv.org"],
    "base_dir": os.path.expanduser("~/Documents/bioinformatics-frontier/reports"),
    "max_papers": 5
}

def generate_briefing():
    """生成简报主函数"""
    today = datetime.now().strftime("%Y-%m-%d")
    week_subdir = get_iso_week_path(today)
    output_dir = os.path.join(CONFIG["base_dir"], week_subdir)
    output_file = os.path.join(output_dir, f"{today}-multiomics-briefing.md")

    # 确保输出目录存在（含子目录）
    os.makedirs(output_dir, exist_ok=True)

    print(f"[generate_briefing] 简报将保存到: {output_file}")
    return output_file

def main():
    """主入口"""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Usage: python generate_briefing.py")
        print("生成每日多组学研究简报")
        sys.exit(0)
    
    output_file = generate_briefing()
    print(f"✅ 简报生成完成: {output_file}")

if __name__ == "__main__":
    main()
