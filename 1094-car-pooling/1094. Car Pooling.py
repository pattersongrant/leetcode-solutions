class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        pickupat = defaultdict(int)
        dropoffat = defaultdict(int)
        maxVal = 0
        for count, pickup_i, dropoff_i in trips:
            pickupat[pickup_i] += count
            dropoffat[dropoff_i] += count
            maxVal = max(maxVal, dropoff_i)

        cur = 0
        for i in range(maxVal):
            if cur > capacity:
                return False
            cur -= dropoffat[i]
            if cur > capacity:
                return False
            cur += pickupat[i]
            if cur > capacity:
                return False
        
        return True
        
        

            




