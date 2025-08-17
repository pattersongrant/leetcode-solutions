class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2


        sums = {0}
        for i in range(len(nums) - 1, -1, -1):
            
            newSums = sums.copy()

            for s in sums:
                newSums.add(s+nums[i])
            
            sums = newSums
            if target in sums:
                return True

        return False
