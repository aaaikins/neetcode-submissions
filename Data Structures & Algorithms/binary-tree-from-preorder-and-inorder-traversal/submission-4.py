# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            mid = inorderMap[root_val]

            pre_idx += 1

            root = TreeNode(root_val)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
            

        return build(0, len(inorder) - 1)

        # if not preorder or not inorder:
        #     return

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])

        # return root
