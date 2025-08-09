# Underwriting Experiment (A/B Limit Policy)

Compares two limit rules (A: 30% of income, B: 25%) and reports avg limit, utilization, and default rate.

## How to run
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python experiment.py
