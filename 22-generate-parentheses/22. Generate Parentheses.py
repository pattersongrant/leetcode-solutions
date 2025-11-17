class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        cur = ""
        maxChar = n * 2

        def dfs(openp, closedp):
            nonlocal cur
            if len(cur) == n*2 and openp == closedp:
                res.append(cur)

            if len(cur) > n*2:
                return
            old = cur

            if openp < n*2:    
                cur += "("
                dfs(openp + 1, closedp)

            if closedp < openp:
                cur = old
                cur += ")"
                dfs(openp, closedp + 1)

        dfs(0, 0)

        return res
            

            





        