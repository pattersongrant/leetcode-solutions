class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for val in count:
            count_val = count[val]
            print(count_val)
            if bucket[count_val] == None:
                bucket[count_val] = [val]
            else:
                bucket[count_val].append(val)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if len(res) >= k: break
            for num in bucket[i]:
                if len(res) >= k: break
                res.append(num)

        return res
        