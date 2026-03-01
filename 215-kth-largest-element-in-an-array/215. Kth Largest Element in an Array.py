class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        buckets = [0] * (abs(min(nums)) + max(nums) + 1)

        offset = abs(min(nums))

        for n in nums:
            if n < 0:
                buckets[offset - abs(n)] += 1
            else:
                buckets[n + offset] += 1
        
        seen = 0
        for i in range(len(buckets) - 1, -1, -1):
            seen += buckets[i]
            if seen >= k:
                return (i - offset)    
            

        