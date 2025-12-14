class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for c in s:
            if c == "*":
                arr.pop()
                continue
            arr.append(c)

        return "".join(arr)

