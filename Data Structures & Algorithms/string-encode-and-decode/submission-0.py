"""
inputs: strs= array of strings, s= string
output: string of encoded strings, array of strings from encoded string
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += i + "."
        return encoded
    def decode(self, s: str) -> List[str]:
        return s.split('.')[0:-1]
