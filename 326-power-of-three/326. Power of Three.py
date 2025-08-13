class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0 or n == 0:
            return False



        while True:
            if n != int(n):
                return False
            if n == 1:
                return True

            n = n / 3.0
            

            
        