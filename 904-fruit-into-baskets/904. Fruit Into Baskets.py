class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l = 0
        while l < len(fruits):
            print(l)
            baskets = set()
            locRes = 0
            newIdx = -1
            secondFound = False
            for j in range(l, len(fruits)):
                if fruits[j] in baskets:
                    locRes += 1
                    if fruits[j] == secondFruit and j > 0 and fruits[j-1] != secondFruit:
                        newIdx = j

                    
                elif fruits[j] not in baskets and len(baskets) < 2:
                    baskets.add(fruits[j])
                    locRes += 1
                    secondFruit = fruits[j]
                    newIdx = j
                else:
                    secondFound = True
                    l = newIdx - 1
                    break
            res = max(res, locRes)
            if not secondFound:
                break
            
            l += 1
        return res



        