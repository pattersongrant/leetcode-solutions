class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        maps = []

        def dfs():
            s = sum(subset)
            if s >target:
                return
            x = {}
            for n in subset:
                if n in x:
                    x[n] += 1
                else:
                    x[n] = 1
            



            if s == target and x not in maps:
                res.append(subset.copy())
                maps.append(x)

    

            for n in nums:
                subset.append(n)
                dfs()
                subset.pop()

        dfs()
        return res
            