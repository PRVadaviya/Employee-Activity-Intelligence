from airflow.sdk import dag,task
from datetime import datetime

@dag(
    dag_id="employee_api_pipeline",
    schedule="@daily"
)
def employee_api_pipeline():
     
     @task.bash
     def fetch_employee_data_from_api():
         return "python /opt/airflow/scripts/api_ingestion/fetch_employees_from_api.py"
             
     @task.bash
     def load_employee_data_to_snowflake():
          return "python /opt/airflow/scripts/api_ingestion/load_employees_data_into_snowflake.py"
     
     @task.bash
     def run_dbt_models():
          return "cd /opt/airflow/dbt && dbt run --select path:models/*"

     extract_data_from_employee_api = fetch_employee_data_from_api()
     load_data_to_snowflake = load_employee_data_to_snowflake()
     transform_data_with_dbt = run_dbt_models()
     
     extract_data_from_employee_api >> load_data_to_snowflake >> transform_data_with_dbt

employee_api_pipeline()