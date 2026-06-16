"""
input: node head
output: node, head of newly reversed linked list

length of linked list? empty?
can there be duplicate values?

keep a tracker of last node and point next node to last node
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        if(head.next == None):
            return head
        future = head.next
        previous = None
        while(head.next != None):
            future = head.next
            head.next = previous
            previous = head
            head = future
        head.next = previous
        return head
            
"""
time complexity: O(n)
space complexity: O(1)
"""