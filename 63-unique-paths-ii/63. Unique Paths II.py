class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}

        if obstacleGrid[0][0] == 1:
            return 0
            
        cache[(0,0)] = 1

        def dfs(r, c):

            if (r,c) in cache:
                return cache[(r,c)]
            if obstacleGrid[r][c] == 1:
                return 0

            up, left = 0, 0
            if r-1 >= 0:
                up = dfs(r-1,c)
            if c-1 >= 0:
                left = dfs(r,c-1)

            cache[(r,c)] = up + left
            return cache[(r,c)]
        
        return dfs(ROWS-1, COLS-1)
