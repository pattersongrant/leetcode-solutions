class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #make sure to read the problem fully, each clause and example
        pair = [[p,s] for p, s in zip(position, speed)] #zip turns it into array of tuples
        stack = []
        for p, s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)