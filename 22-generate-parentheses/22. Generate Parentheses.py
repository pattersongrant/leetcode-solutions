class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        maxChar = n * 2

        def dfs(cur, openp, closedp):
            if openp == closedp == n:
                res.append(cur)
                return

            if openp < n:    
                dfs(cur + "(", openp + 1, closedp)

            if closedp < openp:
                dfs(cur + ")", openp, closedp + 1)

        dfs("", 0, 0)

        return res
            

            





        