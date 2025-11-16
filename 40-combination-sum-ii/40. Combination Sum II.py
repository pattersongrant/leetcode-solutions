class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        candidates.sort()

        def dfs(i, curSum):
            if i >= len(candidates) or curSum >= target:
                if curSum == target:
                    res.append(cur.copy())
                return

            cur.append(candidates[i])
            dfs(i+1, curSum + candidates[i])

            cur.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+= 1

            dfs(i+1, curSum)
                
        dfs(0, 0)
        return res

