class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = {} #(i, cur) : num ways
        def dfs(i, cur):
            if i >= len(coins) or cur > amount:
                return 0
            if (i, cur) in memo:
                return memo[i, cur]
                
            if cur == amount:
                return 1

            res = 0
            res += dfs(i + 1, cur) #move forward
            res += dfs(i, cur + coins[i]) #take
            memo[i, cur] = res
            return res

        return dfs(0, 0)

            

            