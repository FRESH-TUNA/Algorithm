class Solution:
    stack = []
    
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.trace(n, 0, 0, answer)
        return answer
    
    def trace(self, n, left, remain_left, answer):
        if len(self.stack) == n*2:
            answer.append(''.join(self.stack))
            return
        if remain_left: 
            self.stack.append(")")
            self.trace(n, left, remain_left-1, answer)
            self.stack.pop()
        if left != n:
            self.stack.append("(")
            self.trace(n, left+1, remain_left+1, answer)
            self.stack.pop()
