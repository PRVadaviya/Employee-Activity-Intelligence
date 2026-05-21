SELECT

    id,
    first_name,
    last_name,
    department,
    title,
    age_group

FROM {{ ref("stg_employees_data") }}