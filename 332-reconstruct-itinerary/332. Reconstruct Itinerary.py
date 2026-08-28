class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        tickets = tickets[::-1]
        
        for t in tickets:
            adj[t[0]].append(t[1])
        
        stack = ["JFK"]
        res = []
        
        while stack:
            cur = stack[-1]
            if not adj[cur]:
                res.append(stack.pop())
            else:
                stack.append(adj[cur].pop())
                
        return res[::-1]
        



        
