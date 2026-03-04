class Solution:
    def reverse(self, x: int) -> int:
        
        negative = x < 0
        x = abs(x)
        twoToThirtyOne = "2147483648"
        x = str(x)[::-1]


        if len(x) > len(twoToThirtyOne):
            return 0

        elif len(x) < len(twoToThirtyOne):
            return -int(x) if negative else int(x)
        else:
            for i in range(len(x)):
                if x[i] > twoToThirtyOne[i]:
                    return 0
                if x[i] == twoToThirtyOne[i]:
                    continue
                if x[i] < twoToThirtyOne[i]:
                    return -int(x) if negative else int(x)

