class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maxAtEachPrice = []

        curMax = 0
        for i in range(len(items)):
            if i > 0 and items[i][0] != items[i-1][0]:

                maxAtEachPrice.append((items[i-1][0], curMax))
                curMax = max(curMax, items[i][1])
            else:
                curMax = max(curMax, items[i][1])
        curMax = max(curMax, items[-1][1])
        maxAtEachPrice.append((items[-1][0], curMax))

        res = []

        for q in queries:
            maxQuality = 0
            l, r = 0, len(maxAtEachPrice) - 1

            while l <= r:
                m = (l+r) // 2
                if maxAtEachPrice[m][0] > q:
                    r = m - 1
                elif maxAtEachPrice[m][0] < q:
                    l = m + 1
                    maxQuality = max(maxQuality, maxAtEachPrice[m][1])
                else:
                    maxQuality = max(maxQuality, maxAtEachPrice[m][1])
                    break
            res.append(maxQuality)
        
        return res

                    

                



        
        

        
                    




                    
                    

        