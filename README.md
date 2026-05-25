# Employee Attendance & Performance Analytics Platform

An enterprise-style End-to-End Data Engineering project built using Snowflake, dbt, Apache Airflow, and Python to analyze employee attendance, task performance, productivity, and workforce efficiency.

---

## Project Overview

This project simulates a real-world workforce analytics platform where employee data is ingested from APIs, relational databases, and CSV files, then transformed into business-ready analytical models for HR and management reporting.

The platform follows a modern ELT architecture using:
- Snowflake as Cloud Data Warehouse
- dbt for transformations
- Apache Airflow for orchestration
- Python for ingestion pipelines
- SQLAlchemy ORM for database mapping

---

## Business Goal

The platform helps HR and management teams:
- Monitor employee productivity
- Analyze attendance and punctuality
- Track task completion performance
- Identify overdue tasks and work efficiency
- Support appraisal and workforce decision-making

---

# Data Pipelines

## 1. Employee Master Data Pipeline
- Extracts employee data from REST APIs
- Processes nested JSON responses using Python
- Implements ORM-based data mapping
- Handles new and updated employee records
- Scheduled weekly using Apache Airflow

## 2. Employee Task Performance Pipeline
- Extracts task data from PostgreSQL
- Implements incremental loading using dbt incremental models
- Handles insert and update logic using timestamp-based tracking
- Tracks task completion status, overdue tasks, and work-hour utilization
- Scheduled daily using Airflow

## 3. Employee Attendance Pipeline
- Processes attendance datasets from CSV files
- Analyzes punctuality, working hours, and attendance efficiency
- Designed future-ready architecture for AWS S3 + Snowpipe integration
- Supports HR appraisal and workforce analytics

---

# Architecture

```text
Source Systems
 ├── REST APIs
 ├── PostgreSQL
 ├── CSV Files
 │
 ▼
Python Ingestion Layer
 │
 ▼
Snowflake Audit/Bronze Layer
 │
 ▼
dbt Transformations
(Silver Layer)
 │
 ▼
Gold KPI Models
 │
 ▼
HR & Workforce Analytics
```

---

# Medallion Architecture

## Audit/Bronze Layer
- Raw ingestion layer
- Historical source storage
- Staging tables for incremental processing

## Silver Layer
- Data cleansing and standardization
- Deduplication and validation
- Incremental transformations

## Gold Layer
- KPI models
- Productivity analytics
- Attendance insights
- Workforce reporting

---

# Key Features

- End-to-End ELT Pipeline
- Multi-source Data Ingestion
- Incremental Loading Strategy
- dbt Incremental Models
- Airflow Workflow Orchestration
- Snowflake Data Warehouse
- JSON Flattening & Transformation
- ORM-Based Data Mapping
- SCD Type 2 Concepts
- Automated Scheduling & Monitoring

---

# Tech Stack

| Technology | Usage |
|---|---|
| Snowflake | Cloud Data Warehouse |
| dbt | Data Transformation |
| Apache Airflow | Workflow Orchestration |
| Python | Data Ingestion |
| SQLAlchemy ORM | Database Mapping |
| PostgreSQL | Operational Source Database |
| AWS S3 | Future File Storage Integration |
| SQL | Data Processing |
| REST APIs | Employee Data Source |

---

# KPI & Analytics

- Employee Productivity Analysis
- Task Completion Rate
- Overdue Task Monitoring
- Attendance Efficiency
- Punctuality Tracking
- Work-Hour Utilization
- HR Appraisal Insights

---

# Future Enhancements

- Snowflake Streams & Tasks
- Real-time Streaming Pipelines
- Kafka Integration
- Power BI / Tableau Dashboarding
- CI/CD Pipeline Automation
- Advanced Data Quality Monitoring

---

# Project Structure

```text
employee-analytics-platform/
│
├── airflow/
│   ├── dags/
│   └── docker-compose.yaml
│
├── dbt_project/
│   ├── models/
│   ├── macros/
│   └── snapshots/
│
├── scripts/
│   ├── api_ingestion/
│   ├── postgres_ingestion/
│   └── attendance_pipeline/
│
├── datasets/
│
└── README.md
```

---

# Author

**Pratik Vadaviya**  
Aspiring Data Engineer | Snowflake | dbt | Airflow | Python
