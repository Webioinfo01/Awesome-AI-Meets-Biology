#!/bin/bash
# Batch run aweagent from 2508_2 to 2511_1
# Usage: ./batch_run.sh

set -e  # Exit on error

# Config file path
CONFIG_FILE="/Users/peng/Desktop/Project/Agent/Awesome-AI-Meets-Biology/month_reports/config.json"
WORK_DIR="/Users/peng/Desktop/Project/Agent/Awesome-AI-Meets-Biology/month_reports"

# Define all time periods (folder name start date end date)
declare -a PERIODS=(
    "2508_1 2025-08-01 2025-08-15"
    "2508_2 2025-08-16 2025-08-31"
    "2509_1 2025-09-01 2025-09-15"
    "2509_2 2025-09-16 2025-09-30"
    "2510_1 2025-10-01 2025-10-15"
    "2510_2 2025-10-16 2025-10-31"
    "2511_1 2025-11-01 2025-11-15"
)

# Color output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Batch Running AweAgent (2508_1 -> 2511_1)  ${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

for period_info in "${PERIODS[@]}"; do
    # Parse period information
    read -r folder start_date end_date <<< "$period_info"
    
    echo -e "${YELLOW}----------------------------------------${NC}"
    echo -e "${YELLOW}Processing: $folder ($start_date to $end_date)${NC}"
    echo -e "${YELLOW}----------------------------------------${NC}"
    
    # 1. Create folder (if not exists)
    mkdir -p "$WORK_DIR/$folder"
    echo "✓ Folder ready: $folder"
    
    # 2. Update config.json using Python (more reliable JSON processing)
    python3 << EOF
import json

config_path = "$CONFIG_FILE"
with open(config_path, 'r') as f:
    config = json.load(f)

# Update configuration
config['db_path'] = "$folder"
config['output_filename'] = "$folder/research_report_o4mini.md"
config['custom_query']['publication_date'] = "$start_date to $end_date"

with open(config_path, 'w') as f:
    json.dump(config, f, indent=4)

print("✓ config.json updated")
EOF
    
    # 3. Run aweagent
    echo "▶ Starting aweagent..."
    cd "$WORK_DIR"
    aweagent --mode config --config "$CONFIG_FILE"
    
    echo -e "${GREEN}✓ $folder completed!${NC}"
    echo ""
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  All tasks completed!                  ${NC}"
echo -e "${GREEN}========================================${NC}"

