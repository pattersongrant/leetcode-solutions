class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        network of directed nodes (times)
        each edge has a weight (travel time), >= 0
        k = first node sending a signal from

        return either the minimum time to reach all nodes
        OR -1 if impossible

        My solution: use Prim's, as we're starting from a specific node and trying to build an MST.
        
        idea: build a map of neighbors

        start w/ k, adding it and it's neighbors to a min heap sorted by weight.
        then keep going, adding the lowest edge (if unseen so far)  and the neighbors connected to the newly connected node 
        '''

        minHeap = []
        neighbors = defaultdict(list) #node : list of (neighbor, edge)
        for t in times:
            node, target, time = t[0], t[1], t[2]
            neighbors[node].append((target, time))
        
        for neighbor, edge in neighbors[k]:
            heapq.heappush(minHeap, (edge, neighbor, k))


        seen = set()
        seen.add(k)


        
        res = 0
        while minHeap:
            edge, neighbor, cameFrom = heapq.heappop(minHeap)
            #if already visited w/ a smaller weight, skip it
            if neighbor in seen:
                continue

            
            #we've seen this new node now
            seen.add(neighbor)
            res = max(edge, res)

            #add all edges of newly added node
            for n1, e in neighbors[neighbor]:
                heapq.heappush(minHeap, (edge + e, n1, neighbor))

        if not len(seen) == n:
            return -1

        return res



        