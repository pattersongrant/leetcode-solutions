class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #bottom up        
        dp = [[float('inf')] * (len(word2)+1) for _ in range(len(word1)+1)]
        ROWS, COLS = len(dp), len(dp[0])

        for r in range(ROWS):
            dp[r][COLS-1] = ROWS - r - 1
        for c in range(COLS):
            dp[ROWS - 1][c] = COLS - c - 1

        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 2, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r+1][c+1], dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]


        #top down         
        # dp = {}
        # def dfs(i, j, cur):
        #     if (i,j,cur) in dp:
        #         return dp[(i,j,cur)]
        #     elif j == len(word2) and not i == len(word1):
        #         dp[(i,j,cur)] = dfs(i+1, j, cur+1)
        #     elif i == len(word1) and not j == len(word2):
        #         dp[(i,j,cur)] = dfs(i, j+1, cur+1)
        #     elif i == len(word1):
        #         dp[(i,j,cur)] = cur
        #     elif word1[i] == word2[j]:
        #         dp[(i,j,cur)] = dfs(i+1, j+1, cur)
        #     else:
        #         dp[(i,j,cur)] = min(dfs(i+1, j+1, cur+1),
        #                    dfs(i+1, j, cur+1),
        #                    dfs(i, j+1, cur+1))
        #     return dp[(i,j,cur)]

        # return dfs(0,0,0)
