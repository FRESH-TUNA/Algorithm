class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        
        for v in intervals[1:]:
            if answer[-1][1] >= v[0]:
                _v = answer.pop()
                answer.append([_v[0], max(v[1],_v[1])])
            else: answer.append(v)
        
        return answer