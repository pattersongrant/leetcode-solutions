class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) #we've reached the leaf node. .copy() returns a copy of the subset as it will be modified.
                return
            
            subset.append(nums[i]) #decision to include nums[i]
            dfs(i + 1)


            #decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)

            


        return res