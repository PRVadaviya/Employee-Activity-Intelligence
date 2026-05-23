select 
     id,

     trim(first_name) as first_name,
     trim(last_name) as last_name,

     case 
          when trim(maiden_name) is null or trim(maiden_name) = '' then 'NO_MAIDEN_NAME'
          else trim(maiden_name)
     end as maiden_name,

     age,

         CASE
        WHEN age < 30 THEN 'YOUNG'
        WHEN age < 45 THEN 'MID'
        ELSE 'SENIOR'
    END AS age_group,

     upper(gender) as gender,

     ifnull(trim(email), 'NO_EMAIL') as email,
     ifnull(trim(phone), 'NO_PHONE') as phone,
     ifnull(trim(username), 'NO_USERNAME') as username,

     birth_date,

     UPPER(department) as department,
     UPPER(title) as title
     
from {{ ref("raw_employees_data") }}