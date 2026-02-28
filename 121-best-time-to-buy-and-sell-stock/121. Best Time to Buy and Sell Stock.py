class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for n in prices:
            res = max(res, n-buy)
            buy = min(buy, n)
        
        return res