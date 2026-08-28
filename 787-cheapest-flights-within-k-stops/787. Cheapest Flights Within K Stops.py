class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #just do dijkstras and if stops count gets greater than k then return -1, otherwise return the total cost
        # dijkstra's - select the next edge that's smallest in weight away from the source
        # at the end, return the weight away from the source of dst
        # keep each stop tracked as a second variable how many stops from src
        #1. build adj list
        #2. run dijkstra's w/ minHeap, res, stops, 
        # don't update res if the stops are too much
        # eventually it will get to one that has proper stops and expensive even if earlier cheaper flights stack up

        # only update res if stopCount <= k+1 on dst

        adj = {i:[] for i in range(n)}
        for fr,to,price in flights:
            adj[fr].append((to, price))

        minH = [(0,src,0)] #(totalWeightFromSrc, loc, stopCount)
        seen = {} # loc : minStopCountSoFar
        while minH:
            weight, loc, stopCount = heapq.heappop(minH)
            if loc in seen and seen[loc] <= stopCount:
                continue
            seen[loc] = stopCount

            if loc == dst and stopCount <= k+1:
                return weight

            for nei, price in adj[loc]:
                if stopCount + 1 <= k+1:
                    heapq.heappush(minH, (weight + price, nei, stopCount + 1))

        return -1

