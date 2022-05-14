class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = dict()
        root[""] = {"size": len(strs), "next": dict()}
        strs = sorted(strs, key=len)
        
        for s in strs:
            pointer = root[""]["next"]
            for c in s:
                if c in pointer:
                    pointer[c]["size"] += 1
                else:
                    pointer[c] = {"size": 1, "next": dict()}
                pointer = pointer[c]["next"]
        
        
        pointer = root[""]["next"]
        for right, c in enumerate(strs[0]):
            if pointer[c]["size"] != len(strs):
                return strs[0][:right]
            pointer = pointer[c]["next"]
        return strs[0]
