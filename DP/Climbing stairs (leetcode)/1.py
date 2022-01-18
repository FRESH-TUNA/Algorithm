class Solution:
    def climbStairs(self, n: int) -> int:
        anss = [0, 1, 2] + [0] * 43
        for i in range(3, n+1):
            anss[i] = anss[i-1] + anss[i-2]
        return anss[n]
