class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        patterns = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        adj = defaultdict(list)

        for pattern in patterns:
            neighbors = patterns[pattern]
            for neighbor in neighbors:
                adj[neighbor].extend(neighbors)
        
        q = deque()
        q.append(beginWord)
        res = 1
        seen = set()
        while q:
            
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                seen.add(word)
                for w in adj[word]:
                    if w not in seen:
                        q.append(w)

            res += 1
        return 0
            




        

        

            
        
        