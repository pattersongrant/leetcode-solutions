class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X' and (r-1 < 0 or board[r-1][c] != 'X') and (c-1 < 0 or board[r][c-1] != 'X'):
                    res += 1
        return res



