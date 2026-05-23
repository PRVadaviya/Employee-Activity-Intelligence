import pandas as pd

def fetch_tasks_from_postgres(postgres_engine):
     
     print("Fetching tasks data from PostgreSQL...")
     # Fetch Data from PostgreSQL
     query = """
     SELECT *
     FROM tasks
     """

     tasks_data = pd.read_sql(query, postgres_engine)

     print("Data fetched from PostgreSQL:")
     print(tasks_data.head(1))

     return tasks_data