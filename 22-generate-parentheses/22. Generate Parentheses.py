class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def generate(cur, openCount, closedCount):
            if openCount + closedCount == 2*n:
                self.res.append(cur)
                return
            
            if openCount > closedCount:
                generate(cur + ")", openCount, closedCount + 1)
            if closedCount <= openCount and openCount != n:
                generate(cur + "(", openCount + 1, closedCount)
        generate("", 0, 0)
        return self.res