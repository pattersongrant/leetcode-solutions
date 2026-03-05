class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        time = -1

        q = deque()
        def addQueue(r, c):

            if (not (0 <= r < ROWS and 0 <= c < COLS)) or grid[r][c] == 2 or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r,c))
        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    found = True
                if grid[r][c] == 2:
                    q.append((r,c))
        if not found:
            return 0
        
        while q:
            time += 1
            print(q)
            for i in range(len(q)):
                r, c = q.popleft()
                addQueue(r+1,c)
                addQueue(r-1,c)
                addQueue(r,c+1)
                addQueue(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time
                

        

