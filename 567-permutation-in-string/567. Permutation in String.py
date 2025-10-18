class Solution:
    def isPermutation(self, one, two):
        for key in one:
            if key in two:
                if one[key] != two[key]:
                    return False
            else:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for i in range(len(s1)):
            target[s1[i]] = 1 + target.get(s1[i], 0)

        count = {}
        l = 0
        curLen = 0
        print(target)
        for r in range(len(s2)):

            if self.isPermutation(target, count):
                return True
            count[s2[r]] = 1 + count.get(s2[r], 0)
            curLen += 1
            
            if curLen > len(s1):
                count[s2[l]] -= 1
                if (count[s2[l]] == 0):
                    count.pop(s2[l])
                l+=1
            print(count)
            if self.isPermutation(target, count):
                return True

            

        return False
        