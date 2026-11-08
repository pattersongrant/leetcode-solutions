class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for a in range(len(nums)):
            if a - 1 >= 0 and nums[a] == nums[a-1]:
                continue
            b = a+1
            while b < len(nums)-2:
                l = b+1
                r = len(nums)-1
                s = nums[a]+nums[b]+nums[l]+nums[r]
                
                while l < r:
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append([nums[a],nums[b],nums[l],nums[r]])
                        l += 1
                        while l < len(nums)-1 and nums[l] == nums[l-1]:
                            l += 1




                    s = nums[a]+nums[b]+nums[l]+nums[r]
                b += 1
                while b < len(nums) and nums[b] == nums[b-1]:
                    b += 1
        return res


        
        