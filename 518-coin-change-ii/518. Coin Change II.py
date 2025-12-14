class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = [[0] * (len(coins) + 1) for _ in range(amount+1)]
        memo[0] = [1] * (len(coins) + 1)
        for a in range(1, amount+1):
            for c in range(len(coins) - 1, -1, -1):
                memo[a][c] += memo[a][c+1]
                if a - coins[c] >= 0:
                    memo[a][c] += memo[a-coins[c]][c]

        return memo[amount][0]    


            

            