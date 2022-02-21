class Solution:
    def trap(self, height: List[int]) -> int:
        stack, answer = [], 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack: break
                distance = i - stack[-1] - 1
                _height = min(height[i], height[stack[-1]]) - height[top]
                answer += distance * _height
            stack.append(i)
        
        return answer