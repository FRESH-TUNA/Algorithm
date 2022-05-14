class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        db = Counter()
        
        for s in sorted(strs, key=len, reverse=True):
            for i in range(len(s), -1, -1):
                db[s[:i]] += 1
        
        res = db.most_common()
        return [res[0][0], ""][res[0][1] != len(strs)]
