class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        res = -1
        while l <= r:
            m = (l+r) // 2


            s = 0
            trips = 0
            for w in weights:
                s += w
                if s > m:
                    s = w
                    trips += 1
            if s > 0:
                trips += 1

            if trips <= days:
                r = m - 1
                res = m
            elif trips > days:
                l = m + 1
        return res


                

                

            
        