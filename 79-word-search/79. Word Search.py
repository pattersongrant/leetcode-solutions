class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, idx, seenInCheck):
            if (r,c) in seenInCheck:
                return False
            seenInCheck.add((r,c))
            if board[r][c] == word[idx]:
                if idx == len(word) - 1:
                    return True
                else:
                    if r + 1 < ROWS and dfs(r+1, c, idx+1, seenInCheck):
                        return True
                    if c + 1 < COLS and dfs(r, c+1, idx+1, seenInCheck):
                        return True
                    if r - 1 >= 0 and dfs(r-1, c, idx+1, seenInCheck):
                        return True                  
                    if c - 1 >= 0 and dfs(r, c-1, idx+1, seenInCheck):
                        return True
            seenInCheck.remove((r,c))
            return False
    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False


