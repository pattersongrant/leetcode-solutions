class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = Counter(s)
        res = 0
        maxOdd = [0]
        for letter in hashmap:
            n = hashmap[letter]

            if n % 2 != 0:
                if maxOdd and n > maxOdd[-1]:
                    maxOdd.append(n)
                    continue

            if n < 2:
                continue

            if n % 2 != 0:
                res += (n-1)
                continue
            res += n

        if maxOdd:
            res += maxOdd[-1]
            maxOdd.pop()

            for n in maxOdd:
                if n < 2:
                    continue
                res += (n-1)
        return res

            