class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                res = min(r+1-l, res)
                s -= (nums[l])
                l += 1
                

        return res if res != float('inf') else 0

            

        