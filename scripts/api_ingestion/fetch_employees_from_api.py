import requests
import pandas as pd

def fetch_employee_data():
     url = "https://dummyjson.com/users"

     response = requests.get(url)
     data = response.json()
     print("Fetched employee data from API.")

     df = pd.DataFrame(data['users'])

     # Personal Information

     emp_personal_info = df[
     [
          'firstName',
          'lastName',
          'maidenName',
          'age',
          'gender',
          'email',
          'phone',
          'username',
          'birthDate'
     ]
     ]

     # Company Information

     company_df = pd.json_normalize(df['company'])

     emp_company_info = pd.concat(
     [
          df[['id']],
          company_df[['department', 'title']]
     ],
     axis=1
     )

     # Merge Final Data

     emp_data = pd.concat(
     [emp_company_info, emp_personal_info],
     axis=1
     )

     # Rename Columns

     emp_data.columns = [
     'id',
     'department',
     'title',
     'first_name',
     'last_name',
     'maiden_name',
     'age',
     'gender',
     'email',
     'phone',
     'username',
     'birth_date'
     ]

     # Reorder Columns

     employee_data = emp_data[
     [
          'id',
          'first_name',
          'last_name',
          'maiden_name',
          'age',
          'gender',
          'email',
          'phone',
          'username',
          'birth_date',
          'department',
          'title'
     ]
     ]
     print("fetched employee data from API and transformed it into DataFrame:")
     print(employee_data.head(1))
     return employee_data.head(5)