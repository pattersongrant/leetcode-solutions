class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        count = 0

        for i in range(len(people) - 1, -1, -1):
            if l > i:
                break

            if people[i] + people[l] <= limit:
                l += 1
            
            count += 1
        
        return count

            

                



        
            
