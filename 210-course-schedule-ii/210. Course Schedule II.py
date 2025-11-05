class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsToPre = {i:[] for i in range(numCourses)}
        res = []
        taken = set()
        for a, b in prerequisites:
            crsToPre[a].append(b)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            
            visit.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre): return False
                if pre not in taken:
                    res.append(pre)
                    taken.add(pre)
                

            crsToPre[crs] = []
            visit.remove(crs)
            if crs not in taken:
                res.append(crs)
                taken.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
            
            
            
