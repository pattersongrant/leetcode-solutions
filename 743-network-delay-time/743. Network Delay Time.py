class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Dijkstra's
        minHeap = []
        neighbors = defaultdict(list) #node : list of (neighbor, edge)
        for u,v,w in times:
            neighbors[u].append((v,w))
    
        minHeap = [(0, k)]
        seen = set()
        res = 0
        while minHeap:
            edge, neighbor = heapq.heappop(minHeap)
            #if already visited w/ a smaller weight, skip it
            if neighbor in seen:
                continue
            #we've seen this new node now
            seen.add(neighbor)
            res = max(edge, res)

            #add all edges of newly added node
            for n1, e in neighbors[neighbor]:
                if n1 not in seen:
                    heapq.heappush(minHeap, (edge + e, n1))

        return res if len(seen) == n else -1



        