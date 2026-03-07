class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        '''
        store just the value of the square you are jumping to.
        Repeat for each of the 4 sides until the (r,c) is the first one you were at
        
        first
        [0][1] -> [1][n]

        [r][c] -> [c][n-r]

        second
        [1][n] -> [n][n-1]
        '''

        n = len(matrix)
        seen = set()
        for r in range(math.ceil(n)):
            for c in range(math.ceil(n)):
                first = [r, c]
                nxt = [c, n-1-r]
                if (nxt[0], nxt[1]) in seen:
                    continue
                needToMove = matrix[r][c]
                for _ in range(4):
                    seen.add((nxt[0], nxt[1]))
                    oldValAtNxt = matrix[nxt[0]][nxt[1]]
                    matrix[nxt[0]][nxt[1]] = needToMove
                    needToMove = oldValAtNxt
                    nxt = [nxt[1], n-1-nxt[0]]
        
                

                    



        