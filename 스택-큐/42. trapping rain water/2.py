class Solution:
    def trap(self, height: List[int]) -> int:
        stack, answer = [], 0
        
        for right_height_idx, right_height in enumerate(height):
            while stack and right_height > height[stack[-1]]:
                left_height_idx = stack.pop()
                min_height = height[left_height_idx]
                
                while stack and height[stack[-1]] == min_height:
                    stack.pop()
                    
                if stack: left_height_idx = stack[-1]
                
                width = right_height_idx - left_height_idx - 1
                _height = min(right_height, height[left_height_idx]) - min_height
                answer += width * _height

            stack.append(right_height_idx)
                
        return answer