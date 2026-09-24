class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        delta = defaultdict(int)


        for src, dst in trust:
            delta[src] -= 1
            delta[dst] += 1

        for person in range(1,n+1):
            if delta[person] == n-1:
                return person
            

        return -1
