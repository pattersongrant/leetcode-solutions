class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)

        res = 0
        for i in range(k):
            res = heapq.heappop(nums) * -1

        return res