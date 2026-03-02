class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n1 = [nums1[i] for i in range(m)]
        
        n1cur = 0
        n2cur = 0
        cur = 0
        while n1cur != m or n2cur != n:
            if n1cur == m:
                nums1[cur] = nums2[n2cur]
                n2cur += 1
            elif n2cur == n:
                nums1[cur] = n1[n1cur]
                n1cur += 1
            
            elif n1cur < m and n1[n1cur] < nums2[n2cur]:
                nums1[cur] = n1[n1cur]
                n1cur += 1
            else:
                nums1[cur] = nums2[n2cur]
                n2cur += 1
            cur += 1


















        