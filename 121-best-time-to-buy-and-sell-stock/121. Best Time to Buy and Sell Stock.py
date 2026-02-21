class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = prices[0]

        for n in prices:
            if n-minVal > res:
                res = n - minVal
            if minVal > n:
                minVal = n

        return res