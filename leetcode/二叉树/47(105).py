# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not len(preorder):
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])

        left_preorder = preorder[1:1 + root_idx]
        left_inorder = inorder[0:root_idx]

        right_preorder = preorder[root_idx + 1:]
        right_inorder = inorder[root_idx + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root