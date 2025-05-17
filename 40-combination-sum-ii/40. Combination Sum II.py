class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() #SORT so you can easily increment through dupe elements

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(candidates):
                return


            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()

            #whiel i+1 in bounds...
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1

            #skip candidates[i]
            dfs(i+1, cur, total)
                         
        
        dfs(0, [], 0)

        return res