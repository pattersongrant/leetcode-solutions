class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for r in range(1,ROWS+1):
            for c in range(1,COLS+1):
                above = self.sumMat[r-1][c]
                left = self.sumMat[r][c-1]
                double = self.sumMat[r-1][c-1]
                self.sumMat[r][c] = above + left + matrix[r-1][c-1] - double
        print(self.sumMat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        above = self.sumMat[row1-1][col2]
        left = self.sumMat[row2][col1-1]
        double = self.sumMat[row1-1][col1-1]
        return self.sumMat[row2][col2] - above - left + double

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)