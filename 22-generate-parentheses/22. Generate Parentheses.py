class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        cur = ""
        maxChar = n * 2

        def isValid():
            nonlocal cur
            if not cur:
                return False
            seen = []
            for c in cur:
                if c == "(":
                    seen.append(c)
                else:
                    if not seen:
                        return False
                    seen.pop()
            return len(seen) == 0
                    

        def dfs():
            nonlocal cur
            if len(cur) == n*2 and isValid():
                res.append(cur)

            if len(cur) > n*2:
                return
            
            old = cur
            cur += "("
            dfs()
            if cur != "":
                cur = old
                cur += ")"
                dfs()

        dfs()

        return res
            

            





        