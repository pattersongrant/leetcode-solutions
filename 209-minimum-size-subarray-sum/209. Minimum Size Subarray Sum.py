class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        s = 0
        while l < len(nums):
            if s < target:
                if r == len(nums):
                    break
                s += nums[r]
                r += 1
            else:
                while s >= target:
                    res = min(r-l, res)
                    s -= (nums[l])
                    l += 1

        return res if res != float('inf') else 0

            

        