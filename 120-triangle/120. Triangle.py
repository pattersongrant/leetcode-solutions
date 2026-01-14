class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        cache = {}
        cache[(0,0)] = triangle[0][0]


        def minTotalAtPoint(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            upAndLeft = float('inf')
            upAndRight = float('inf')
            if r-1 >= 0:
                if c-1 >= 0:
                    upAndLeft = minTotalAtPoint(r-1,c-1)
                if c <= len(triangle[r-1]) - 1:
                    upAndRight = minTotalAtPoint(r-1, c)

    
            cache[(r,c)] = min(upAndLeft, upAndRight) + triangle[r][c]
            return cache[(r,c)]

        res = float('inf')
        for c in range(len(triangle[-1])):
            res = min(res, minTotalAtPoint(len(triangle) - 1, c))
        
        return res

