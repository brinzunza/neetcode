"""
input: node head, int n : length of linked list from head? value of n? 0?
output: node, beginning of the linked list

two pass approach, to get size of linked list, then pass again through array and remove size of list - n.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        length = head
        count = 0
        while length:
            length = length.next
            count += 1

        delete = count - n
        if delete == 0:
            return head.next

        second = head
        index = 0
        while index < delete - 1:
            second = second.next
            index += 1

        if second and second.next:
            second.next = second.next.next

        return head
        
"""
time complexity: O(n)
space complexity: O(1)
"""