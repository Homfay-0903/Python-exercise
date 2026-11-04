# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_meter = 0

        def calculate_meter(node: TreeNode):
            nonlocal max_meter

            if not node:
                return 0

            left_dep = calculate_meter(node.left)
            right_dep = calculate_meter(node.right)
            max_meter = max(max_meter, left_dep + right_dep)

            return 1 + max(left_dep, right_dep)

        calculate_meter(root)

        return max_meter