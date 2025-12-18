class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.res = 0
        def dfs(r, c):
            
            grid[r][c] = "0"
            if r + 1 < ROWS and grid[r+1][c] == "1":
                dfs(r+1, c)
            if r - 1 >= 0 and grid[r-1][c] == "1":
                dfs(r-1, c)
            if c + 1 < COLS and grid[r][c+1] == "1":
                dfs(r, c+1)
            if c - 1 >= 0 and grid[r][c-1] == "1":
                dfs(r, c-1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.res += 1
                    dfs(r,c)
        return self.res