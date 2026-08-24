# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        r = head
        lent = 1
        l = head
        prev = None
        while n != 0:
            r = r.next
            n -= 1

        while r != None:
            prev = l
            l = l.next
            r = r.next

        if prev == None:
            return head.next

        prev.next = l.next
        l.next = None

        return head    
                