class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ROWS, COLS = m, n

        graph = []

        for i in range(ROWS):
            graph.append(["E"] * COLS)

        for r,c in guards:
            graph[r][c] = "G"

        for [r,c] in walls:
            graph[r][c] = "W"

        def dfs(r, c, vert, prev):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
                or graph[r][c] == "W" or graph[r][c] == "G"):
                return

            graph[r][c] = "O"

            if vert:
                if prev != (r+1, c):
                    dfs(r+1, c, True, (r,c))
                if prev != (r-1, c):
                    dfs(r-1, c, True, (r,c))
            if not vert:
                if prev != (r, c+1):
                    dfs(r, c+1, False, (r,c))
                if prev != (r, c-1):    
                    dfs(r, c-1, False, (r,c))


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
