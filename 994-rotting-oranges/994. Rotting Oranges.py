class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.seen = set()
        time = -1

        closestDistanceToRotten = [[100] * COLS for r in range(ROWS)]

        def dfs(r, c, distance):
            print(r,c)
            if (r,c) in self.seen:
                return
            self.seen.add((r,c))
            if grid[r][c] == 1:
                closestDistanceToRotten[r][c] = min(distance, closestDistanceToRotten[r][c])

            if r+1 < ROWS and grid[r+1][c] == 1:
                dfs(r+1, c, distance + 1)
            if r-1 >= 0 and grid[r-1][c] == 1:
                dfs(r-1, c, distance + 1)
            if c+1 < COLS and grid[r][c+1] == 1:
                dfs(r, c+1, distance + 1)
            if c-1 >= 0 and grid[r][c-1] == 1:
                dfs(r, c-1, distance + 1)
            
            self.seen.remove((r,c))


            
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    self.seen = set()
                    dfs(r, c, 0)
        
        res = 0
        print(closestDistanceToRotten)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if closestDistanceToRotten[r][c] == 100:
                        return -1
                    res = max(res, closestDistanceToRotten[r][c])
        

        return res
                

        

