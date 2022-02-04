class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer, cur = ListNode(head.val), head.next
        while cur: 
            answer, cur = self.insert(answer, cur.val), cur.next
        return answer
            
    def insert(self, answer, new_value):
        prev, curr = None, answer
        new_node = ListNode(new_value)
        
        while curr:
            if curr.val <= new_value:
                prev, curr = curr, curr.next
                continue
            if prev == None:
                new_node.next = curr
                return new_node
            else:
                prev.next = new_node
                new_node.next = curr
                return answer
        
        prev.next = new_node
        return answer
                