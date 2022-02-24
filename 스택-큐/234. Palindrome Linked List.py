# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Q = deque()
        while head: 
            Q.append(head.val)
            head = head.next

        while len(Q) > 1:
            if Q.pop() != Q.popleft(): return False
        
        return True
