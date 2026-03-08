class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            board[r][c] = '.'
            if r+1 < ROWS and board[r+1][c] == 'X':
                dfs(r+1, c)
            if c+1 < COLS and board[r][c+1] == 'X':
                dfs(r, c+1)
            if r-1 >= 0 and board[r-1][c] == 'X':
                dfs(r-1, c)
            if c-1 >= 0 and board[r][c-1] == 'X':
                dfs(r, c-1)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X':
                    res += 1
                    dfs(r,c)
        return res



