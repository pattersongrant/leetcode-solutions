class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        merge = intervals[0]

        for start, end in intervals:
            if start <= merge[1]:
                merge[1] = max(end, merge[1])
            
            else:
                res.append(merge)
                merge = [start, end]
        res.append(merge)
        return res
