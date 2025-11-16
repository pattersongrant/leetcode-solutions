class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #2 choices - include (but don't increment) OR go to next elt
        res = []

        cur = []


        def dfs(i, curSum):
            if i >= len(nums) or curSum >= target:
                if curSum == target:
                    res.append(cur.copy())
                return


            cur.append(nums[i])
            dfs(i, curSum + nums[i])

            cur.pop()
            dfs(i+1, curSum)

        dfs(0, 0)

        return res
            
            