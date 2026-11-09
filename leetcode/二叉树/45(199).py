# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        queue = deque([root])

        while len(queue):
            cur_queue_len = len(queue)

            for i in range(cur_queue_len):
                cur_node = queue.popleft()

                if i == cur_queue_len - 1:
                    res.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return res