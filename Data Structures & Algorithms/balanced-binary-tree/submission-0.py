# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            nonlocal res

            if not node:
                return 0
            
            l = check_height(node.left)
            r = check_height(node.right)

            if abs(l-r) > 1:
                res = False
            
            return max(r, l) + 1
        
        res = True
        check_height(root)
        return res
            
        