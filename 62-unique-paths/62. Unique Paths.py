class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom up DP
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r-1 >= 0:
                    dp[r][c] += dp[r-1][c]
                if c-1 >= 0:
                    dp[r][c] += dp[r][c-1]
        
        return dp[m-1][n-1]
            




            
            

        