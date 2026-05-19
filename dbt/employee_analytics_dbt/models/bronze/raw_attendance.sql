
select 
*
from {{ source("AUDIT", "RAW_ATTENDANCE") }}
