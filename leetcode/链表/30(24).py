# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        pre_node = dummy

        while pre_node.next and pre_node.next.next:
            node1, node2 = pre_node.next, pre_node.next.next

            node1.next = node2.next
            node2.next = node1
            pre_node.next = node2
            pre_node = node1

        return dummy.next