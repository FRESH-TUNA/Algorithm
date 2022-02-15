class Solution:
    def minWindow(self, s: str, t: str) -> str:
        BORDER = 100001
        db = collections.Counter(t)
        target_size = len(t)
        start, end = 0, BORDER
        left = 0
        
        for right, value in enumerate(s):
            target_size -= db[value] > 0
            db[value] -= 1

            if target_size == 0:
                while left < right+1 and db[s[left]] < 0:
                    db[s[left]] += 1
                    left += 1
                if right-left+1 < end-start:
                    start, end = left, right+1
                    db[s[left]] += 1
                    left += 1
                    target_size += 1

        return "" if end == BORDER else s[start:end]