SELECT score, DENSE_RANK() OVER (ORDER BY Score DESC) 'rank'
From Scores
