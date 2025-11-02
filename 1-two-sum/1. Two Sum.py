class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {} #number : index
    
        for i, n in enumerate(nums):
            
            if target-n in hashmap:
                return [i, hashmap[target-n]]
            
            if n not in hashmap:
                hashmap[n] = i
        

            
            
                


