class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #rr:
        #topdown
        # #ways to get to up + 1 plus # ways to get from left + 1
        #base case: 0 is 0
        ROWS, COLS = m, n
        
        memo = []

        for i in range(m):
            memo.append([0 for i in range(n)])
        memo[0][0] = 1
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
                #add left and up
                res = 0
                if r - 1 >= 0:
                    res += (memo[r-1][c])
                if c - 1 >= 0:
                    res += (memo[r][c-1])
                
                memo[r][c] = res

        

        return memo[ROWS-1][COLS-1]

