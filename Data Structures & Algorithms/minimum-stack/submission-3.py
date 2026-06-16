class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallest) == 0:
            self.smallest.append(val)
        elif self.smallest[-1] > val:
            self.smallest.append(val)
        else:
            self.smallest.append(self.smallest[-1])

    def pop(self) -> None:
        self.smallest.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
