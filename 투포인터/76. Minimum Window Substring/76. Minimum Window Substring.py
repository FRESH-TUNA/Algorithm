class Solution:
    def minWindow(self, s: str, t: str) -> str:
        BORDER = 100001
        compareto = collections.Counter(t)
        db = collections.Counter(s[0])
        start, end = 0, 1
        answer = [0, BORDER]

        while start < end:
            if compareto <= db:
                answer = min(answer, (start, end), 
                             key=lambda x: x[1]-x[0])
                db[s[start]] -= 1
                start += 1
                continue
            
            if end == len(s): break
            else: 
                db[s[end]] += 1
                end += 1
  
        start, end = answer
        return "" if end == BORDER else s[start:end]
