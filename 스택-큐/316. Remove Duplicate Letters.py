class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        db = collections.Counter(s)
        answer = []
        answer_set = set()
        
        for c in s:
            db[c] -= 1
            if c in answer_set: continue
            
            while answer and answer[-1] > c and db[answer[-1]] > 0:
                answer_set.remove(answer.pop())
            answer.append(c)
            answer_set.add(c)
        return ''.join(answer)
