class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            elif s[i] == "{":
                stack.append("{")
            elif s[i] == "[":
                stack.append("[")
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out == "{" and s[i] == "}":
                    continue
                elif out == "(" and s[i] == ")":
                    continue
                elif out == "[" and s[i] == "]":
                    continue
                else:
                    return False
        return len(stack) == 0
                    