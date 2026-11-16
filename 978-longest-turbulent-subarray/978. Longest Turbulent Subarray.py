class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            return 2 if arr[0] != arr[1] else 1
        res = 1
        last = 0 #0, 1, or 2 : none, left greater, right greater
        if arr[0] > arr[1]:
            last = 1
            cur = 2
        elif arr[0] < arr[1]:
            last = 2
            cur = 2
        else:
            last = 0
            cur = 1
        res = max(res, cur)
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                if last == 2:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 2
                last = 1
            elif arr[i-1] < arr[i]:
                if last == 1:
                    cur += 1
                    res = max(res,cur)
                else:
                    cur = 2
                res = max(res,cur)
                last = 2
            else:
                last = 0
                cur = 1
                res = max(res,cur)
        return res
                

        