class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for n in s:
            if n == '(' or n =='{' or n == '[':
                stack.append(n)
            elif n == ')':
                # get last element with n[-1]
                if stack == []:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif n == '}':
                if stack == []:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif n == ']':
                if stack == []:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                    
                else:
                    return False
        if stack != []:
            return False
        else:
            return True

                

            