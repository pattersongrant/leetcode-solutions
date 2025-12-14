class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {} #(i, cur) : numWays

        self.ways = 0
        def dfs(i, cur):
            if i == len(nums):
                if cur == target:
                    self.ways += 1
                    return 1
                return 0
            if (i,cur) in memo:
                self.ways += memo[(i, cur)]
                return memo[(i,cur)]
            res = 0
            res += dfs(i + 1, cur - nums[i])
            res += dfs(i + 1, cur + nums[i])

            memo[(i, cur)] = res

            return res

        
        dfs(0,0)
        return self.ways