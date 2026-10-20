# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        has_cycls = False
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycls = True
                break

        if not has_cycls:
            return None

        pointer = head

        while pointer != slow:
            pointer = pointer.next
            slow = slow.next

        return pointer