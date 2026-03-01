class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        res = target + 1000000 #sum of 3 integers
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
            
                if abs(target - tot) < abs(target - res):
                    res = tot
                if tot > target:
                    r -= 1
                elif tot < target:
                    l += 1
                else:
                    return tot
        return res
            

            
