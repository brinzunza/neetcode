"""
input: array string strs
output: array string strs

how long can strs be? 0?
what characters can it contain?

combine strings and add number to start to know where to split. Add a delimiter incase number is multi digit
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded

"""
encode: O(n), O(n)
decode: O(n), O(n)
"""