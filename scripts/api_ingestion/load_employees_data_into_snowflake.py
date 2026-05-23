from connect_snowflake import build_snowflake_connection
from fetch_employees_from_api import fetch_employee_data

employee_data = fetch_employee_data()
snowflake_connection, cursor = build_snowflake_connection()

def load_employee_data_to_snowflake():
     # Truncate the target table before inserting new data
     truncate_query = "TRUNCATE TABLE raw_employees_data"
     cursor.execute(truncate_query)

     print("Truncated raw_employees table.")
     # Insert Data into Snowflake
     insert_query = """
     INSERT INTO raw_employees_data (
     id,
     first_name,
     last_name,
     maiden_name,
     age,
     gender,
     email,
     phone,
     username,
     birth_date,
     department,
     title
     )
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
     """

     data_to_insert = [
     (
          int(row['id']),
          row['first_name'],
          row['last_name'],
          row['maiden_name'],
          int(row['age']),
          row['gender'],
          row['email'],
          row['phone'],
          row['username'],
          row['birth_date'],
          row['department'],
          row['title']
     )
     for _, row in employee_data.iterrows()
     ]

     cursor.executemany(insert_query, data_to_insert)
     print("Inserted employee data into Snowflake.")

     snowflake_connection.commit()
     print("Employee data loaded into Snowflake successfully.")

load_employee_data_to_snowflake()