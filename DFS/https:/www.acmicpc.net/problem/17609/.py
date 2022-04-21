import sys

class Solution:
    N, WORDS = None, None
    
    def main(self):
        self.init()
        self.solutions()

    def init(self):
        input = sys.stdin.readline
        self.N = int(input())
        self.WORDS = [input().rstrip() for _ in range(self.N)]

    def solutions(self):
        for i in range(self.N):
            print(self.solution(self.WORDS[i]))

    def solution(self, word):
        return self.dfs(word, 0, len(word)-1, 0)

    def dfs(self, word, start, end, cnt):
        while start < end:
            if word[start] == word[end]: 
                start += 1
                end -= 1
                continue
            
            if cnt == 1: return 2

            start_res = self.dfs(word, start+1, end, 1)
            end_res = self.dfs(word, start, end-1, 1)

            if start_res != 2: return start_res
            if end_res != 2: return end_res
            return 2 
        return 0 if cnt == 0 else 1
# driver
Solution().main()
