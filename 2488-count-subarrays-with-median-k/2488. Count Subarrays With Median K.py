class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        idx = nums.index(k)


        counts = defaultdict(int)
        #l1 = larger
        #s1 = smaller
        s1 = l1 = res = 0
        for i in reversed(range(idx)):
            if nums[i] > k:
                l1 += 1
            elif nums[i] < k:
                s1 += 1
            counts[(l1-s1)] += 1
            # counts[(s1-l1)] += 1

            if l1-s1==0 or l1-s1==1: res += 1
        
        s2 = l2 = 0
        for i in range(idx+1, len(nums)):
            if nums[i] < k:
                s2 += 1
            if nums[i] > k:
                l2 += 1

            res += counts[s2-l2] + counts[s2-l2+1]

            if l2-s2==0 or l2-s2==1: res += 1
        return res + 1



            
        