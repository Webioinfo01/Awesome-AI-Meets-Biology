# Awesome-AI-Meets-Biology — curation rules

Curated paper list: `docs/data.json` (category dict) is the source of truth;
README counts and RSS are derived artifacts regenerated locally before every
push.

## Scope

AI×Biology papers. General-domain AI papers (e.g. a generic benchmark
database) only by explicit user request — say so in the commit message when
one is admitted.

## Adding a paper

```bash
awescholar --config config.json updater search --archive docs/data.json --by title "<title>" --category <Category> [--code-url owner/repo]
awescholar --config config.json updater enrich --archive docs/data.json --only "<title substring>"   # auto-find repo when codeUrl is empty
awescholar render counts --archive docs/data.json
awescholar render rss --archive docs/data.json -o docs/rss.xml
git add docs/data.json readme.md README.zh-CN.md docs/rss.xml && git commit && git push
```

Deployment is GitHub Pages serving `docs/` (CNAME → awesomebio.webioinfo.top):
pushing to main IS the deploy. There is no CI — the README/RSS in the push
must already be rendered.

## Conventions and gotchas

- `archive.stars_style: "badge"` (config.json): `githubStars` holds
  `https://img.shields.io/github/stars/owner/repo` URLs, never bare numbers.
- `--annotate` only fills `domain` for DOI-bearing records; fresh arXiv
  preprints need a manual one-line `domain`.
- Fresh arXiv preprints lag in Semantic Scholar: awescholar ≥0.2.7 derives
  `doi=10.48550/arXiv.<id>` and `venue=arXiv` from the record's arXiv
  external ID automatically; citation counts arrive once S2 catches up
  (`updater backfill --archive docs/data.json --fields citations`).
- `docs/data.json.*.bak` files are timestamped backups from render/update —
  git-clean files are skipped automatically; don't commit the baks.

Full command reference lives in the `awescholar` skill
(~/.agents/skills/awescholar).
