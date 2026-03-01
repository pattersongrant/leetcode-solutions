class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merge = [100000000, -10000000]
        res = []
        
        for i in range(len(intervals)):
            if i+1 < len(intervals) and (intervals[i+1][0] <= intervals[i][1] or intervals[i+1][0] <= merge[1]):
                merge[0] = min(intervals[i][0], merge[0])
                merge[1] = max(intervals[i+1][1], intervals[i][1], merge[1])

            elif merge == [100000000, -10000000]:
                res.append(intervals[i])
            else:
                res.append(merge)
                merge = [100000000, -10000000]
        return res
        