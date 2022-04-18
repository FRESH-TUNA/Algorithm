SET @max_c := (SELECT MAX(e.c) max_c FROM (SELECT hacker_id, COUNT(*) c FROM challenges GROUP BY hacker_id) e);

SELECT d.hacker_id, d.name, b.c FROM
(
  SELECT hacker_id, COUNT(*) c FROM challenges GROUP BY hacker_id
) b
JOIN(
  SELECT f.c, COUNT(*) co FROM (SELECT hacker_id, COUNT(*) c FROM challenges GROUP BY hacker_id) f GROUP BY f.c
) c ON c.c = b.c
JOIN hackers d ON d.hacker_id = b.hacker_id
WHERE c.co < 2 OR  c.c = @max_c
ORDER BY b.c DESC, d.hacker_id