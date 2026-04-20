🏦 Automated Finance Branch Performance Pipeline (ELT)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Airflow](https://img.shields.io/badge/Airflow-2.x-green)
![dbt](https://img.shields.io/badge/dbt-1.x-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue)
![Meltano](https://img.shields.io/badge/Meltano-ELT-purple)
📌 Project Overview
An end-to-end ELT data engineering pipeline that automates the extraction, loading, and transformation of daily branch-level finance records (targets vs actuals). Built using the Modern Data Stack on a local Linux (WSL2) environment.
This project simulates a real-world NBFC/banking scenario — branch sales performance data flows from raw Excel files through Meltano into PostgreSQL, where dbt models transform it into clean, reportable tables orchestrated by Apache Airflow.
---
🛠️ Tech Stack
Layer	Tool
Orchestration	Apache Airflow
Ingestion	Meltano
Transformation	dbt (data build tool)
Database	PostgreSQL
Environment	Ubuntu on WSL2
Source Data	Excel files (branch performance)
---
🏗️ Architecture
```
Excel Files (Branch Targets \& Actuals)
        ↓
Meltano (Extract \& Load → PostgreSQL raw schema)
        ↓
dbt (Transform → clean models, aggregations, tests)
        ↓
PostgreSQL (Final reporting tables)
        ↓
Airflow DAG (Orchestrates full pipeline on schedule)
```
---
📈 Database Schema
The pipeline produces the following transformed tables in PostgreSQL:
`stg\_branch\_performance` — Cleaned and typed staging layer from raw Excel data
`fct\_branch\_summary` — Aggregated branch-wise actuals vs targets
`fct\_top\_performers` — Ranked branches by achievement percentage
`fct\_target\_gap` — Branches with highest gap between target and actual
---
🚀 Key Features
Automated Scheduling — Daily Airflow DAGs run the full pipeline without manual intervention
Data Quality Tests — dbt tests validate nulls, uniqueness, and referential integrity
Domain-Driven Modeling — Data modeled to reflect real NBFC branch reporting structure
Error Handling — Custom Airflow paths and dbt profiles configured for local WSL2 environment
---
📁 Project Structure
```
finance-branch-pipeline/
├── data/
│   └── branch\_performance.xlsx       # Sample source data
├── meltano/
│   └── meltano.yml                   # Meltano ELT config
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg\_branch\_performance.sql
│   │   └── marts/
│   │       ├── fct\_branch\_summary.sql
│   │       ├── fct\_top\_performers.sql
│   │       └── fct\_target\_gap.sql
│   ├── tests/
│   └── dbt\_project.yml
├── airflow/
│   └── dags/
│       └── finance\_pipeline\_dag.py   # Main Airflow DAG
├── requirements.txt
└── README.md
```
---
⚙️ How to Run
Prerequisites
Python 3.10+
PostgreSQL running locally
WSL2 (Ubuntu)
Setup
```bash
# Clone the repo
git clone https://github.com/sathyadev025-source/finance-branch-pipeline.git
cd finance-branch-pipeline

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
Run with Airflow
```bash
# Set Airflow home
export AIRFLOW\_HOME=\~/projects/finance-branch-pipeline/airflow\_home

# Initialize Airflow
airflow db init

# Start scheduler
airflow scheduler
```
Run dbt Transformations
```bash
cd dbt
dbt run
dbt test
```
---
📊 Sample Data
Branch performance data includes:
Branch Name & Region
Target Amount (monthly)
Actual Disbursement
Achievement %
Product Category (Home Loan, Personal Loan, etc.)
---
🎯 Business Value
This pipeline replicates a real reporting workflow used in NBFC/banking environments — where branch managers and regional heads track daily performance against targets. Automating this with a modern ELT stack eliminates manual Excel reporting and enables near-real-time visibility.
---
👤 Author
Sathya Moorthi R  
GitHub | LinkedIn
