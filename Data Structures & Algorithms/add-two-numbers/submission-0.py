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
        str1 = ""
        str2 = ""

        while(l1):
            str1 += str(l1.val)
            l1 = l1.next

        while(l2):
            str2 += str(l2.val)
            l2 = l2.next

        num1 = int(str1[::-1])
        num2 = int(str2[::-1])

        final = str(num1 + num2)

        final = list(final[::-1])

        result = ListNode()
        l3 = result
        for i in final:
            l3.next = ListNode(i)
            l3 = l3.next
        
        return result.next



