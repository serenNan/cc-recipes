# CLAUDE.md

## 项目简介

收集我和朋友们(hjn / zj / lyq)使用 Claude Code 的习惯、配置和玩法的笔记仓库。

## 技术栈

纯 Markdown 笔记，无构建、无依赖、无测试。用任何编辑器写就行，推荐 VSCode 或 Obsidian。

## 项目结构

```
cc-recipes/
├── README.md         # 项目说明
├── CLAUDE.md         # 本文件
├── .gitignore
├── hjn-recipes/      # hjn 的 CC 使用习惯
│   └── skills/       # 分享的 skill（如 analyze-project 接单分析）
├── zj-recipes/       # zj 的 CC 使用习惯
└── lyq-recipes/      # lyq 的 CC 使用习惯
```

每个人的子目录下自由组织内容，没有统一规范。可以写的内容类型见 README.md。

## 开发约定

- 文件编码 UTF-8 无 BOM
- 中文内容里用英文标点，避免 Unicode 特殊字符
- 提交信息用中文，遵循 `feat/fix/docs/chore` 等常规前缀
- 各人目录内风格自由，互不干涉
