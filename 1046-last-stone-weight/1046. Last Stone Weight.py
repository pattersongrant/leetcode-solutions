class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if (x == y): 
                continue
            else: # y is greater than x
                new = abs(y) - abs(x)
                heapq.heappush(stones, new * -1)


        if len(stones) == 1:
            return stones[0] * -1
        if len(stones) == 0:
            return 0