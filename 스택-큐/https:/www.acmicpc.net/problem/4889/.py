import sys, re

class Solution:
    def init(self):
        input = sys.stdin.readline
        s = []
        while True:
            _s = input().rstrip()
            if "-" in _s: break
            else: s.append(_s)
        return s

    def main(self):
        print('\n'.join([self.solution(i, s) for i, s in enumerate(self.init())]))

    def solution(self, i, s):
        stack, res = 0, 0

        for c in s:
            if c == '{': stack += 1
            elif stack == 0: 
                res += 1
                stack += 1
            else: stack -= 1
        return str(i+1) + '. ' + str(res + stack // 2)       
        
        
# driver
Solution().main()
