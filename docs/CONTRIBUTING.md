# Contributing

## Add or Update Data (Contributors)

Choose **one** of the following methods:

### Method 1: Ask an AI Agent

If you are working inside Claude Code, Codex, Cursor, or another coding agent, tell it:

```text
Read https://github.com/Webioinfo01/awescholar/blob/main/README.ai.md and follow it to install awescholar for this agent.
```

Then ask the agent in natural language. For example:

```text
用 awescholar skills，更新 month_reports/2512_2/updater_filter.json 到项目。
```

```text
Using awescholar skills, update month_reports/2512_2/updater_filter.json into the project.
```

The agent will automatically execute the following steps:

1. **Merge** filtered papers into `docs/data.json` — deduplication by DOI, new categories appended, existing entries preserved
2. **Regenerate** `docs/rss.xml` — channel metadata preserved, only item entries updated

> Note: the README is a website-first landing page. Paper tables are no longer embedded in the README — the website (`docs/index.html` + `docs/data.json`) is the canonical browsing surface.

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
awescholar updater add --archive docs/data.json
```

### Method 4: Search from Semantic Scholar

```bash
# Search by title and save for review
awescholar updater search --json-file papers.json --by title

# Search by DOI
awescholar updater search --json-file papers.json --by doi

# Search and add directly to archive
awescholar updater search --archive docs/data.json --by title
```

> After updating data, submit a Pull Request.

---

## Merge and Publish (Maintainers Only)

### Step 1: Merge New Data into Archive

```bash
awescholar updater update --direction new2old --input updater_filter.json --archive docs/data.json
```

### Step 2: Refresh README Counts

```bash
awescholar updater counts --archive docs/data.json
```

The README table sections were removed in favor of the website; this command refreshes the papers badge and the per-category counts in the "Browse the Collection" section from the archive.

### Step 3: Generate RSS Feed

```bash
awescholar updater rss --archive docs/data.json
```

Both steps can also be run automatically via the full pipeline — set `merge_new_to_old: true` and `data_json_path: "docs/data.json"` in `config.json`, then:

```bash
awescholar --config config.json crawler run
```

---

## Install awescholar

```bash
pip install awescholar
```

For skill-based AI agent integration, see [README.ai.md](https://github.com/Webioinfo01/awescholar/blob/main/README.ai.md).

---

## Local Development Setup

If you are opening `index.html` locally (e.g., by double-clicking the file), you might encounter issues with loading `data.json` due to browser security restrictions (CORS).

To properly view and test the `index.html` file and its data dependencies locally, serve the files using a simple HTTP server:

1. Open your terminal.
2. Navigate to the `docs` directory:
   ```bash
   cd docs
   ```
3. Start a local HTTP server:
   ```bash
   python -m http.server
   ```
4. Open your browser and navigate to `http://localhost:8000`, then click on `index.html`.

To stop the server, press `Ctrl + C` in your terminal.
