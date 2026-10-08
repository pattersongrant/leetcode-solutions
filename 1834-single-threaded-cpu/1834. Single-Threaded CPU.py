class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        available = defaultdict(list)
        checkSet = set()
        checkHeap = []
        for i in range(len(tasks)):
            if tasks[i][0] not in checkSet:
                heapq.heappush(checkHeap, tasks[i][0])
            if tasks[i][0]+tasks[i][1] not in checkSet:
                heapq.heappush(checkHeap, (tasks[i][0]+tasks[i][1]))
            checkSet.add(tasks[i][0])
            checkSet.add(tasks[i][0]+tasks[i][1])
            available[tasks[i][0]].append([tasks[i][1], i])
        
        selectHeap = []
        freeAt = 0
        res = []

        while checkHeap:
            i = heapq.heappop(checkHeap)
            if i in available:
                for li in available[i]:
                    heapq.heappush(selectHeap, li)
            if i >= freeAt:
                if selectHeap:
                    run = heapq.heappop(selectHeap)
                    res.append(run[1])
                    freeAt = run[0] + i
                    if freeAt not in checkSet:
                        checkSet.add(freeAt)
                        heapq.heappush(checkHeap, freeAt)

        while selectHeap:
            res.append(heapq.heappop(selectHeap)[1])

        return res

            
        
        