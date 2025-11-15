class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, l1 in enumerate(intervals):

            for i2, l2 in enumerate(intervals[i+1:]):
                if l2[0] <= l1[1]:

                    l1[0] = min(l1[0], l2[0])
                    l1[1] = max(l1[1], l2[1])

                    intervals.pop(i+1)
                else:
                    break
                    

        return intervals

                

