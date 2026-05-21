
select 
     DATE(checkin_time) AS attendance_date,
     count(*) as total_employees,
     count(case when checkin_status = 'Early' then 1 end) as early_checkins,
     count(case when checkin_status = 'On Time' then 1 end) as on_time_checkins,
     count(case when checkin_status = 'Late' then 1 end) as late_checkins
from {{ ref("stg_attendance") }}
group by DATE(checkin_time)