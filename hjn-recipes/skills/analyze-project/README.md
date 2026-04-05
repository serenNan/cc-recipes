# analyze-project skill（hjn 分享版）

hjn 自用的接单分析 skill。发了单子链接/文件，它会：

1. 读需求（支持 URL / PDF / DOCX / 图片）
2. 搜历史相似项目校准报价（可选，依赖 memsearch）
3. 五维打分给难度等级和报价区间
4. 算平台抽成后的实际到手金额
5. 问你接不接；接的话建项目文件夹 + Obsidian 订单记录 + git init
6. 按难度推荐对应的 GSD 命令

## 安装

把整个 `analyze-project/` 目录复制到 `~/.claude/skills/` 下：

```bash
cp -r analyze-project ~/.claude/skills/
```

## 使用前必改（重要）

SKILL.md 里有一段 `⚠️ 使用前必读` 的注释块，列出了所有需要你本地化的地方：

- **路径占位符**（必改）
  - `<YOUR_FREELANCE_DIR>` → 你的接单项目根目录
  - `<YOUR_ORDERS_NOTE_DIR>` → 你的订单笔记目录
- **平台列表和抽成比例** → 按你常接的平台改
- **memsearch / project-log** → 没有就把第二步删掉
- **wecom-monitor 自动识别** → hjn 个人项目，不用就删
- **docx skill 依赖** → 没装就改成 libreoffice/soffice 直接调用
- **Python 环境** → pdf2images.py 需要 `pip install pymupdf`

直接在 SKILL.md 里全局搜 `<YOUR_` 和 `（按你自己情况改）` 就能定位要改的地方。

## 使用示例

```
# 发个 PDF 需求给它
/analyze-project D:/downloads/需求.pdf

# 发个 URL
/analyze-project https://example.com/project-brief

# 直接描述
/analyze-project "用 Python 爬 xx 网站数据，导出 Excel，要求带筛选功能"
```

skill 的触发词很多（分析单子、接不接得了、报价多少、这单能做吗 等），通常自然语言一说就会自动触发。

## 目录结构

```
analyze-project/
├── SKILL.md                    # 主体提示词（要改占位符）
├── references/
│   └── report-template.md      # 分析报告模板（用户明确要求时才生成）
└── scripts/
    ├── pdf2images.py           # PDF → 图片（PyMuPDF）
    ├── docx2pdf.py             # DOCX → PDF
    └── read_pdf.py             # 读 PDF 文本
```
