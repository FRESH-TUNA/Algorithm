class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        answer = 0
        
        for price in prices[1:]:
            if price - minimum > answer: answer = price - minimum
            minimum = min(minimum, price)
            
        return answer
