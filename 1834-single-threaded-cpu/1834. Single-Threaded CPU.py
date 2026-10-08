class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        available = defaultdict(list)
        checkTimes = set()
        for i in range(len(tasks)):
            checkTimes.add(tasks[i][0]) 
            checkTimes.add(tasks[i][0]+tasks[i][1])
            available[tasks[i][0]].append([tasks[i][1], i])
        checkSet = checkTimes
        checkTimes = list(checkTimes)
        checkHeap = []
        for t in checkTimes:
            heapq.heappush(checkHeap, t)
        
        checkTimes.sort()
        checkTimes.append(checkTimes[-1]+1)
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

            
        
        