import sys

class Solution:
    s = None

    def main(self):
        self.init()
        self.solution()

    def init(self):
        input = sys.stdin.readline
        self.s = list(input().rstrip())
        self.res = len(self.s) * 2

    def solution(self):
        for i in range(len(self.s)):
            if self.is_p(i):
                print(i+len(self.s))
                return
        print(len(self.s) * 2)

    def is_p(self, i):
        left, right = i, len(self.s)-1
        while left < right:
            if self.s[left] == self.s[right]:
                left += 1
                right -= 1
            else: return False
        return True

# driver
Solution().main()
