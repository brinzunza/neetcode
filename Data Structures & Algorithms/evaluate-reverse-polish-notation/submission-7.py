"""
input: str array tokens 
output: int, result of the reverse polish notation equation

size of str array? 0?
multiple digit ints? 
division by 0?

iterate through array, keep a stack of integers, when operator appears pop top two elements in stack and place result at top of stack. Repeat until stack is 1
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                second = nums.pop()
                first = nums.pop()
                if token == "+":
                    nums.append(first + second)
                elif token == "-":
                    nums.append(first - second)
                elif token == "*":
                    nums.append(first * second)
                elif token == "/":
                    nums.append(int(first / second))
            else:
                nums.append(int(token))
        return nums.pop()

"""
Time complexity: O(n)
Space complexity: O(n)
"""