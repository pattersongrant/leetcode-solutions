class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = defaultdict(list) #letter : [first idx, last idx]
        for i, c in enumerate(s):
            letters[c].append(i)
        intervals = []
        for l in letters:
            if len(letters[l]) == 1:
                intervals.append([letters[l][0], letters[l][0]])
            else:
                intervals.append([letters[l][0], letters[l][-1]])
        
        res = []
        curMax = intervals[0][1]
        curMin = intervals[0][0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > curMax:
                res.append(curMax - curMin + 1)
                curMin = intervals[i][0]
                curMax = intervals[i][1]
            else:
                curMax = max(intervals[i][1], curMax)
        res.append(curMax - curMin + 1)
        return res


            


        

        