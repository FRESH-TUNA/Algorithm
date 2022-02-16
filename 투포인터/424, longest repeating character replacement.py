class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        db = collections.Counter()
        left = right = 0
        
        for right, v in enumerate(s, 1):
            db[v] += 1
            most_chars = db.most_common(1)[0][1]
            if right - left - most_chars > k:
                db[s[left]] -= 1
                left -= 1

        return right - left
