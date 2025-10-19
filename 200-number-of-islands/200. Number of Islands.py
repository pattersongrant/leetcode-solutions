class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                r1, c1 = q.popleft()
                
                for x, y in directions:

                    if (r1+x in range(rows) and 
                        c1+y in range(cols) and 
                        grid[r1+x][c1+y] == "1" and
                        (r1+x, c1+y) not in visited):
                        q.append((r1+x, c1+y))
                        visited.add((r1+x, c1+y))
                        grid[r1+x][c1+y] = "0"
                        
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands

