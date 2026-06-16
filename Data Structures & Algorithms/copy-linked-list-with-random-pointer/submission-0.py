"""
input: node head; head of linked list : length of linked list?
output: head node of copied linked list


"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        total = {} 
        
        start = head
        while start:
            created = Node(start.val)
            total[start] = created
            start = start.next

        start = head
        while start:
            newList = total[start]
            newList.next = total.get(start.next)
            newList.random = total.get(start.random)
            start = start.next

        return total[head]

"""
time complexity: O(n)
space complexity: O(n)
"""