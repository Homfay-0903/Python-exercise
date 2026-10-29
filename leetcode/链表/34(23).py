# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        def mergeList(list1: ListNode, list2: ListNode):
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

        def divide(left, right):
            if left == right:
                return lists[left]
            elif left > right:
                return
            else:
                mid = (left + right) // 2
                return mergeList(divide(left, mid), divide(mid + 1, right))

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        return divide(0, len(lists) - 1)