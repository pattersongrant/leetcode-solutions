class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(0, int(n/2)+1):
            if 3**i > n:
                break
            if 3**i == n:
                return True
        
        return False
        