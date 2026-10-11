class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(arr1, arr2):
            res = []
            i, j = 0, 0
            while i < len(arr1) or j < len(arr2):
                val1 = arr1[i] if i < len(arr1) else float('inf')
                val2 = arr2[j] if j < len(arr2) else float('inf')
                if val1 <= val2:
                    i += 1
                    res.append(val1)
                else:
                    j += 1
                    res.append(val2)

            return res

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            m = (len(arr)-1) // 2
            return merge(mergeSort(arr[:m+1]), mergeSort(arr[m+1:]))

        return mergeSort(nums)

