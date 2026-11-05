from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        node_queue = deque([root])

        while node_queue:
            cur_res = []
            cur_node_len = len(node_queue)

            for i in range(cur_node_len):
                cur_node = node_queue.popleft()
                cur_res.append(cur_node.val)

                if i == cur_node_len - 1:
                    res.append(cur_res)

                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)

        return res