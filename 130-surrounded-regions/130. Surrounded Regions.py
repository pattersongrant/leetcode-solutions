class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        noCap = set()

        def dfs(r,c):
            if (r,c) in noCap:
                return
            noCap.add((r,c))
            if r+1 < ROWS and board[r+1][c] == 'O':
                dfs(r+1, c)
            if c + 1 < COLS and board[r][c+1] == 'O':
                dfs(r, c+1)
            if r-1 >= 0 and board[r-1][c] == 'O':
                dfs(r-1, c)
            if c - 1 >= 0 and board[r][c-1] == 'O':
                dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if ((not (r==0 or r == ROWS - 1 or c == 0 or c == COLS -1)) 
                    or (r,c) in noCap):
                    continue
                if board[r][c] == 'O':
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in noCap:
                    board[r][c] = 'X'

        
        