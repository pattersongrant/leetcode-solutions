class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countsToElements = defaultdict(list)

        nums.sort()
        cur = 1
        maxCount = 1
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                cur += 1
            elif i > 0 and nums[i] != nums[i-1]:
                countsToElements[cur].append(nums[i-1])
                maxCount = max(maxCount, cur)
                cur = 1
        countsToElements[cur].append(nums[-1])
        maxCount = max(maxCount, cur)
        res = []
        count = 0

        for i in range(maxCount, -1, -1):
            if i in countsToElements:
                for elt in countsToElements[i]:
                    if count >= k: break
                    res.append(elt)
                    count += 1

        return res        



            



