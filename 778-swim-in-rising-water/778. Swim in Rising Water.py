class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # start at 0,0 - how long to get to bottom right ?
        # you can swim horizontally or vertically, if grid[r][c] <= t
        # use dijkstra's where elevation is the weight
        # in minHeap: (maxToGetHere, r, c)
        ROWS, COLS = len(grid), len(grid[0])


        minH = [(grid[0][0], 0, 0)]
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        visit = set()

        while minH:
            maxToGetHere, r, c = heapq.heappop(minH)
            if (r,c) == (ROWS-1, COLS-1):
                return maxToGetHere
        
            for newR, newC in directions:
                newR, newC = r + newR, c + newC
                if newR < 0 or newR == ROWS or newC < 0 or newC == COLS or (newR, newC) in visit:
                    continue
                visit.add((newR, newC))
                heapq.heappush(minH, (max(maxToGetHere, grid[newR][newC]), newR, newC))
        return visit[(r,c)]





