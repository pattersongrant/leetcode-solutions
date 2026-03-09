class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numToIdx = {}

        for i, n in enumerate(nums):
            if target-n in numToIdx:
                return [i, numToIdx[target-n]]
            numToIdx[n] = i