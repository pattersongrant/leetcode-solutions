class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -10
        totalprod = 1
        for i in nums:
            totalprod *= i
        if totalprod > 0:
            return totalprod


        for i in range(0,len(nums)):
            if nums[i] > res:
                res = nums[i]
            subproduct = nums[i]
            for j in range(i+1, len(nums)):
                subproduct *= nums[j]
                if subproduct > res:
                    res = subproduct

        return res
                