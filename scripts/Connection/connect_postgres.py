
import os
from sqlalchemy import create_engine

def build_postgres_connection():

     print("Building PostgreSQL connection...")
     postgres_host = os.getenv("POSTGRES_HOST")
     postgres_port = os.getenv("POSTGRES_PORT")
     postgres_user = os.getenv("POSTGRES_USER")
     postgres_password = os.getenv("POSTGRES_PASSWORD")
     postgres_db = os.getenv("POSTGRES_DB")

     postgres_engine = create_engine(
          f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
     )
     return postgres_engine