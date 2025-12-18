class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}

        def topDown(x):
            if x == 0:
                return 0
            elif x == 1 or x == 2:
                return 1
            else:
                if x in memo:
                    return memo[x]
                memo[x] = topDown(x-2) + topDown(x-1) + topDown(x-3)
                return memo[x]


        return topDown(n)