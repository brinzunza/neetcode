class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        state = []

        def backtracking(state, count):
            if count == 0 and len(state) == (n*2):
                result.append(state)
            if len(state) < (n*2):
                state += "("
                backtracking(state, count + 1)
                state = state[:-1]
                if count > 0:
                    state += ")"
                    backtracking(state, count - 1)
                    state = state[:-1]
        
        backtracking("", 0)
        return result