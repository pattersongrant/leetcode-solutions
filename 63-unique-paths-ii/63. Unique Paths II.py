class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * COLS for _ in range(ROWS)]

        if obstacleGrid[0][0] == 1:
            return 0
            
        cache[0][0] = 1

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) == (0,0):
                    continue
                if obstacleGrid[r][c] == 1:
                    cache[r][c] = 0
                    continue
                up, left = 0, 0
                if r-1 >= 0:
                    up = cache[r-1][c]
                if c-1 >= 0:
                    left = cache[r][c-1]
                cache[r][c] = up + left

        return cache[ROWS-1][COLS-1]
