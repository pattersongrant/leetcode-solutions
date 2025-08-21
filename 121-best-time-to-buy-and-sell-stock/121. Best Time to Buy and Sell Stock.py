class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        maxProfit = 0

        for n in prices:
            if n - minValue > maxProfit:
                maxProfit = n - minValue
            if n < minValue:
                minValue = n

        return maxProfit

        