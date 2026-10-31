# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def LDR(node: TreeNode):
            if not node:
                return

            LDR(node.left)
            res.append(node.val)
            LDR(node.right)

        LDR(root)

        return res