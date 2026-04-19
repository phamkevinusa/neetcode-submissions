# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def calc(l1, l2, carry):
            num = 0
            if not l1 and not l2 and carry == 0:
                return None
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            num += carry

            carry = num // 10 #grab 10s digit
            num = num % 10 #reduce to 1s digit


            return ListNode(num, calc(l1, l2, carry))

        return calc(l1, l2, 0)
        