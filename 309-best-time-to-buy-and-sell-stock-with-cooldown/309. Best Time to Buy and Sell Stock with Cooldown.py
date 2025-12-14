class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {} #(i, buying, cur) : maxValue

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            cooldown = dfs(i+1, buying)
            buysell = 0
            if buying == True: 
                buysell = dfs(i+1, False) - prices[i]
            else:
                buysell = dfs(i + 2, True) + prices[i]
            res = max(buysell, cooldown)
            memo[(i, buying)] = res
            return res
        
        return dfs(0, True)

            


