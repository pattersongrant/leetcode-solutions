class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        minHeap = []

        for i in range(k):
            heapq.heappush(minHeap, (-nums[i], i))

        res = []
        res.append(-minHeap[0][0])
        count = 0
        for r in range(k, len(nums)):
            heapq.heappush(minHeap, (-nums[r], r))

            while minHeap[0][1] <= r-k:
                heapq.heappop(minHeap)

            res.append(-minHeap[0][0])
        
        return res




        

        





        
        