"""
input: string s
output: boolean, true if brackets are valid, false otherwise

len s? 

use a stack to keep track of which have been opened and which can be closed
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                return False

        return len(stack) == 0

"""
Time complexity: O(n)
Space complexity: O()
"""