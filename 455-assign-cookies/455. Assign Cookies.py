class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cur_s = 0
        cur_g = 0
        while cur_g < len(g):
            if cur_s == len(s):
                return cur_g
            elif g[cur_g] > s[cur_s]:
                cur_s += 1
            else:
                cur_g += 1
                cur_s += 1
        
        return cur_g
        
        