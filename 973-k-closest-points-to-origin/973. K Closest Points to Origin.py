class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
                #need to create a min Heap sorted by distance but able to get points out of it
        #PYTHON sorts lists in a minHeap based on the FIRST ELEMENT

        heap = []
        for i in range(len(points)):
            heap.append([points[i][0]**2+points[i][1]**2,points[i][0], points[i][1]])


        heapq.heapify(heap)

        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append([popped[1], popped[2]])
        return res
        