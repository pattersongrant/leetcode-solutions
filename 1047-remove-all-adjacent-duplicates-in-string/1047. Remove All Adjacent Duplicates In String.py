class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        i = 1
        arr = []
        for c in s:
            arr.append(c)

        while i < len(arr):
            if arr[i-1] == arr[i]:
                arr.pop(i)
                arr.pop(i-1)
                if i != 1:
                    i -= 1
            else:
                i += 1


        return "".join(arr)




        

            
        