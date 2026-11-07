class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low_k = 0
        high_k = max(piles)
        passed = -1
        while low_k <= high_k:
            k_m = (low_k + high_k) // 2
            if k_m == 0:
                break
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k_m)
            if hrs < h:
                passed = k_m
                high_k = k_m - 1
            elif hrs > h:
                low_k = k_m + 1
            else:
                passed = k_m
                high_k = k_m - 1
        return passed


                
                
                


