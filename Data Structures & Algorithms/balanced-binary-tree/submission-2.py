# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkHeight(root):
            nonlocal res
            if not root:
                return 0

            l = checkHeight(root.left)
            r = checkHeight(root.right)

            if abs(l - r) > 1:
                res = False

            return 1 + max(l, r)
        res = True
        checkHeight(root)
        return res
        


        