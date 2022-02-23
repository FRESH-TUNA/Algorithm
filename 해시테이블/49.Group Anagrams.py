class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        db = collections.defaultdict(list)
        
        for str in strs:
            db[tuple(sorted(str))].append(str)
            
        return db.values()
