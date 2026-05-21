import os

from sqlalchemy import create_engine
from snowflake.connector import connect
import pandas as pd


# PostgreSQL Connection
postgres_host = os.getenv("POSTGRES_HOST", "employee_postgres")
postgres_port = os.getenv("POSTGRES_PORT", "5432")
postgres_user = os.getenv("POSTGRES_USER", "admin")
postgres_password = os.getenv("POSTGRES_PASSWORD", "admin")
postgres_db = os.getenv("POSTGRES_DB", "employee_db")

postgres_engine = create_engine(
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
)

# Fetch Data from PostgreSQL

query = """
SELECT *
FROM tasks
"""

df = pd.read_sql(query, postgres_engine)

print("Data fetched from PostgreSQL:")
print(df.head())


def normalize_timestamp(value):
    if pd.isna(value):
        return None
    return pd.Timestamp(value).to_pydatetime()


def normalize_date(value):
    if pd.isna(value):
        return None
    return pd.Timestamp(value).date()


# Snowflake Connection
snowflake_conn = connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cursor = snowflake_conn.cursor()

print("Connected to Snowflake:")

# Insert Data into Snowflake
insert_query = """
INSERT INTO raw_employees_tasks (
    task_id,
    employee_id,
    task_name,
    task_status,
    hours_logged,
    created_at,
    updated_at,
    due_date
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        (
            int(row['task_id']),
            row['employee_id'],
            row['task_name'],
            row['task_status'],
            float(row['hours_logged']),
            normalize_timestamp(row['created_at']),
            normalize_timestamp(row['updated_at']),
            normalize_date(row['due_date'])
        )
    )

snowflake_conn.commit()

print("Data loaded into Snowflake AUDIT.raw_employees_tasks")

# Close Connections

cursor.close()
snowflake_conn.close()

print("Pipeline completed successfully")