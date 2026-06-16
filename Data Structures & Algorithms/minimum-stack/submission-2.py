"""
design MinStack class
- push(int val): puts element at top of stack
- pop(): removes top element
- top(): gets top element
- getMin(): retrieves min element
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val, self.minimum[-1]))

    def pop(self) -> None:
        self.minimum.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

"""
Time complexity: O(1)
Space Complexity: O(n)
"""
