# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        q = collections.deque()
        q.append(root)
       
        while q:
            level = []
            lent = len(q)
            for i in range(lent):
                num = q.popleft()
                if num:
                    level.append(num.val)
                    q.append(num.left)
                    q.append(num.right)
                 
            if level:
                ans.append(level)
        
        return ans

        
        
       