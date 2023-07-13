-- select bandname and life span of metal bands

SELECT band_name, date_diff(formed, split) lifespan WHERE style="Glam rock";