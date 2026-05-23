import os

# from dotenv import load_dotenv     # for the airflow environment take from the .env file, but if run in local then uncommit line
from snowflake.connector import connect

# Load environment variables from .env file
# load_dotenv()                      # for the airflow environment take from the .env file, but if run in local then uncommit line

def build_snowflake_connection():
     print("Building Snowflake connection...")
     
     snowflake_connection = connect(
          user=os.getenv("SNOWFLAKE_USER"),
          password=os.getenv("SNOWFLAKE_PASSWORD"),
          account=os.getenv("SNOWFLAKE_ACCOUNT"),
          warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
          database=os.getenv("SNOWFLAKE_DATABASE"),
          schema=os.getenv("SNOWFLAKE_SCHEMA")
     )

     cursor = snowflake_connection.cursor()

     print("Connected to Snowflake:")

     return snowflake_connection, cursor