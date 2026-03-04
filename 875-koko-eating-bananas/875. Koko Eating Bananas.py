class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            
            m = (l+r) // 2
            hoursUsed = 0
            for n in piles:
                # old = hoursUsed
                if m >= n:
                    hoursUsed += 1
                else:
                    hoursUsed += math.ceil(n/m)
                # print(m, n, hoursUsed - old)
            
            if hoursUsed <= h:
                r = m - 1
                res = min(m, res)
            elif hoursUsed > h:
                l = m + 1


        
        return res