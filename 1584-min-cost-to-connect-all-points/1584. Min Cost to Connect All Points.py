class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #prim's
        weights = defaultdict(list) #point : array of distance to other points
        for i in range(len(points)):
            for j in range(len(points)):
                weights[i].append(abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1]))
        

        minHeap = [(0,0)]
        seen = set()
        res = 0
        while minHeap:
            newWeight, newPoint = heapq.heappop(minHeap)
            if newPoint in seen:
                continue
            seen.add(newPoint)
            res += newWeight

            for i in range(len(points)):
                heapq.heappush(minHeap, (weights[newPoint][i], i))
        
        return res
                



