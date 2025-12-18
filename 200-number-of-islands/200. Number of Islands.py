class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        islands = 0

        def addQueue(r, c):
            if (r >= 0 and r != ROWS and c >= 0 and 
                c != COLS and grid[r][c] == "1"):
                q.append((r, c))
                grid[r][c] = "0"

        def bfs(r, c):
            q.append((r, c))

            while q:
                r, c = q.popleft()
                addQueue(r+1, c)
                addQueue(r-1, c)
                addQueue(r, c+1)
                addQueue(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands



        