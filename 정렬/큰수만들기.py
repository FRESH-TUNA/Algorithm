class Solution:
    def compare(self, a, b):
        return int(b+a) - int(a+b)

    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join(sorted([str(n) for n in nums],
            key=functools.cmp_to_key(self.compare)))))
        