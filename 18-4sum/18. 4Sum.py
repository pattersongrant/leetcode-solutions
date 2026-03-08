class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        print(i,j,l,r)
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        r -= 1
                        l += 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l += 1
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
                
        return res


                    
                    
                

            

        



