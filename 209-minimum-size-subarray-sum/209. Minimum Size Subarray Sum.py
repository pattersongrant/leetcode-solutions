class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        s = 0
        while l < len(nums):
            if s < target:
                while s < target and r < len(nums):
                    s += nums[r]
                    r += 1
                if r == len(nums) and s < target:
                    break
            else:
                while s >= target:
                    s -= (nums[l])
                    l += 1
                res = min(r+1-l, res)

        return res if res != float('inf') else 0

            

        