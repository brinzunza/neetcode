class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack:
                    return False
                n = stack.pop()
                if pairs[i] != n:
                    return False

        return len(stack) == 0
