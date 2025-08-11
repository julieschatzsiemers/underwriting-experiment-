# Underwriting Limit Policy Simulation

Compares two limit rules:
- **A:** 30% of income  
- **B:** 25% of income

## What it reports
- Average limit and utilization by group  
- Default rate by group (simple proxy)

> Default proxy note: briefly explain how you flag “default” (e.g., “marks default when simulated payment capacity is below a minimum payment threshold”).

## Quickstart
git clone https://github.com/julieschatzsiemers/underwriting-limit-policy-simulation.git
cd underwriting-limit-policy-simulation
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python experiment.py

## How to run
    python3 -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python experiment.py

## Outputs
- [Summary table (CSV)](summary.csv)
- [![Default rate by group](default_rate_by_group.png)](default_rate_by_group.png)
