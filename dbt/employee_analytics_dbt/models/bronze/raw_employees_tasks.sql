
select 
*
from {{ source("AUDIT", "RAW_EMPLOYEES_TASKS") }}
