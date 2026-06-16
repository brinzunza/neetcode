class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.minimum) < 1):
            self.minimum.append(val)
        elif(val < self.minimum[len(self.minimum) - 1]):
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[len(self.minimum) - 1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minimum[len(self.minimum) - 1]
