select h.hacker_id,h.name 
from hackers h
JOIN submissions s ON h.hacker_id=s.hacker_id
JOIN challenges c ON c.challenge_id=s.challenge_id
JOIN difficulty d ON c.difficulty_level=d.difficulty_level
where s.score=d.score
group by h.hacker_id, h.name having  count(h.hacker_id) > 1
order by count(c.challenge_id) desc, h.hacker_id
