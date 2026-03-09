class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        take from up and left and up and right. You get half the excess there
        if not up and left or not up and right, you get 0 from there.
        '''
        dp = [([0] * (r+1)) for r in range(query_row+1)]
        dp[0][0] = poured

        for r in range(len(dp)):
            for c in range(len(dp[r])):
                if r - 1 >= 0 and c in range(len(dp[r-1])) and dp[r-1][c] > 1:
                    dp[r][c] += (dp[r-1][c] - 1) / 2
                if r - 1 >= 0 and c-1 in range(len(dp[r-1])) and dp[r-1][c-1] > 1:
                    dp[r][c] += (dp[r-1][c-1] - 1) / 2
                
        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1
            
            



