class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, l1_stack, l2_stack = 0, [], []
        ans = tail = ListNode

        while carry or l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            result = carry + l1_val + l2_val
            carry, new_val = result // 10, result % 10
            tail.next = ListNode()
            tail = tail.next
            tail.val = new_val
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return ans.next
        