class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res = 0
        cache = {}
        
        def dfs(curSum, cur):
            if (curSum) in cache:
                self.res += cache[(curSum)]
                return cache[(curSum)]

            if curSum >= target:
                if curSum == target:
                    self.res += 1
                    return 1
                else:
                    return 0

            res = 0
            for n in nums:
                cur.append(n)
                res += dfs(curSum + n, cur)
                cur.pop()


            cache[(curSum)] = res
            return cache[(curSum)]

        dfs(0,[])
        return self.res



