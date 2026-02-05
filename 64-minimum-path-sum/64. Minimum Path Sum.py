class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # recurrence relation: Pick the smaller of the up cell and left cell. And then add the value of the current cell to get the value to get to that cell.
        ROWS, COLS = len(grid), len(grid[0])
        dp = {}



        def getValAtPoint(r, c):
            res = grid[r][c]
            if (r,c) in dp:
                return dp[(r,c)]
            if r == 0 and c == 0:
                dp[(r,c)] = res    
            elif r-1 >= 0 and c-1 < 0:
                dp[(r,c)] = res + getValAtPoint(r-1,c)
            elif c-1 >= 0 and r-1 < 0:
                dp[(r,c)] = res + getValAtPoint(r,c-1)
            else:
                dp[(r,c)] = min(res + getValAtPoint(r-1,c), res + getValAtPoint(r,c-1))
            return dp[(r,c)]

            
        return getValAtPoint(ROWS-1, COLS-1)



