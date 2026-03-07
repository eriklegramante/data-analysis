SELECT 
    user_id, 
    daily_phone_hours, 
    exam_score,
    stress_level
FROM fact_student_performance
WHERE exam_score < 70 AND daily_phone_hours > 5
ORDER BY stress_level DESC;

SELECT 
    env_condition,
    stress_level,
    AVG(sleep_hours) as media_sono
FROM fact_student_performance
GROUP BY env_condition, stress_level;