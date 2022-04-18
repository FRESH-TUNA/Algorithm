SELECT H.hacker_id, H.name, sum(score)
FROM HACKERS H
JOIN (SELECT S_B.hacker_id, S_B.challenge_id, max(score) AS score
      FROM SUBMISSIONS S_B
      WHERE score != 0
      GROUP BY S_B.hacker_id, S_B.challenge_id
     ) SCORES ON SCORES.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name
ORDER BY sum(score) DESC, H.hacker_id ASC;
