class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        differenceCounts = [[] for _ in range(max(abs(min(arr)),max(arr))+abs(x)+1)]
        print(abs(max(arr)))
        print(abs(x))
        print(len(differenceCounts))
        for n in arr:
            if (abs(x-n) > len(differenceCounts)-1):
                print("too big",abs(x-n))
            differenceCounts[abs(x-n)].append(n)
        
        res = []
        j = 0
        i = 0
        while i < k:
            while j < len(differenceCounts) and differenceCounts[j] == []:
                print("j",j)
                j += 1
            
            for elt in differenceCounts[j]:
                if i == k:
                    break
                res.append(elt)
                i += 1
            j += 1
        res.sort()
        return res

            

            

        return res
