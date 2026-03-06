class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        I am going to do a top-down DP solution starting from the finish line

        the recurrence relation for the number of paths at any given point is the number of paths to get to the square above + the number of paths to get to the square to the left

        So I will start from the finish and the by using a top down recursion function will work from the base case all the way to the start.

        I will also use a memo the size of m * n to ensure that I cache any already calculated squares
        '''
        dp = [[-1] * n for i in range(m)]
        dp[0][0] = 1
        # dp[1][0] = 1
        # dp[0][1] = 1
        def dfs(r, c):
            if r < 0 or c < 0:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            dp[r][c] = dfs(r-1,c) + dfs(r,c-1)
            return dp[r][c]

        return dfs(m-1, n-1)

            




            
            

        