SELECT DISTINCT num ConsecutiveNums
FROM LOGS
WHERE (id+1, num) in (SELECT * from Logs) and (id+2, num) in (SELECT * from Logs)
