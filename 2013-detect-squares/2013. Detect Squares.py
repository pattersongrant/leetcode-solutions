'''
Brute force method:
given a point

    for every count call, check the 2 other places that if there is points there, then a square is formed
    this is O(n) for each count as each one only checks 4n places max

    No diagonal squares mean only points that are in line with the other one can be considered for a first point

    It's a stream though, so there may be an efficiently good way to keep the answer availabel as we go through the problem
'''
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int) #point : count
        self.rows = defaultdict(set) #row : set of points


    def add(self, point: List[int]) -> None:
        #update points, rows, cols
        self.points[tuple(point)] += 1
        self.rows[point[1]].add(tuple(point))
        
    def count(self, point: List[int]) -> int:
        #check rows and cols for in-line points
        #if any are found, then for each point check if the two points exist that make it a square
        res = 0
        for p in self.rows[point[1]]:
            length = abs(p[0] - point[0])
            if [p[0], p[1]] == point:
                continue

            if self.points[p] and self.points[(p[0], p[1] + length)] and self.points[(point[0], point[1] + length)]:
                res += (self.points[p] * self.points[(p[0], p[1] + length)] * self.points[(point[0], point[1] + length)])
            if self.points[p] and self.points[(p[0], p[1] - length)] and self.points[(point[0], point[1] - length)]:
                res += (self.points[p] * self.points[(p[0], p[1] - length)] * self.points[(point[0], point[1] - length)])


        return res
            
        
        

        
