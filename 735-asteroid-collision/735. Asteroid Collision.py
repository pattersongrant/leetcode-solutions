class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1,len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue
            inc = asteroids[i]
            top = stack[-1]

            if top < 0:
                stack.append(inc)
            elif top > 0:
                if inc < 0:
                    if abs(inc) > top:
                        while top > 0 and abs(inc) > top:
                            stack.pop()
                            if not stack:
                                break
                            top = stack[-1]
                        if abs(inc) > top:
                            stack.append(inc)
                    if abs(inc) == top:
                        stack.pop()
                else:
                    stack.append(inc)
        return stack