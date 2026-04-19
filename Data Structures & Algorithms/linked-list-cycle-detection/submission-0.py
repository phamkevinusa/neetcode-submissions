# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 2 pointers at different speeds method
        if not head:
            return False
        
        p1 = head
        p2 = head.next

        while p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return False
            p2 = p2.next
            if p2 == p1:
                return True
        return False