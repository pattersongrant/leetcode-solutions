class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        traverse left to right
        count opens and stars

        if opens > 0 and star:
            use current star as a close
            starsUsedToClose += 1 This can be undone, if another close is found.
            opens -= 1
        
        if opens == 0 and star:
            starsForOpen += 1
        
        if close and opens == 0:
            if starsForOpen > 0: Use unused star as an open
                starsForOpen -= 1 This cannot be undone. There will never be an open in the past.
        
        if close and opens > 0:
            if starsUsedToClose > 0:
                starsForOpen += 1
                starsUsedToClose -= 1
            opens -= 1

        '''
        #keep these running. As parentheses get closed, subtract from opens.
        opens = 0
        starsForOpen = 0
        starsUsedToClose = 0

        for c in s:
            if c == "(":
                opens += 1

            elif c == "*":
                if opens > 0:
                    starsUsedToClose += 1
                    opens -= 1
                else:
                    starsForOpen += 1

            else:
                if opens == 0 and starsUsedToClose == 0: #if there is no opens and no stars were used to close
                    if starsForOpen > 0:
                        starsForOpen -= 1
                    else:
                        return False
                elif opens == 0 and starsUsedToClose > 0: #if there is no opens and stars were used to close
                    starsForOpen += 1
                    starsUsedToClose -= 1

                elif opens > 0:
                    # if starsUsedToClose > 0:
                    #     starsForOpen += 1
                    #     starsUsedToClose -= 1
                    opens -= 1
        return opens == 0


