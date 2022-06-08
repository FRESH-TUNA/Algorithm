import sys, re

class Solution:
    s = None

    def init(self):
        input = sys.stdin.readline
        self.s = input().rstrip()
        
    def main(self):
        self.init()
        self.solution()

    def solution(self):
        p = re.compile('(100+1+|01)+')
        m = p.fullmatch(self.s)
        if m:
            print("SUBMARINE")
        else:
            print("NOISE")
# driver
Solution().main()
