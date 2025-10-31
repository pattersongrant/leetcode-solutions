class Solution:
    def isHappy(self, n: int) -> bool:
        nStr = str(n)
        seen = set()
        while nStr != "" and nStr != "1":
            res = 0
            for i in range(len(nStr)):
                intv = int(nStr[i:i+1])
                res += (intv ** 2)
                print(res)
            if res in seen:
                return False
            seen.add(res)
            nStr = str(res)
            print(nStr)

        return nStr == "1"
