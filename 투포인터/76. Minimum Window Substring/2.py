class Solution:
    def minWindow(self, s: str, t: str) -> str:
        BORDER = 100001
        start, end = 0, BORDER
        left = 0
        db = collections.Counter(t)
        db_size = len(t)

        for right, value in enumerate(s, 1):
            db_size -= db[value] > 0
            db[value] -= 1
            
            if not db_size:
                while left < right and db[s[left]] < 0:
                    db[s[left]] += 1
                    left += 1
                if right - left <= end - start:
                    start, end = left, right
                    db[s[left]] += 1
                    left += 1
                    db_size += 1

        return "" if end == BORDER else s[start:end]