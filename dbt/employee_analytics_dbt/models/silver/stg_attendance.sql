
select
*,
datediff(hour, checkin_time, checkout_time) as hours_worked,
case 
     when date_part(hour, checkin_time) < 9 then 'Early'
     when date_part(hour, checkin_time) >= 9 and date_part(hour, checkin_time) <= 10 then 'On Time'
     else 'Late'
end as checkin_status
from {{ ref("raw_attendance") }}