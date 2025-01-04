class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        popped = 0
        while i < len(tokens):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(tokens[i])
            else:
                val = 0
                if tokens[i] == "+":
                    val = int(stack[i-popped-2]) + int(stack[i-popped-1])
                elif tokens[i] == "-":
                    val = int(stack[i-popped-2]) - int(stack[i-popped-1])
                elif tokens[i] == "*":
                    val = int(stack[i-popped-2]) * int(stack[i-popped-1])
                elif tokens[i] == "/":
                    val = int(int(stack[i-popped-2]) / int(stack[i-popped-1]))
                stack.pop()
                stack.pop()
                stack.append(val)
                popped += 2
            i+=1
        return int(stack[0])
