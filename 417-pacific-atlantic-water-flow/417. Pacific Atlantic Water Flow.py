class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        res = []

        def dfs(r, c, visit, prev):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or (r,c) in visit or prev > heights[r][c]):
                return
            visit.add((r,c))
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS): #dfs each in first and last row
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS): #dfs each in first and last col
            dfs(r, 0, pac, heights[r][0]) 
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        return res
        
        

            
            
            
