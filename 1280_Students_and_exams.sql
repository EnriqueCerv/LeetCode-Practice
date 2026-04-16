# Write your MySQL query statement below
SELECT T1.student_id, T1.student_name, T2.subject_name, COUNT(T3.subject_name) AS attended_exams
FROM Students AS T1
CROSS JOIN Subjects AS T2
LEFT JOIN Examinations as T3 ON 
    T1.student_id = T3.student_id
    AND T2.subject_name = T3.subject_name
GROUP BY T1.student_id, T2.subject_name
ORDER BY T1.student_id, T2.subject_name