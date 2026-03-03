class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        [1]

        [1][1]

        [1][2][1]

        [1][3][3][1]

        [1][4][6][4][1]

        the value of a cell = the value of that idx in the row before it + (idx-1) in row before it

        '''

        tri = [[1]]

        for i in range(1, numRows):
            cur = [0] * (i + 1)

            for j in range(len(cur)):
                v1,v2 = 0,0
                if j-1 >= 0:
                    v1 = tri[i-1][j-1]
                if j != i:
                    v2 = tri[i-1][j]
                cur[j] = v1+v2
            tri.append(cur)
        
        return tri
            

