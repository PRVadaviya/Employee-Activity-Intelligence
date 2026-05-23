from airflow.sdk import dag,task

@dag(
    dag_id="task_pipeline",
    schedule="@daily",
    catchup=False
)
def task_pipeline():
    @task.bash
    def fetch_tasks_data_from_database():
        return "python /opt/airflow/scripts/postgres_ingestion/fetch_tasks_from_database.py"

    @task.bash
    def load_tasks_to_snowflake():
        return "python /opt/airflow/scripts/postgres_ingestion/load_tasks_to_snowflake.py"
          
    @task.bash
    def transform_data():
        return "cd /opt/airflow/dbt && dbt run --select path:models/*"

    extract_data_from_postgres_snowflake = fetch_tasks_data_from_database()
    load_data_to_snowflake = load_tasks_to_snowflake()
    transform_tasks = transform_data()
     
    extract_data_from_postgres_snowflake >> load_data_to_snowflake >> transform_tasks

task_pipeline()