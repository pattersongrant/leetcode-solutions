class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counts = Counter(s)
        
        maxHeap = []
        for let in counts:
            heapq.heappush(maxHeap, [-counts[let], let])
        
        res = []
        while maxHeap:
            if len(maxHeap) >= 2:
                count1, let1 = heapq.heappop(maxHeap)
                count2, let2 = heapq.heappop(maxHeap)
                if count1 != -1:
                    heapq.heappush(maxHeap, [count1+1, let1])
                if count2 != -1:
                    heapq.heappush(maxHeap, [count2+1,let2])
                res.append(let1)
                res.append(let2)
            else:
                count1, let1 = heapq.heappop(maxHeap)
                res.extend([let1] * -count1)

        res = "".join(res)
        for i in range(1,len(res)):
            if res[i] == res[i-1]:
                return ""
        
        return res
