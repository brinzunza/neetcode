"""
Input: string s
output: boolean, true if string is palindrome, else false

how long can the string be? len 0? characters?

two pointers one at start and one at end, if they meet while maintaining the same chars, then true, else false.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(cleaned)
        start = 0
        end = len(cleaned) - 1
        while(start < end):
            if(cleaned[start] != cleaned[end]):
                return False
            start += 1
            end -= 1
        return True

"""
Time complexity: O(n)
Space complexity: O(1)
"""