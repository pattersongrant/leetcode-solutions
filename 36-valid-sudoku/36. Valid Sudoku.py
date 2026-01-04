class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        #arrays of sets
        rows = [set() for r in range(ROWS)] #i.e rows[0] = set() of all in first row
        cols = [set() for c in range(COLS)]
        threes = [set() for i in range(9)]
        


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

                idx = 0

                if r < 3:
                    if c < 3:
                        idx = 0
                    elif c < 6:
                        idx = 3
                    else:
                        idx = 6
                elif r < 6:
                    if c < 3:
                        idx = 1
                    elif c < 6:
                        idx = 4
                    else:
                        idx = 7
                else:
                    if c < 3:
                        idx = 2
                    elif c < 6:
                        idx = 5
                    else:
                        idx = 8

                if board[r][c] in threes[idx]:
                    return False
                threes[idx].add(board[r][c])

        return True

        
