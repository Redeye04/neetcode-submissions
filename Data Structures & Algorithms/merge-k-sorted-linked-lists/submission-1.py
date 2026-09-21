# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedL = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedL.append(self.sortedL(l1, l2))
            lists = mergedL[:]
        
        return lists[0]
        
    
    def sortedL(self, list1, list2):
        root = ListNode()
        curr = root

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            elif list1.val > list2.val:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = ListNode(list2.val, ListNode(list1.val))
                curr = curr.next.next
                list1 = list1.next
                list2 = list2.next
            
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return root.next
    
