"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# O(n) - Time
# O(n) - Space
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        CopyHashy = {None: None}
        curr = head

        while curr:
            Copy = Node(curr.val)
            CopyHashy[curr] = Copy
            curr = curr.next
        
        curr = head
        while curr:
            cpy = CopyHashy[curr]
            cpy.next = CopyHashy[curr.next]
            cpy.random = CopyHashy[curr.random]
            curr = curr.next
        
        return CopyHashy[head]