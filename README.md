# Automated Finance Data Pipeline (ETL)

## 📌 Project Overview
An end-to-end data engineering pipeline that automates the extraction, loading, and transformation of daily finance records. This project demonstrates a "Modern Data Stack" approach using containerized-style orchestration on a local Linux (WSL2) environment.

## 🛠️ Tech Stack
* **Orchestrator:** Apache Airflow (Python-based DAGs)
* **Ingestion:** Meltano (ELT tool for seamless data movement)
* **Transformation:** dbt (data build tool) for SQL modeling
* **Database:** PostgreSQL (Target Data Warehouse)
* **Environment:** Ubuntu on WSL2

## 🚀 Key Features
* **Automated Scheduling:** Daily DAGs handle data updates without manual intervention.
* **Data Quality:** Integrated dbt tests to ensure data integrity during transformation.
* **Error Handling:** Configured custom Airflow paths and profiles to manage local environment constraints.

## 📈 Database Schema
The pipeline transforms raw Excel/CSV data into a structured format in PostgreSQL, focusing on aggregate reporting and financial analysis.

---

## 🏏 Project 2: Cricket T20 Data Pipeline (Modern Data Stack)

An automated Data Engineering pipeline that extracts raw ball-by-ball T20 match data, processes it locally, and loads it into a database for visual analytics.

### 🛠️ Tech Stack
* **Orchestration:** Apache Airflow
* **Database:** PostgreSQL
* **Processing:** Python (Pandas & SQLAlchemy)
* **Visualization:** Metabase

### 🏗️ Architecture
1. **Extract:** Python extracts raw JSON ball-by-ball match data from Cricsheet.
2. **Transform:** Pandas cleans the data, handles missing values, and structures delivery records.
3. **Load:** Automatically inserts records into a local Postgres database (successfully loaded **45,734+ rows**).
4. **Orchestrate:** An Airflow DAG schedules and runs the pipeline automatically using a `BashOperator`.
5. **Visualize:** Native Metabase instance aggregates metrics like Strike Rate and Bowler Economy.

### 🚀 How to Run Cricket Pipeline
1. Make sure you are in the virtual environment: `source .venv-airflow/bin/activate`
2. Ensure Airflow is running: `export AIRFLOW_HOME=~/projects/training-kit/airflow_home && airflow scheduler`
3. Run Metabase: `java -jar metabase.jar`
