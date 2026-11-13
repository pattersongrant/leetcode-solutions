class Solution:
    def numSquares(self, n: int) -> int:

        cache = {}
        perfs = []
        for i in range(1,n+1):
            if i**(0.5) == int(i**0.5):
                cache[i] = 1
                perfs.append(i)
            else:
                cache[i] = i
                for perf in perfs:
                    cache[i] = min(cache[i], cache[i-perf] + cache[perf])

        return cache[n]

        