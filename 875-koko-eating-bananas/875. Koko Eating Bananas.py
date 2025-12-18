class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #run the algorithm (0 + pilesMax) // 2
        #(it will never be more than pilesMax)
        # if the time is greater than h, run again on lower 

        # use binary search with variable x from 0 to h
        # to run the algorithm until you find the value of x that the pile can be eaten in h hours


        l, r = 1, max(piles)
        res = r
        while l <= r:
            time = 0
            m = (l + r) // 2

            for n in piles:
                time += math.ceil(n/m)
            if time <= h:
                res = m
                r = m - 1
            elif time > h:
                l = m + 1

        
        return res




            







