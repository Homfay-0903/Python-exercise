"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        cur_node = head
        while cur_node:
            node_map[cur_node] = Node(cur_node.val)
            cur_node = cur_node.next

        cur_node = head
        while cur_node:
            new_node = node_map[cur_node]
            new_node.next = node_map[cur_node.next] if cur_node.next else None
            new_node.random = node_map[cur_node.random] if cur_node.random else None
            cur_node = cur_node.next

        return node_map.get(head, None)