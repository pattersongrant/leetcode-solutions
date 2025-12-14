class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = [[-1 for _ in range(amount)] for _ in range(len(coins) + 1)] #(i, cur) : num ways
        def dfs(i, cur):
            if cur == amount:
                return 1
            if i >= len(coins) or cur > amount:
                return 0
            if memo[i][cur] != -1:
                return memo[i][cur]




            res = 0
            res += dfs(i + 1, cur) #move forward
            res += dfs(i, cur + coins[i]) #take
            memo[i][cur] = res
            return res

        return dfs(0, 0)

            

            