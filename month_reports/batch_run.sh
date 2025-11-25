#!/bin/bash
# 批量运行 aweagent 从 2508_2 到 2511_1
# 使用方法: ./batch_run.sh

set -e  # 遇到错误时停止

# 配置文件路径
CONFIG_FILE="/Users/peng/Desktop/Project/Agent/Awesome-AI-Meets-Biology/month_reports/config.json"
WORK_DIR="/Users/peng/Desktop/Project/Agent/Awesome-AI-Meets-Biology/month_reports"

# 定义所有时间段 (文件夹名 开始日期 结束日期)
declare -a PERIODS=(
    "2508_1 2025-08-01 2025-08-15"
    "2508_2 2025-08-16 2025-08-31"
    "2509_1 2025-09-01 2025-09-15"
    "2509_2 2025-09-16 2025-09-30"
    "2510_1 2025-10-01 2025-10-15"
    "2510_2 2025-10-16 2025-10-31"
    "2511_1 2025-11-01 2025-11-15"
)

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  批量运行 AweAgent (2508_1 -> 2511_1)  ${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

for period_info in "${PERIODS[@]}"; do
    # 解析时间段信息
    read -r folder start_date end_date <<< "$period_info"
    
    echo -e "${YELLOW}----------------------------------------${NC}"
    echo -e "${YELLOW}处理: $folder ($start_date to $end_date)${NC}"
    echo -e "${YELLOW}----------------------------------------${NC}"
    
    # 1. 创建文件夹（如果不存在）
    mkdir -p "$WORK_DIR/$folder"
    echo "✓ 文件夹已准备: $folder"
    
    # 2. 使用 Python 更新 config.json（更可靠的 JSON 处理）
    python3 << EOF
import json

config_path = "$CONFIG_FILE"
with open(config_path, 'r') as f:
    config = json.load(f)

# 更新配置
config['db_path'] = "$folder"
config['output_filename'] = "$folder/research_report_o4mini.md"
config['custom_query']['publication_date'] = "$start_date to $end_date"

with open(config_path, 'w') as f:
    json.dump(config, f, indent=4)

print("✓ config.json 已更新")
EOF
    
    # 3. 运行 aweagent
    echo "▶ 开始运行 aweagent..."
    cd "$WORK_DIR"
    aweagent --mode config --config "$CONFIG_FILE"
    
    echo -e "${GREEN}✓ $folder 完成!${NC}"
    echo ""
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  全部任务完成!                         ${NC}"
echo -e "${GREEN}========================================${NC}"

