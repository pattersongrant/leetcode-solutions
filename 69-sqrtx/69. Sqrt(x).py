class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 0, x

        while l <= r:
            m = (l+r) // 2
            sq = m*m
            if sq == x:
                return m
            elif sq > x and (m-1) * (m-1) < x:
                return m-1
            elif sq > x:
                r = m - 1
            elif sq < x:
                l = m + 1
            
        