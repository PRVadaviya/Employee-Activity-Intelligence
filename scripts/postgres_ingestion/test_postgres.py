from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://admin:admin@localhost:5433/employee_db"
)

query = "SELECT * FROM tasks"

df = pd.read_sql(query, engine)

print(df)