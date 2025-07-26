# Monthly Reports Directory

This directory contains monthly research reports in markdown format.

## File Naming Convention

### Format: `YYYYMM.md`

- **YYYY**: 4-digit year (e.g., 2025)
- **MM**: 2-digit month (e.g., 01 for January, 12 for December)

### Examples:
- `202505.md` - May 2025 report
- `202412.md` - December 2024 report
- `202401.md` - January 2024 report

## Directory Structure

```
docs/
├── monthly-reports.html    # Main page
├── reports-config.json     # Configuration file
└── month_reports/
    ├── README.md           # This file
    ├── 202505.md          # May 2025 report
    ├── 202504.md          # April 2025 report
    ├── 202503.md          # March 2025 report
    ├── 202502.md          # February 2025 report
    ├── 202501.md          # January 2025 report
    └── 202412.md          # December 2024 report
```

## Configuration

The reports are managed through `reports-config.json` in the docs directory. This file contains:

- List of all available reports
- Display names and descriptions
- File paths and metadata

### Configuration Format:
```json
{
  "reports": [
    {
      "id": "202505",
      "name": "May 2025",
      "file": "month_reports/202505.md",
      "description": "Research Report for May 2025"
    }
  ],
  "metadata": {
    "lastUpdated": "2025-01-15",
    "totalReports": 1,
    "description": "Monthly research reports on AI applications in biology"
  }
}
```

## Adding New Reports

1. Create a new markdown file with the format `YYYYMM.md`
2. Place it in the `month_reports/` directory
3. Update `reports-config.json` to include the new report
4. The page will automatically load the updated configuration

## Markdown Format

Each report should be a valid markdown file. The first heading will be used as the report title in the navigation.

Example structure:
```markdown
# Research Paper Report for 2025-05-01 to 2025-05-30

## Overall Summary
...

## Table of Contents
...

## ai-agents
...
```

## Notes

- Reports are loaded from the configuration file
- Files are automatically sorted by date (newest first)
- The system supports reports from 2020 onwards
- Invalid files or non-markdown files will be ignored
- The page will show a helpful message if no reports are found
- Fallback to directory scanning if configuration file is not available 