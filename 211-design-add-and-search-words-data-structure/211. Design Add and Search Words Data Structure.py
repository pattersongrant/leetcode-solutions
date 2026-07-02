'''
if there is a dot in search word - try every letter in children at that point until match or no more
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.quick = set()
    def addWord(self, word: str) -> None:
        self.quick.add(word)
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        if word in self.quick:
            return True
        def searchFromHere(start, remaining):
            cur = start
            for i, c in enumerate(remaining):
                if c not in cur.children:
                    if c == ".":
                        for next_c in cur.children:
                            if searchFromHere(cur.children[next_c], remaining[i+1::]):
                                return True
                    return False
                cur = cur.children[c]
            return cur.endOfWord



        return searchFromHere(self.root, word)

        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)