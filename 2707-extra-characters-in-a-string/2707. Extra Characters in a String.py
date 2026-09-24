class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        '''
        dfs solution.
        turn dictionary into a set

        either take or skip every letter.
        skip = extra character

        and then if there is a chance to take a word, then take or skip every word


        return the time that you got to the end and had minimum extra characters
        '''

        dictionary = set(dictionary)
        res = len(s)
        seen = set()

        def dfs(i, curBuild, extraCharacters):
            #each iteration, you can add the letter to your curBuild or reset
            #extraCharacters stays the same unless you find a word, then you can subtract the length of that word
            nonlocal res
            # print((i,curBuild,extraCharacters))
            if (i,curBuild,extraCharacters) in seen:
                return
            seen.add((i,curBuild,extraCharacters))            
            if i == len(s):
                if curBuild in dictionary:
                    extraCharacters -= len(curBuild)
                res = min(res, extraCharacters)
                return
            let = s[i]
            inDict = True if curBuild in dictionary else False

            if inDict:
                dfs(i+1, let, extraCharacters - len(curBuild)) #reset curBuild
                dfs(i+1, curBuild+let, extraCharacters)
            else:
                dfs(i+1, curBuild+let, extraCharacters) #skip word / addToCurBuild
                dfs(i+1, let, extraCharacters) #reset curBuild
        
        dfs(0, "", len(s))
        return res
        