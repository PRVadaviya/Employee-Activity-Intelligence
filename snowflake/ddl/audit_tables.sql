
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

CREATE OR REPLACE TABLE BRONZE.raw_employees (

    id INTEGER,
    first_name STRING,
    last_name STRING,
    maiden_name STRING,
    age INTEGER,
    gender STRING,
    email STRING,
    phone STRING,
    username STRING,
    birth_date DATE,
    department STRING,
    title STRING,
    ingestion_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);