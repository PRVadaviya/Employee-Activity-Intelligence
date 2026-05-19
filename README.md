# Employee Analytics Platform

A production-style end-to-end Data Engineering project built using Snowflake, dbt, Apache Airflow, Python, and AWS S3.

This project simulates a real-world Employee Attendance & Performance Management System used by HR managers and leadership teams to monitor attendance, productivity, task completion, and appraisal insights.

---

# Project Objective

The goal of this project is to design and build a scalable modern data platform that:

- Ingests data from multiple enterprise sources
- Applies ELT transformations using dbt
- Implements Medallion Architecture (Bronze → Silver → Gold)
- Uses Airflow for orchestration
- Builds analytics-ready dimensional models
- Supports incremental loading and SCD Type 2
- Generates business KPIs for reporting

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Snowflake | Cloud Data Warehouse |
| dbt | Data Transformation |
| Apache Airflow | Workflow Orchestration |
| Python | Data Ingestion & Automation |
| AWS S3 | Raw Data Storage |
| PostgreSQL | Source Database |
| SQLAlchemy | ORM / Database Connectivity |

---

# Architecture

```text
Sources
(API / PostgreSQL / CSV / JSON)
        ↓
Python Extraction Layer
        ↓
AWS S3 Staging
        ↓
Snowflake Bronze Layer
        ↓
dbt Silver Transformations
        ↓
dbt Gold Layer (Facts & Dimensions)
        ↓
KPIs / Dashboards
```

---

# Data Sources

## 1. Attendance API
- Daily attendance logs
- Employee check-in/check-out data

## 2. PostgreSQL Task Database
- Task assignments
- Work logs
- Task completion status

## 3. HR Files from S3
- Employee master data
- Department
- Appraisal information

## 4. Activity Logs
- Login/logout events
- Employee activity tracking

---

# Medallion Architecture

## Bronze Layer
Raw ingestion layer.

- Append-only
- Minimal transformation
- Raw source preservation

Tables:
- raw_attendance
- raw_tasks
- raw_employees
- raw_activity_logs

---

## Silver Layer
Cleaned and standardized layer.

Features:
- Type casting
- Deduplication
- Null handling
- Business rules

Models:
- stg_attendance
- stg_tasks
- stg_employees

---

## Gold Layer
Analytics-ready business layer.

Features:
- Star schema
- Fact tables
- Dimension tables
- KPI aggregations
- SCD Type 2

Tables:
- fact_attendance
- fact_task_log
- dim_employee
- dim_date
- kpi_attendance_daily

---

# Key Features

- Multi-source ingestion
- Incremental loading
- SCD Type 2 snapshots
- Airflow DAG orchestration
- dbt tests & documentation
- Snowflake Streams & Tasks
- Data quality checks
- KPI reporting layer
- RBAC & security
- Monitoring & logging

---

# Airflow DAGs

| DAG | Purpose |
|---|---|
| dag_attendance_ingestion | Attendance API ingestion |
| dag_task_ingestion | PostgreSQL task ingestion |
| dag_hr_file_ingestion | S3 HR file ingestion |
| dag_dbt_transform | dbt model execution |
| dag_data_quality | Data validation checks |

---

# dbt Features Used

- Incremental Models
- Snapshots
- Seeds
- Macros
- Tests
- Sources
- Documentation

---

# Snowflake Features Used

- Warehouses
- External Stages
- File Formats
- Snowpipe
- Streams & Tasks
- Time Travel
- RBAC
- Clustering

---

# Folder Structure

```text
employee-analytics-platform/
│
├── airflow/
│   ├── dags/
│   └── logs/
│
├── dbt_project/
│   ├── models/
│   ├── snapshots/
│   ├── tests/
│   ├── macros/
│   └── seeds/
│
├── snowflake/
│   ├── ddl/
│   ├── stages/
│   ├── pipes/
│   └── roles/
│
├── scripts/
│
├── datasets/
│
├── docs/
│
└── README.md
```

---

# KPIs Generated

- Attendance Rate
- Late Login Percentage
- Average Work Hours
- Task Completion Rate
- Department Productivity
- Monthly Productivity Score
- Appraisal Readiness

---

# Future Improvements

- Kafka streaming ingestion
- CI/CD pipeline
- Docker deployment
- Terraform infrastructure
- Real-time dashboards
- Kubernetes deployment

---

# How to Run

## 1. Clone Repository

```bash
git clone <repo-url>
```

## 2. Setup Python Environment

```bash
pip install -r requirements.txt
```

## 3. Configure Snowflake Connection

Update:
- profiles.yml
- Airflow Connections

## 4. Run Airflow

```bash
airflow standalone
```

## 5. Run dbt

```bash
dbt run
dbt test
```

---

# Project Status

🚧 In Development

Current Progress:
- [ ] Snowflake setup
- [ ] Bronze ingestion
- [ ] dbt staging models
- [ ] Gold marts
- [ ] Airflow DAGs
- [ ] KPI dashboards

---

# Author

Pratik Vadaviya

Aspiring Data Engineer | Snowflake | dbt | Airflow | Python | SQL