# https://leetcode.com/problems/letter-combinations-of-a-phone-number
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        db = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        return [] if digits == "" else ["".join(x) 
            for x in product(*[list(db[x]) for x in list(digits)])]
