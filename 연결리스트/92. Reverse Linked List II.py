# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        
        start = root = ListNode(None)
        root.next = head
        
        for _ in range(left-1):
            start = start.next
            
        end = start.next
        
        for _ in range(right - left):
            sub_head, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = sub_head
            
        return root.next