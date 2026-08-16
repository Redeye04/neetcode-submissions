# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashy = {}
        
        while head != None:
            if head.val in hashy and head.next != None:
                return True
            hashy[head.val] = 1
            head = head.next
            
        
        return False