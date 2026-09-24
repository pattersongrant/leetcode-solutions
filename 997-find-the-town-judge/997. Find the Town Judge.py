class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        truststhisperson = defaultdict(int)
        whotheytrust = defaultdict(int)

        for src, dst in trust:
            whotheytrust[src] += 1
            truststhisperson[dst] += 1

        for person in range(1,n+1):
            if whotheytrust[person] == 0 and truststhisperson[person] == n-1:
                return person
            

        return -1
