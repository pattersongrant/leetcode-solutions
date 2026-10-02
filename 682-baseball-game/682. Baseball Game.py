class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == "C":
                res -= stack[-1]
                stack.pop()
            elif op == "D":
                res += stack[-1]*2
                stack.append(stack[-1]*2)
            elif op == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1]+stack[-2])
            else:
                res += int(op)
                stack.append(int(op))
        return res

        