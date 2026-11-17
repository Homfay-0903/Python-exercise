# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        def dfs(node: Optional[TreeNode], curSum: int) -> int:
            if not node:
                return 0

            curSum += node.val

            count = prefix_map[curSum - targetSum]
            prefix_map[curSum] += 1

            count += dfs(node.left, curSum)
            count += dfs(node.right, curSum)

            prefix_map[curSum] -= 1

            return count

        return dfs(root, 0)