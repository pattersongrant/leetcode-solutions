class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):       
            for c in coins:
                if i - c < 0: 
                    continue
                if dp[i - c] != -1:
                    if dp[i] == -1:
                        dp[i] = float('inf')
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount]

            