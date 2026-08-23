# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(node, path_max):
            nonlocal good_nodes
            if not node:
                return None

            if node.val >= path_max:
                good_nodes += 1

            path_max = max(node.val, path_max)

            dfs(node.left, path_max)
            dfs(node.right, path_max)

        dfs(root, root.val)
        return good_nodes

