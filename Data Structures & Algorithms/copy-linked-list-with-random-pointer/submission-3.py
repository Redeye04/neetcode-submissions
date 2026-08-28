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
        hashy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            hashy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = hashy[curr]
            copy.next = hashy[curr.next]
            copy.random = hashy[curr.random]
            curr = curr.next
        
        return hashy[head]