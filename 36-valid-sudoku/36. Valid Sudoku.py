class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) #keys are (r // 3, c//3)
        #each square is a coordinate (0-2, 0-2)

        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == ".":
                    continue
                if (item in rows[r] or
                    item in cols[c] or
                    item in squares[(r//3, c//3)]):
                    return False
                cols[c].add(item)
                rows[r].add(item)
                squares[(r//3, c//3)].add(item)
        return True
