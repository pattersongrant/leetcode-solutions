class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        [4,5,6,7,0,1,2]

        target = 4 -- return index of target or -1 if not there
        [6,7,0,1,2,4,5] 0 towards left
        [2,4,5,6,7,0,1] 0 towards right
        [1,2,4,5,6,7,0] 0 at end
        
        l, r = 0, 0
        m = (l+r) // 2

        if m is greater than r, then that means that m is in the rotated part of the array.
            if target is greater than m, then remove everything to the left of m
            if target is less than m
                if target greater than r, remove right side
                if target is less than r, remove left

        if m is less than r, then that is part of the 0-part of the array.
            if target is greater than r, then remove everything to right of m
            if target is less than r, then remove everything to left of m

        if m == target or l == target or r == target then return it
        '''

        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[l] == target:
                return l
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            
            if nums[m] > nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                if target > nums[r]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return - 1







