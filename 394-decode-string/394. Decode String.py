class Solution:
    def decodeString(self, s: str) -> str:

        repStack = []
        stringStack = []

        curRep = ""
        stringStack.append("")

        for i in range(len(s)):
            
            if s[i] in "0123456789":
                curRep += s[i]
            
            elif s[i] == "[":
                stringStack.append("")
                repStack.append(int(curRep))
                curRep = ""

            elif s[i] == "]":

                stringStack[-2] += stringStack[-1] * repStack[-1]
                stringStack.pop()
                repStack.pop()
            
            else:
                stringStack[-1] += s[i]

        
        return stringStack[-1]





            

        