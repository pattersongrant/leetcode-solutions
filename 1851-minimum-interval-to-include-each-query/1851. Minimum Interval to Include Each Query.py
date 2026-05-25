class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #keep a minHeap w/ (length, right[i])
        #keep a hashmap mapping queries to positons

        minHeap = []
        intervals.sort()
        curInt = 0
        resMap = {}
        '''
        only add interval to minHeap, if the start index is less than the query
        add all the intervals until the start index > query

        when adding to minHeap, pop until there is an interval where the right[i] is less than query
        '''
        for query in sorted(queries):
            if query in resMap:
                continue
            # add all valid start idx intervals
            while curInt != len(intervals) and intervals[curInt][0] <= query:
                i = intervals[curInt]
                heapq.heappush(minHeap, (i[1]-i[0]+1, i[1]))
                curInt += 1

            # pop minHeaps that end too early
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            if minHeap:
                resMap[query] = minHeap[0][0]
            else:
                resMap[query] = -1
        
        res = []
        for q in queries:
            res.append(resMap[q])
        
        return res
            

            
            


            

                






