class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        must take b before a

        return true if can finish all courses

        you can't finish a course if there is a cycle, i.e

        prerequisites: [a, b], [b, a]
        you need b to take a, but you also need a to take b. Therefore impossible

        my approach:
        Make a dictionary mapping course a to its prereqs

        Traverse each course from 0 to numCourses-1.
            if not in dictionary, continue
            if in dictionary, keep a set and keep checking dictionary for the prereqs of this course
            if set detects a cycle, return false
        
        if I get to end of loop, return true
        '''
        checked = set()
        seen = set()
        prereqs = defaultdict(list)
        for pair in prerequisites:
            a, b = pair[0], pair[1]
            if a == b:
                return False
            prereqs[a].append(b)
        
        def dfs(prereq):
            if prereq in seen:
                return False
            seen.add(prereq)

            for p in prereqs[prereq]:
                if not dfs(p):
                    return False
                seen.remove(p)
                checked.add(p)
            checked.add(prereq)
            return True
        for a in range(numCourses):
            checked.add(a)
            seen = set([a])
            if a not in prereqs:
                continue
            else:
                for prereq in prereqs[a]:
                    if prereq in checked:
                        continue
                    if not dfs(prereq):
                        return False
                    seen.remove(prereq)
            
                    

        return True






