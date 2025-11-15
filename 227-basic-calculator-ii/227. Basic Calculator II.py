class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        cur = 0
        prevOp = "+"

        for i, c in enumerate(s):

            if c.isdigit():
                cur = cur * 10 + int(c)

            if c in "+-/*" or i == len(s) - 1:
                if prevOp == "+":
                    stack.append(cur)
                if prevOp == "-":
                    stack.append(-cur)
                if prevOp == "*":
                    stack[-1] *= cur
                if prevOp == "/":
                    stack[-1] = int(stack[-1] / cur)
                prevOp = c
                cur = 0

        return sum(stack)