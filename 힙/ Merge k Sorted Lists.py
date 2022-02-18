# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Q = []
        answer, last = None, None
        
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(Q, (node.val, idx, node))
                
        while Q:
            val, idx, node = heapq.heappop(Q)
            
            if not answer:
                answer = ListNode(val)
                last = answer
            else:
                last.next = ListNode(val)
                last = last.next
            
            if node.next:
                heapq.heappush(Q, (node.next.val, idx, node.next))
        
        return answer
            