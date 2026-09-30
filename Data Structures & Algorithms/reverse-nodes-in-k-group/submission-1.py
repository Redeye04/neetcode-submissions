# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gprev = dummy

        while True:
            kth = self.getk(gprev, k)
            if not kth:
                return dummy.next

            gnext = kth.next
            prev, curr = gnext, gprev.next
            while curr != gnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = gprev.next
            gprev.next = kth
            gprev = temp
        
    def getk(self, root, k):
        while root and k > 0:
            root = root.next
            k -= 1
        return root