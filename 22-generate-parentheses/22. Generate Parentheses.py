class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        maxChar = n * 2

        def dfs(cur, openp, closedp):
            if len(cur) == maxChar and openp == closedp:
                res.append(cur)
                return

            if len(cur) > n * 2:
                return

            old = cur

            if openp < maxChar:    
                dfs(cur + "(", openp + 1, closedp)

            if closedp < openp:
                dfs(cur + ")", openp, closedp + 1)

        dfs("", 0, 0)

        return res
            

            





        