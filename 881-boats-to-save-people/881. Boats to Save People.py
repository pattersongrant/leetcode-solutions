class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0

        count = 0
        cur = 0

        for i in range(len(people) - 1, -1, -1):
            
            if l > i:
                break
            cur = people[i]
            curCount = 1
            while cur < limit and l < i and curCount < 2:
                cur += people[l]
                curCount += 1
                l += 1
            
            count += 1


            if cur > limit: #if last added boat exceeded limit
                l -= 1
            cur = 0
        
        return count

            

                



        
            
