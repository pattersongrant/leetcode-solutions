class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {} #(i, cur) : numWays

        self.ways = 0
        def dfs(i, cur):
            if i == len(nums):
                if cur == target:
                    return 1
                return 0
            if (i,cur) in memo:
                return memo[(i,cur)]

            memo[(i, cur)] = dfs(i + 1, cur - nums[i]) + dfs(i + 1, cur + nums[i])

            return memo[(i, cur)]

        return dfs(0,0)