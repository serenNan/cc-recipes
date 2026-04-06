# cc-recipes

分享我和朋友们使用 Claude Code 的习惯、配置和玩法。

## 这是什么

一个收集 Claude Code 使用"食谱"的小仓库。每个人有自己的一套用法 —— 常用的 skill、hooks、工作流、快捷命令、踩过的坑、觉得好用的小技巧 —— 都丢在这里互相参考。

不追求统一规范，**各写各的，风格自由**。看到别人的好习惯可以直接抄过来用。

## 目录结构

```
cc-recipes/
├── README.md
├── hjn-recipes/           # hjn 的 CC 使用习惯
│   └── skills/
│       └── analyze-project/   # 接单分析 skill（五维评分 + 报价 + 项目初始化）
├── zj-recipes/            # zj 的 CC 使用习惯
└── lyq-recipes/           # lyq 的 CC 使用习惯
```

## 已有的食谱

### hjn

| 食谱 | 类型 | 说明 |
|------|------|------|
| [analyze-project](hjn-recipes/skills/analyze-project/) | Skill | 接单分析：需求拆解 → 五维难度评分 → 平台抽成计算 → 历史项目匹配校准报价 → 一键建项目文件夹 |

## 可以写什么

- **Skills** —— 完整的 skill 目录，别人 `cp` 到 `~/.claude/skills/` 就能用
- **Hooks** —— pre/post tool use hooks，防踩坑或自动化
- **工作流** —— 一个典型任务你是怎么让 CC 跑的
- **提示词模板** —— 反复用的 prompt 套路
- **配置片段** —— settings.json、CLAUDE.md 里的得意之作
- **踩坑记录** —— 别人别再踩一遍
- **神奇发现** —— 突然发现 CC 还能这么用

## 怎么用别人的食谱

直接看、直接抄。觉得好用就搬到自己的目录里，按自己的习惯改改。

**Skill 类食谱**的安装方法：
1. 把对应的 skill 目录复制到 `~/.claude/skills/`
2. 打开 `SKILL.md`，搜 `<YOUR_` 找占位符，替换成你自己的路径
3. 安装依赖（每个 skill 的 README 会说需要什么）
4. 重启 CC 会话即可使用

## CC 小技巧速查

### /insights —— 查看你的 CC 使用统计

在 CC 里输入 `/insights` 可以看到：
- **Token 用量统计**：每次会话消耗了多少 token，按天/周/月汇总
- **工具调用分布**：哪些工具用得最多（Read/Edit/Bash/Agent...）
- **会话时长和频率**：你每天大概跟 CC 聊多久
- **成本估算**：大致花了多少钱（基于 token 用量）

用法：直接在 CC 输入框打 `/insights` 回车。

这个命令对**了解自己的使用模式**很有帮助 —— 比如发现 Bash 工具调用占比太高，可能说明你该写个 skill 来替代重复的 shell 操作。
