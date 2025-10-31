class Solution:
    def jump(self, nums: List[int]) -> int:
        furthestNext = 0
        bestNextIdx = 0
        curJumpIdx = 0
        curJumpDistance = nums[0]
        jumps = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            furthestNext = max(i+nums[i], furthestNext)
            if furthestNext == i+nums[i]:
                bestNextIdx = i
            if i == len(nums) - 1:
                return jumps + 1
            if i+1 > curJumpDistance + curJumpIdx:
                curJumpIdx = bestNextIdx
                curJumpDistance = nums[bestNextIdx]
                jumps += 1
                if curJumpDistance + curJumpIdx >= len(nums) - 1:
                    return jumps + 1