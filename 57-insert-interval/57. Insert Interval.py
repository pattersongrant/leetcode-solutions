class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = newInterval
        res = []
        startIdx = new[0]
        endIdx = new[1]

        for old in intervals:
            if new[0] >= old[0] and new[0] <= old[1]:
                startIdx = old[0]

            if new[1] >= old[0] and new[1] <= old[1]:
                endIdx = old[1]
        
        added = False
        for old in intervals:
            if startIdx < old[0] and endIdx > old[1]:
                continue
            if old[0] == startIdx:
                if old[1] == endIdx:
                    print(old)
                    res.append([startIdx, endIdx])
                    added = True
                continue
            if old[1] == endIdx:
                print(old)
                res.append([startIdx, endIdx])
                added = True
                continue
            
            if not added and old[0] > endIdx:
                res.append([startIdx, endIdx])
                added = True
            res.append(old)
        if not added:
            res.append([startIdx, endIdx])
        return res
            
            
            



        
            

            
            
        


        

        
            
            