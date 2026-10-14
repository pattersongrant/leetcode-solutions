class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lowBound = 0
        highBound = k-1
        bestLowBound = 0
        bestHighBound = k-1

        tot = 0
        for i in range(highBound+1):
            tot += abs(arr[i]-x)
        res = tot
        print(lowBound,highBound,tot)
        
        while highBound < len(arr)-1:
            print(lowBound,highBound,tot)
            tot -= abs(arr[lowBound]-x)
            highBound +=1
            lowBound += 1
            tot += abs(arr[highBound]-x)
            if res > tot:
                bestLowBound = lowBound
                bestHighBound = highBound
                res = tot
            
        
        return arr[bestLowBound:bestHighBound+1]
            
