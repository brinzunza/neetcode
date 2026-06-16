'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
- input int n 
- return string array in any order 
- find all permutations of paranthesis where they have their adequate open and closed pair

clarifications
- size of n
- can n be negative

logic: 
- brute force: create all possible permutations then filter the well-formed
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def valid(s):
            open = 0
            for i in s:
                open += 1 if i == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s):
            if n * 2 == len(s):
                if valid(s):
                    result.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return result