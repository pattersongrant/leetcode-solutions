class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # stack 
        res = []

        #recursive solution to go through all different routes
        def backtrack(openN, closedN):
            if openN == closedN == n: #if a complete and valid parentheses
                res.append("".join(stack)) #turn the stack into a single string
                return #go back to finish the previous function call
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN) #goes through again with 1 more open
                stack.pop() #pop the last added bracket
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1) #goes through again with 1 more close
                stack.pop()
        backtrack(0,0) # run the function with default values
        return res
        