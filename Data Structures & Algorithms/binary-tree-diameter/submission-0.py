# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def check_height(node):
            nonlocal res

            if not node:
                return 0
            
            l = check_height(node.left)
            r = check_height(node.right)

            
            res = max(res, l + r)
            
            return max(r,l) + 1
        
        res = 0
        check_height(root)
        return res