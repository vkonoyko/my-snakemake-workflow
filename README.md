# Snakemake Workflow for Data Analysis

Simple educational workflow demonstrating DAG principles.

## Project Description

Workflow performs three sequential tasks:
1. Generate Data - creates random data points in JSON format
2. Analyze Data - analyzes data and creates visualization
3. Create Report - combines results into final report

## Project Structure

```
my-snakemake-workflow/
├── Snakefile
├── README.md
├── config.yaml
├── scripts/
│   ├── generate_data.py
│   └── analyze_data.py
├── data/
├── output/
└── logs/
```

## Installation and Run

### Prerequisites
- Python 3.9+
- Git
- Snakemake
- matplotlib

### Quick Start
```bash
# 1. Clone repository
git clone https://github.com/vkonoyko/my-snakemake-workflow.git
cd my-snakemake-workflow

# 2. Switch to workflow branch
git checkout feature/add-workflow

# 3. Install dependencies
pip install snakemake matplotlib

# 4. Run workflow
snakemake --cores 1
```

## Expected Output

After successful workflow execution:
- analysis_report.txt - text report with data analysis
- data_visualization.png - scatter plot of generated data
- final_report.txt - final report with metadata

## Testing

To test individual components:
```bash
# Test data generation
python scripts/generate_data.py test.json

# Test data analysis
python scripts/analyze_data.py test.json test_report.txt
```

## License

Educational project.
