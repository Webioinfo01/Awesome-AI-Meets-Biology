# 如何更新

## 第一部分：更新数据（贡献者）

选择**任一**方法：

### 方法一：使用 AweAgent CLI

1. 安装 AweAgent：`pip install aweagent` 或从 [GitHub](https://github.com/Webioinfo01/AweAgent) 克隆
2. 配置 `config.json`
3. 运行：`aweagent run --mode config --config config.json`

### 方法二：直接编辑

按以下格式向 `docs/data.json` 添加条目：

```json
{
    "year": "2025.07",
    "title": "论文标题",
    "team": "团队名称",
    "team website": "https://...",
    "affiliation": "",
    "domain": "研究领域",
    "venue": "期刊/会议",
    "paperUrl": "https://...",
    "codeUrl": "https://github.com/...",
    "githubStars": "https://img.shields.io/github/stars/owner/repo",
    "doi": ""
}
```

### 方法三：交互模式

```bash
aweagent updater --mode new_interactive --archive-file docs/data.json
```

> ✅ **更新数据后即可提交 Pull Request！**

---

## 第二部分：转换数据（仅维护者）

执行转换数据前，需要人工校正一遍"updater_filter.json" 中的内容是否合适。

```bash
# 步骤1：将新数据转换为归档格式
aweagent updater --mode new2old_json --new-data month_reports/2506_1/updater_filter.json --archive-file docs/data.json

# 步骤2：更新 readme.md
aweagent updater --mode readme --readme-path readme.md --archive-file docs/data.json --no-backup

# 步骤3：生成 RSS 订阅
aweagent updater --mode rss --rss-path docs/rss.xml --archive-file docs/data.json
```

不使用 AweAgent 时，仅需执行步骤 2 和 3。

