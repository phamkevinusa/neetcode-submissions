"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}

        curr = head
        while curr: #pass 1 add copies to hashmap
            copy = Node(curr.val) #create basic copy of node, no pointers
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            #point to the correct copy node
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random=oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
