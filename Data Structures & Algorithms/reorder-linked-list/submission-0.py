"""
input: node head; head of singly linked list : value? length of linked list?
output: nothing : linked list should be reordered

two pointer: slow and fast pointers to get first half and second half
then reverse second half linked list, then merge 
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        previous = None
        current = slow.next
        slow.next = None
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

        while previous:
            reconnection = first.next
            first.next = previous
            previous = previous.next
            first.next.next = reconnection
            first = reconnection

"""
time complexity: O(n)
space complexity: O(1)
"""