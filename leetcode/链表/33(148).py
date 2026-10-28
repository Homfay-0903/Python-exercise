# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeList(list1: ListNode, list2: ListNode) -> ListNode:
            dummy = ListNode(0)
            cur_node = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    cur_node.next = list1
                    list1 = list1.next
                else:
                    cur_node.next = list2
                    list2 = list2.next
                cur_node = cur_node.next

            cur_node.next = list1 if list1 else list2

            return dummy.next

        if not head or not head.next:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left, right = head, slow.next
        slow.next = None

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return mergeList(left_sorted,  right_sorted)