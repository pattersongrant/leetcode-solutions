class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while r >= l:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            #if m is in the right side
            if nums[l] <= nums[m]:
                if nums [l] > target or target > nums[m]:
                    
                    l = m + 1
                else:
                    
                    r = m - 1

            else:
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1


        return -1