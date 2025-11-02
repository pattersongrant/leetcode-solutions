class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ROWS, COLS = m, n

        graph = []

        visitedByGuard = set()

        for i in range(ROWS):
            graph.append(["E"] * COLS)

        for r,c in guards:
            graph[r][c] = "G"

        for [r,c] in walls:
            graph[r][c] = "W"

        def dfs(r, c, vert, curGuard):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
                or graph[r][c] == "W" or graph[r][c] == "G" or 
                (r,c,curGuard) in visitedByGuard):
                return

            graph[r][c] = "O"
            visitedByGuard.add((r,c,curGuard))
            if vert:
                dfs(r+1, c, True, curGuard)
                dfs(r-1, c, True, curGuard)
            if not vert:
                dfs(r, c+1, False, curGuard)
                dfs(r, c-1, False, curGuard)


        for r in range(ROWS):
            for c in range(COLS):
                if graph[r][c] == "G":
                    dfs(r+1, c, True, (r,c))
                    dfs(r-1, c, True, (r,c))
                    dfs(r, c+1, False, (r,c))
                    dfs(r, c-1, False, (r,c))

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if graph[r][c] == "E":
                    res += 1
                    
        return res
