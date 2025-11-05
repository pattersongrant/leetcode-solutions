class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        aTob = {i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            aTob[a].append(b)

        visited = set()
        def dfs(crs):
            if aTob[crs] == []:
                return True

            if crs in visited:
                return False

            visited.add(crs)
            for pre in aTob[crs]:
                if not dfs(pre): 
                    return False
                
            visited.remove(crs)
            aTob[crs] = []
            return True
        
        for i in range(numCourses):

            if not dfs(i):
                return False
            

        return True


