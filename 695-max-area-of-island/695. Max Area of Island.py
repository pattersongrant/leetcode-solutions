class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(1,0), (-1,0), (0,-1), (0, 1)]

        def bfs(r, c): #returns area of island
            q = collections.deque()
            a = 0

            q.append((r, c))
            grid[r][c] = 0
            a += 1
            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    if ((r + dr) in range(len(grid)) and 
                        (c + dc) in range(len(grid[0])) and
                        grid[r+dr][c+dc] == 1):
                        a += 1
                        q.append(((r+dr), (c+dc)))
                        grid[r+dr][c+dc] = 0
            return a      

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))

        return res



