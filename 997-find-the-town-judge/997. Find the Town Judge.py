class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        truststhisperson = defaultdict(set)
        whotheytrust = defaultdict(set)

        for src, dst in trust:
            whotheytrust[src].add(dst)
            truststhisperson[dst].add(src)

        for person in range(1,n+1):
            if len(whotheytrust[person]) == 0 and len(truststhisperson[person]) == n-1:
                return person
            

        return -1
