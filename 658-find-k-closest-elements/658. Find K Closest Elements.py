class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []

        for i, n in enumerate(arr):
            heapq.heappush(minHeap, [abs(x-n), n])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        res.sort()
        return res
