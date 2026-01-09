class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()

        l = 0
        maxB = 0
        res = [0] * len(queries)
        for q, i in queries:
            while l < len(items) and items[l][0] <= q:
                maxB = max(maxB, items[l][1])
                l += 1
            res[i] = maxB
        
        return res
            
            




            

