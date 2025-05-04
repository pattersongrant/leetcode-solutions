import math
from math import comb
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        totalCount = {}
        
        for n in dominoes:
            if tuple(sorted(n)) not in totalCount:
                totalCount[tuple(sorted(n))] = 0
            totalCount[tuple(sorted(n))] += 1


        total = 0
        for i in totalCount:
            total += comb(totalCount[i], 2)
        return total
            

