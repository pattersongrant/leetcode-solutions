class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        for n in nums:
            if len(prefix) == 0:
                prefix.append(n * 1)
            else:
                prefix.append(n * prefix[-1])

        for i in range(len(nums) - 1, -1, -1):
            if len(postfix) == 0:
                postfix.append(nums[i] * 1)
            else:
                postfix.append(nums[i] * postfix[-1])

        res = [1] * len(nums)
        postfix = postfix[::-1]

        for i in range(len(nums)):
            if i > 0:
                res[i] *= prefix[i-1]
            if i < len(nums) - 1:
                res[i] *= postfix[i+1]

        return res



        

        