SELECT 
    T1.user_id, 
    IFNULL(
        ROUND(
            SUM(T2.action = 'confirmed') / COUNT(T2.action), 2
            ), 0
        ) AS confirmation_rate
FROM Signups as T1
LEFT JOIN Confirmations AS T2 ON T1.user_id = T2.user_id
GROUP BY T1.user_id