"""
input: string s (len? chars?)
output: boolean; represents if string follows correct paranthesis structure

brute force: 
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0
        bufferCount = 0

        for c in s:
            if c == '(':
                openCount += 1
                bufferCount += 1
            elif c == ')':
                openCount -= 1
                bufferCount -= 1
            else:  # '*'
                openCount -= 1
                bufferCount += 1

            if bufferCount < 0:
                return False
            if openCount < 0:
                openCount = 0

        return openCount == 0
