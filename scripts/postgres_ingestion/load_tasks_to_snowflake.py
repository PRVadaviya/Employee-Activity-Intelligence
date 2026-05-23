import pandas as pd

# PostgreSQL Connection
from scripts.Connection.connect_postgres import build_postgres_connection
postgres_engine = build_postgres_connection()

# Snowflake Connection
from ..Connection.connect_snowflake import build_snowflake_connection
snowflake_connection, cursor = build_snowflake_connection()

# Fetch Data from PostgreSQL
from scripts.postgres_ingestion.fetch_tasks_from_database import fetch_tasks_from_postgres
df = fetch_tasks_from_postgres(postgres_engine)

def normalize_timestamp(value):
    if pd.isna(value):
        return None
    return pd.Timestamp(value).to_pydatetime()


def normalize_date(value):
    if pd.isna(value):
        return None
    return pd.Timestamp(value).date()


# Load Data into Snowflake
def load_employee_tasks_to_snowflake():
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

    snowflake_connection.commit()
    print("Data loaded into Snowflake AUDIT.raw_employees_tasks")

    # Close Connections
    cursor.close()
    snowflake_connection.close()

    print("Pipeline completed successfully")

load_employee_tasks_to_snowflake()