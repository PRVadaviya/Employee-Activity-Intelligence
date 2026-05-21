select
employee_id,

sum(case when task_status = 'COMPLETED' then 1 else 0 end) as total_completed_tasks,
sum(case when task_status = 'IN_PROGRESS' then 1 else 0 end) as total_in_progress_tasks,
sum(case when task_status = 'PENDING' then 1 else 0 end) as total_pending_tasks,
from {{ ref("stg_employees_tasks")}}

group by employee_id
