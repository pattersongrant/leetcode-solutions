class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(cur, used):

            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            
            for n in nums:
                if n not in used:
                    cur.append(n)
                    used.add(n)
                    dfs(cur, used)
                    used.remove(n)
                    cur.pop()


                

        dfs([], set())

        return res

        


        