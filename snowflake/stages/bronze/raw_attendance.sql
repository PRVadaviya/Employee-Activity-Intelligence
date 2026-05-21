USE ROLE ACCOUNTADMIN;

USE WAREHOUSE COMPUTE_WH;

USE SCHEMA EMP_ANALYTICS.BRONZE;

CREATE OR REPLACE STAGE RAW_ATTENDANCE_STAGE;

// IF this internal stage is not working is your case load data using Snowflake UI
PUT file://E:/Projects/Employee-Activity-Intelligence/datasets/attendance/attendance.csv @RAW_ATTENDANCE_STAGE;

LIST @RAW_ATTENDANCE_STAGE;

copy into raw_attendance
from @RAW_ATTENDANCE 
FILE_FORMAT = (
     TYPE='CSV' 
     SKIP_HEADER = 1 
     FIELD_DELIMITER = ',')

SELECT * from raw_attendance;