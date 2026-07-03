'''
construct a trie w/ every word in words
go through the board
    at every postition, check if an adjacent nodes in the children
        if it is, keep following until no more (while adding found end of words to self.res)
'''

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.added = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        def insert(word):
            cur = self.root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
        
        for w in words:
            insert(w)

        ROWS, COLS = len(board), len(board[0])
        self.res = []
        def findWordsFromHere(r, c, curString, seen, curNode):
            if (r,c) in seen:
                return
            seen.add((r,c))
            if curNode.endOfWord and not curNode.added:
                self.res.append(curString + board[r][c])
                curNode.added = True
                    
            if r+1 < ROWS and board[r+1][c] in curNode.children:
                findWordsFromHere(r+1, c, curString + board[r][c], seen, curNode.children[board[r+1][c]])
            if r-1 >= 0 and board[r-1][c] in curNode.children:
                findWordsFromHere(r-1, c, curString + board[r][c], seen, curNode.children[board[r-1][c]])
            if c+1 < COLS and board[r][c+1] in curNode.children:
                findWordsFromHere(r, c+1, curString + board[r][c], seen, curNode.children[board[r][c+1]])
            if c-1 >= 0 and board[r][c-1] in curNode.children:
                findWordsFromHere(r, c-1, curString + board[r][c], seen, curNode.children[board[r][c-1]])
            seen.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in self.root.children:
                    findWordsFromHere(r, c, "", set(), self.root.children[board[r][c]])
        
        return self.res
                

        



