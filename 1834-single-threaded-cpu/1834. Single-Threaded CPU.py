class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        minHeap = []
        i = 0
        t = 0
        res = []
        freeAt = 0
        while minHeap or i < len(tasks):
            while i < len(tasks) and t >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]])
                i += 1
            
            if minHeap:
                popped = heapq.heappop(minHeap)
                res.append(popped[1])
                t += popped[0]
            else:
                t = tasks[i][0]
                

        return res

