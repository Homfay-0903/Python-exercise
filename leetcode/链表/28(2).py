# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        cur_node = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cur_sum = val1 + val2 + carry

            digint = cur_sum % 10
            carry = cur_sum // 10

            cur_node.next = ListNode(digint)
            cur_node = cur_node.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
