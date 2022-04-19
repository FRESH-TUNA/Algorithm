/*
Enter your query here.
*/
SET @max := (
    SELECT max(t.c)
    FROM (SELECT hacker_id, count(*) c FROM CHALLENGES GROUP BY hacker_id) t
);

SELECT HACKERS.hacker_id, HACKERS.name, t2.c
FROM (SELECT hacker_id, count(*) c FROM CHALLENGES GROUP BY hacker_id) t2 
JOIN HACKERS ON HACKERS.hacker_id = t2.hacker_id
JOIN (SELECT c, count(*) cc
      FROM (SELECT hacker_id, count(*) c FROM CHALLENGES GROUP BY hacker_id) t3
      GROUP BY c) t4 ON t4.c = t2.c
WHERE t2.c = @max or t4.cc = 1
ORDER BY t2.c DESC, HACKERS.hacker_id ASC
