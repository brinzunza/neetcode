class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)

            elif i in (')', '}', ']'):
                if not stack:
                    return False

                top = stack[-1]

                if top == '(' and i != ')':
                    return False
                if top == '{' and i != '}':
                    return False
                if top == '[' and i != ']':
                    return False

                stack.pop()

        return len(stack) == 0