class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left+1, right)

        answer = (0, 1)

        for i in range(len(s)):
            answer = max(
                answer, extend(i, i+1), extend(i, i+2),
                key=lambda x: x[1]-x[0]
            )
        
        return s[answer[0]:answer[1]]
