"""
input: node head : value? length of linked list?
output: boolean : true if cycle exists, false otherwise
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None or head.next == None):
            return False
        while(head.next):
            if(head.next.val == 1001):
                return True
            head.val = 1001
            head = head.next
        return False
