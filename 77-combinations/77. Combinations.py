class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def dfs(cur, arr): #add all combinations starting with n to res
            if len(arr) == k:
                res.append(arr.copy())
                return
            if cur <= n:
                arr.append(cur)
                dfs(cur+1, arr)
                arr.pop()
                dfs(cur+1, arr)

        dfs(1, [])
        return res

