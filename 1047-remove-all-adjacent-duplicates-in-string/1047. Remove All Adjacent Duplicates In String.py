class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        arr = []

        for c in s:
            if arr and arr[-1] == c:
                arr.pop()
            else:
                arr.append(c)
        
        return "".join(arr)



        

            
        