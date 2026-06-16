"""
input: node l1; head of first linked list, node l2; head of second linked list : length of linked list? empty?
output: node; head of new linked list with reverse order of sum of two input linked lists

go through both input arrays, saving their values in variable and reversing it. casting it to int and adding.
then reverse it again and place into new linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total_sum = val1 + val2 + carry
            digit = total_sum % 10
            carry = total_sum // 10

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        return dummy_head.next

"""
time complexity: O(n+m)
space complexity: O(1)
"""