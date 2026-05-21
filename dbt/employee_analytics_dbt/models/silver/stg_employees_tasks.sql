select 

task_id,
employee_id,
task_name,

case when task_status IS NULL then 'Unknown' 
     else task_status 
end as task_status,

hours_logged,

cast(created_at as timestamp) as created_at,
cast(updated_at as timestamp) as last_updated,
cast(due_date as timestamp) as due_date,

ingestion_ts

from {{ ref("raw_employees_tasks") }}