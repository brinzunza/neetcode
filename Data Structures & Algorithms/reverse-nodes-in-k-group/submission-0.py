# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth_node = group_prev
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            next_group_head = kth_node.next

            prev, curr = next_group_head, group_prev.next
            while curr != next_group_head:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            group_tail = group_prev.next
            group_prev.next = kth_node
            group_prev = group_tail
