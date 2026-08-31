class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        place = 0

        for n in nums:
            if n != val:
                res += 1
                nums[place] = n
                place += 1
        return res