class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for inter in intervals[1::]:
            if inter[0] >= prevEnd:
                prevEnd = inter[1]
            else:
                count += 1
                prevEnd = min(inter[1], prevEnd)
            
        
        return count