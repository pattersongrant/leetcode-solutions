class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # have a set that you add and remove from of available nums
        # have a result set of tuples
        # use dfs to go through taking or skipping every element at every position
        available = Counter(nums)
        self.res = set()
        def dfs(available, cur):

            if len(cur) == len(nums):
                self.res.add(tuple(cur))
                return

            for num in available:
                if available[num] == 0:
                    continue
                cur.append(num)
                available[num] -= 1
                dfs(available, cur)
                available[num] += 1
                cur.pop()
            
        dfs(available, [])
        return [list(tup) for tup in self.res]