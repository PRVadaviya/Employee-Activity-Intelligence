from airflow.sdk import dag,task

@dag(
    dag_id="task_pipeline",
    schedule="@daily",
    catchup=False
)
def task_pipeline():
     @task.bash
     def load_tasks():
         return "python /opt/airflow/scripts/load_tasks_to_snowflake.py"
             
     @task.bash
     def run_dbt_models():
         return "cd /opt/airflow/dbt && dbt run "

     # @task.bash
     # def test_dbt_models():
     #      return "cd /opt/airflow/dbt_project && dbt run --select path:models/*"

     extract_data_from_postgres_snowflake = load_tasks()
     transform_data_with_dbt = run_dbt_models()
     
     extract_data_from_postgres_snowflake >> transform_data_with_dbt

task_pipeline()