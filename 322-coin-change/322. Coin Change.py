class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for i in range(1, amount+1):
            dp[i] = 2**31           
            for c in coins:
                if i - c < 0 or dp[i - c] == 2**31: 
                    continue
                dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[amount] == 2 **31:
            return -1
        return dp[amount]

            