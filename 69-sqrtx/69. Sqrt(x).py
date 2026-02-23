class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        prev = 0
        for i in range(x+1):
            squared = i*i
            if squared == x:

                return i
            
            if squared > x and prev*prev < x:
                return prev
            
            prev = i
        