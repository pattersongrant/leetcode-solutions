class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        
        memo = []

        for i in range(m):
            memo.append([-1 for i in range(n)])
        memo[0][0] = 1

        def numWays(r, c):
            if memo[r][c] != -1:
                return memo[r][c]

            res = 0
            if r - 1 >= 0:
                res += (numWays(r-1, c))
            if c - 1 >= 0:
                res += (numWays(r, c-1))
            
            memo[r][c] = res

            return res
        

        return numWays(ROWS-1, COLS-1)

