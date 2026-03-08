class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rightStack = []
        res = []
        for n in asteroids:
            if n > 0: 
                rightStack.append(n)
            else:
                negExploded = False
                while rightStack and rightStack[-1] <= abs(n):
                    if rightStack[-1] == abs(n):
                        rightStack.pop()
                        negExploded = True
                        break
                    else: 
                        rightStack.pop()
                if not rightStack and not negExploded:
                    res.append(n)
        res.extend(rightStack)
        return res

                





        