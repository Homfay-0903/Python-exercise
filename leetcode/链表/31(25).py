# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head.next or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre_node1 = dummy

        while True:
            tail = pre_node1

            for i in range(k):
                tail = tail.next

                if not tail:
                    return dummy.next

            pre_node2 = tail.next
            next_dummy = pre_node1.next
            cur_node = pre_node1.next

            for i in range(k):
                next = cur_node.next
                cur_node.next = pre_node2
                pre_node2 = cur_node
                cur_node = next

            pre_node1.next = pre_node2
            pre_node1 = next_dummy

        return dummy.next