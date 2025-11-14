class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = prices[0]

        for n in prices:
            res = max(res, n-minVal)
            minVal = min(minVal, n)

        return res