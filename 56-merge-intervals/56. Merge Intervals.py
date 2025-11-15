class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]


        for i, li in enumerate(intervals[1:]):
            if li[0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0], li[0])
                res[-1][1] = max(res[-1][1], li[1])
            else:
                res.append(li)
                    

        return res

                

