class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            res = 0
            buy = prices[0]
        
            for cur in prices[1::]:
                res = max(res, cur-buy)
                buy = min(cur, buy)
        
            return res