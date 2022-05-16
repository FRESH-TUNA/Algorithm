SELECT score, (SELECT COUNT(*) FROM (SELECT DISTINCT score FROM SCORES) tmp where s.score <= tmp.score) "RANK"
FROM SCORES s
ORDER BY score DESC
