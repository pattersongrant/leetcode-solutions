class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                r1, c1 = q.popleft()
                
                for x, y in directions:

                    if ((r1+x >= 0 and r1+x < rows) and 
                        (c1+y >= 0 and c1+y < cols) and 
                        grid[r1+x][c1+y] == "1"):
                        q.append((r1+x, c1+y))
                        grid[r1+x][c1+y] = "0"
                        
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands

