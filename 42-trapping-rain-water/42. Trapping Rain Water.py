class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        l, r = 1, len(height)-2
        res = 0
        while l <= r:
            maxL = max(height[l-1], maxL)
            maxR = max(height[r+1], maxR)
            if maxL < maxR: 
                if (maxL - height[l]) > 0:
                    res += (maxL - height[l])
                l += 1
            else:
                if ((maxR - height[r]) > 0):
                    res += (maxR - height[r])
                r -= 1
        return res