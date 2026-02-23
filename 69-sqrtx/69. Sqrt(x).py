class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        m = 0
        while l <= r:
            m = (l+r) // 2
            squared = m*m

            if squared > x:
                r = m - 1
            elif squared < x:
                l = m + 1
            elif squared == x:
                return m
        
        return m if (m*m < x) else (m - 1)
            