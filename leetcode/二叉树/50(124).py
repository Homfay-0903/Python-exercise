# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        res = float('-inf')

        def max_sum(node: TreeNode) -> int:
            nonlocal res

            if not node:
                return 0

            max_sum_left = max(max_sum(node.left), 0)
            max_sum_right = max(max_sum(node.right), 0)

            res = max(res, node.val + max_sum_left + max_sum_right)

            return node.val + max(max_sum_left, max_sum_right)

        max_sum(root)

        return res