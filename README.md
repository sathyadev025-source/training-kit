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
