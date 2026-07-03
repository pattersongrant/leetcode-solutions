class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        firstColZero = False
        for n in matrix[0]:
            if n ==0:
                firstRowZero = True
        for r in matrix:
            if r[0] == 0:
                firstColZero = True

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        print(matrix)
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                
                for c in range(1, len(matrix[r])):
                    matrix[r][c] = 0
        print(matrix)
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(1, len(matrix)):
                    matrix[r][c] = 0
        print(matrix)

        if firstColZero:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        if firstRowZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
                
                    

                    
                    

        