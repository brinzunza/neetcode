"""
input: actions(push, pop, top, getMin) (type? runtime of each?)
output: function stack class with following functions
- push(pushes an integer into top of stack)
- pop(returns top item of stack and removes)
- top(returns top item of stack)
- getMin(returns smallest value in stack)
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallest) > 0 and self.smallest[-1] < val:
            self.smallest.append(self.smallest[-1])
        else:
            self.smallest.append(val)

    def pop(self) -> None:
        self.smallest.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]

"""
test cases:
["MinStack", "push" 1, "push" 2, "push" 0, "getMin", "pop", "top", "getMin"]

"""