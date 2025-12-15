import math
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}


        for r in rectangles:
            ratio = r[0] / r[1]
            if ratio in count:
                count[ratio] += 1
            else:
                count[ratio] = 1
        tot = 0

        for ra in count:
            tot += (comb(count[ra], 2))
        return tot