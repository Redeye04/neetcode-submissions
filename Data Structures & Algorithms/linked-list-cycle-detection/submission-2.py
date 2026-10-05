# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashy = {}
        def findn(head, hashy):
            if not head:
                return False

            if head in hashy:
                return True
            else:
                hashy[head] = 0
                return findn(head.next, hashy)
        
        return findn(head, hashy)