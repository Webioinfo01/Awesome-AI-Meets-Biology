# How to Update

## Part 1: Update Data (Contributors)

Choose **one** of the following methods:

### Method 1: Use AweAgent CLI

1. Install AweAgent: `pip install aweagent` or clone from [GitHub](https://github.com/Webioinfo01/AweAgent)
2. Configure `config.json`
3. Run: `aweagent crawler --mode config --config config.json`

### Method 2: Direct Edit

Add entries to `docs/data.json` following this format:

```json
{
    "year": "2025.07",
    "title": "Paper Title",
    "team": "Team Name",
    "team website": "https://...",
    "affiliation": "",
    "domain": "Research Domain",
    "venue": "Journal/Conference",
    "paperUrl": "https://...",
    "codeUrl": "https://github.com/...",
    "githubStars": "https://img.shields.io/github/stars/owner/repo",
    "doi": ""
}
```

### Method 3: Interactive Mode

```bash
aweagent updater --mode new_interactive --archive-file docs/data.json
```

### Method 4: Search from Semantic Scholar

```bash
# Search by title (default)
aweagent updater --mode new_search --json-file papers.json --search-by title

# Search by DOI
aweagent updater --mode new_search --json-file papers.json --search-by doi
```

> ✅ **After updating data, you can submit a Pull Request!**

---

## Part 2: Convert Data (Maintainers Only)

Before executing data conversion, manually verify that the content in "updater_filter.json" is appropriate.

```bash
# Step 1: Convert new data to archive format
aweagent updater --mode new2old_json --new-data month_reports/2512_1/updater_filter.json --archive-file docs/data.json

# Step 2: Update readme.md
aweagent updater --mode readme --readme-path readme.md --archive-file docs/data.json --no-backup

# Step 3: Generate RSS feed
aweagent updater --mode rss --rss-path docs/rss.xml --archive-file docs/data.json
```

Without AweAgent, only Steps 2 & 3 are needed.
