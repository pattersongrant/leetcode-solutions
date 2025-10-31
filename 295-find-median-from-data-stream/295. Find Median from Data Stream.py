class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if (self.maxHeap and self.minHeap and
            -self.maxHeap[0] > self.minHeap[0]):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if (len(self.maxHeap) > len(self.minHeap)):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if (len(self.maxHeap) < len(self.minHeap)):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

        
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        
        