# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(nums, start, end):
            if start == end:
                return TreeNode(nums[start])

            mid = (start + end) // 2
            return TreeNode(
                nums[mid],
                None if mid == start else makeBST(nums, start, mid-1),
                makeBST(nums, mid+1, end) 
            )
        
        return makeBST(nums, 0, len(nums)-1)