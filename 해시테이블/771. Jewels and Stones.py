class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        db = collections.Counter(stones)
        answer = 0
        
        for jewel in jewels: answer += db[jewel]
        return answer
