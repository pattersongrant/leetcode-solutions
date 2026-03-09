class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        take from up and left and up and right. You get half the excess there
        if not up and left or not up and right, you get 0 from there.
        '''
        dp = [([-1] * (r+1)) for r in range(query_row+1)]
        dp[0][0] = poured
        seen = set()
        seen.add((0,0))
        def dfs(row, idx):
            amount = 0
            if row < 0 or row >= len(dp) or idx < 0 or idx >= (len(dp[row])):
                return 0
            if dp[row][idx] != -1:
                return dp[row][idx]
            dp[row][idx] = 0
            
            above1 = dfs(row-1, idx)
            above2 = dfs(row-1, idx-1)
            if above1 > 1:
                amount += (above1-1) / 2.0
            if above2 > 1:
                amount += (above2-1) / 2.0 

            dp[row][idx] = amount
            return dp[row][idx]
        res = dfs(query_row, query_glass)
        return res if res < 1 else 1.0 
            
            



