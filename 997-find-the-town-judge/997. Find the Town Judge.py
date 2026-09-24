class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        truststhisperson = defaultdict(list)
        whotheytrust = defaultdict(list)

        for src, dst in trust:
            whotheytrust[src].append(dst)
            truststhisperson[dst].append(src)

        for person in range(1,n+1):
            if len(whotheytrust[person]) == 0 and len(truststhisperson[person]) == n-1:
                return person
            

        return -1
