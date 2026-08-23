# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l2.val == 0:
            return l1

        n1 = 0
        n2 = 0

        place = 1
        while l1 != None:
            n1 += l1.val * place
            place *= 10
            l1 = l1.next

        place = 1
        while l2 != None:
            n2 += l2.val * place
            place *= 10
            l2 = l2.next
        
        ans = str(n1 + n2)[::-1]
        l3 = ListNode()
        curr = l3

        for i in range(0, len(ans)):
            if i == len(ans) - 1:
                l3.val = ans[i]
                l3.next = None
                break

            l3.val = int(ans[i])
            l3.next = ListNode()
            l3 = l3.next

        return curr
