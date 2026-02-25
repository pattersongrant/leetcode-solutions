class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        furthest = 0

        for i, n in enumerate(nums):
            if i <= furthest:
                furthest = max(furthest, i+n)
            
        return furthest >= len(nums) - 1
            