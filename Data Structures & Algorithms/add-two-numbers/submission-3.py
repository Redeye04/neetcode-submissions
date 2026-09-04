# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        place = 1
        num1 = 0
        while l1:
            num1 += l1.val * place
            place *= 10
            l1 = l1.next

        place = 1
        num2 = 0
        while l2:
            num2 += l2.val * place
            place *= 10
            l2 = l2.next
        
        num3 = str((int(num1)+int(num2)))
        nums = ListNode()
        curr = nums
        print(num1, num2, num3)
        for i in range(len(num3)-1, 0, -1):
            curr.val = int(num3[i])
            curr.next = ListNode()
            curr = curr.next
        curr.val = num3[0]
        return nums
        

        