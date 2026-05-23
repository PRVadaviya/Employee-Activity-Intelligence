
{{ config(
	materialized='table',
	pre_hook="truncate table if exists {{ this }}"
) }}

select
* 
from {{ source('AUDIT', 'RAW_EMPLOYEES_DATA') }}