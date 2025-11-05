class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #add negative values
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)

        if len(self.minHeap) + 1 < len(self.maxHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        elif len(self.minHeap)  > 1+ len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

            
            

    def findMedian(self) -> float:


        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0]-self.maxHeap[0]) / 2.0
            
        elif len(self.maxHeap) > len(self.minHeap):
            
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()