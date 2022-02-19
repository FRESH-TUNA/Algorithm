class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        db = collections.defaultdict(set)
        for index, num in enumerate(nums):
            db[num].add(index)
            
        for index, num in enumerate(nums):
            compared = target - num
            if compared not in db: continue
            for _index in db[compared]:
                if _index != index:
                    return [index, _index]