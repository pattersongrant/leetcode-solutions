class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #make dictionary with number : index
        for i, n in enumerate(nums):
            diff=target-n
            #check if the required number(diff) is in the hashmap already
            if diff in hashmap:
                return [hashmap[diff], i]
                #if it is, return the correct answer by getting the index of the difference from hashmap(hashmap[diff]) and the index of the current number checking in the loop from nums (i).
            hashmap[n]=i
            #if the difference is not in the hashmap already, add the current number of the loop (n) to the hashmap and then go through the loop again checking the next number from nums
