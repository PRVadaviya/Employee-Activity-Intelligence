
USE ROLE ACCOUNTADMIN;

USE WAREHOUSE COMPUTE_WH;

USE SCHEMA EMP_ANALYTICS.AUDIT;

CREATE OR REPLACE TABLE AUDIT.raw_employees_tasks (
    task_id INTEGER,
    employee_id STRING,
    task_name STRING,
    task_status STRING,
    hours_logged FLOAT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    due_date DATE,
    ingestion_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);