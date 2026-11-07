# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(lowwer, node, upper):
            if not node:
                return True
            if node.val <= lowwer or node.val >= upper:
                return False
            if not dfs(lowwer, node.left, node.val):
                return False
            if not dfs(node.val, node.right, upper):
                return False
            return True
        return dfs(-float('inf'), root, float('inf'))