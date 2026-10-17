# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        list1, list2 = head, slow.next
        reverse_list2 = self.reverseList(list2)

        while list1 and reverse_list2:
            if list1.val != reverse_list2.val:
                return False
            list1 = list1.next
            reverse_list2 = reverse_list2.next

        return True

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre_node, cur_node = None, head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node

        return pre_node