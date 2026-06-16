"""
input: node list1, node list2 : value of node? length of linked list?
output: node; head of merged, sorted linked list


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        main = head

        while(list1 and list2):
            if list1.val > list2.val:
                main.next = list2
                list2 = list2.next
            else:
                main.next = list1
                list1 = list1.next
            
            main = main.next
        
        if list1:
            main.next = list1
        elif list2:
            main.next = list2
        
        return head.next

"""
Time complexity: O(n + m)
space complexity: O(1)
"""