class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            #middle row
            row = (top + bot) // 2
            #rightmost value [-1]
            if target > matrix[row][-1]: 
                top = row + 1
            #smallest value [0]
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        #if all the numbers in matrix were checked
        if not (top <= bot):
            return False
        #gets current row
        row = (top + bot) // 2
        #run BS on correct row
        l, r = 0, COLS - 1
        while l<=r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False