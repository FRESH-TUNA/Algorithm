#https://leetcode.com/problems/daily-temperatures/submissions/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                ans_index = stack.pop()
                answer[ans_index] = index - ans_index
            stack.append(index)
            
        return answer