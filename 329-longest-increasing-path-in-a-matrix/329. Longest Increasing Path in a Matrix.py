class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = [[-1] * COLS for _ in range(ROWS)]
        # dp[r][c] : distance to lowest value starting from this cell
        res = 1
        def search(r,c,traveled, came_from): #returns furthest distance to bottom
            #find the bottom and update res, while updating dp going back up
            nonlocal res
            res = max(res, traveled)
            if dp[r][c] != -1:
                res = max(res, traveled + dp[r][c])
                return dp[r][c]

            up, down, left, right = -1, -1, -1, -1
            if (came_from != (r-1, c) and r-1 >= 0 and 
                matrix[r-1][c] < matrix[r][c]):
                down = search(r-1, c, traveled + 1, (r,c))

            if (came_from != (r+1, c) and r+1 < ROWS and 
                matrix[r+1][c] < matrix[r][c]):
                up = search(r+1, c, traveled + 1, (r,c))

            if (came_from != (r, c-1) and c-1 >= 0 and 
                matrix[r][c-1] < matrix[r][c]):
                left = search(r, c-1, traveled + 1, (r,c))

            if (came_from != (r, c+1) and c+1 < COLS and 
                matrix[r][c+1] < matrix[r][c]):
                right = search(r, c+1, traveled + 1, (r,c))
            
            maxSearch = max(up,down,left,right)
            dp[r][c] = maxSearch + 1

            return dp[r][c]
        for r in range(ROWS):
            for c in range(COLS):
                #search only starting from local maximums (>=)
                up = matrix[r+1][c] if r+1 < ROWS else 0
                down = matrix[r-1][c] if r-1 >= 0 else 0
                right = matrix[r][c+1] if c+1 < COLS else 0
                left = matrix[r][c-1] if c-1 >= 0 else 0
                if matrix[r][c] >= max(up,down,left,right):
                    search(r,c,1, (r,c))
        
        return res
