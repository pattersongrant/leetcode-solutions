class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minute = 0
        self.infected = 0
        q = deque()
        visited = set()
        self.startFresh = 0

        def addQueue(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r,c) in visited or grid[r][c] == 0):
                return
            visited.add((r, c))
            self.infected += 1
            grid[r][c] = 2
            q.append((r,c)) 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    self.startFresh += 1

        if self.startFresh == 0:
            return 0

        if len(q) == 0:
            return -1

        while q:
            oldInfect = self.infected
            for i in range(len(q)):
                r, c = q.popleft()
                addQueue(r+1, c)
                addQueue(r-1, c)
                addQueue(r, c+1)
                addQueue(r, c-1)
            minute += 1
            if self.infected == self.startFresh:
                return minute
            if oldInfect == self.infected:
                    return -1
        if self.infected != self.startFresh:
                return -1
        return minute
    
            


