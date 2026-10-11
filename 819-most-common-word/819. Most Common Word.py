class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.split(r'[,|.|;|!|\s|?|\'|:|,]', paragraph)
        paragraph = Counter(paragraph)
        maxWord = ""
        maxWordCount = 0
        banned = set(banned)
        for word in paragraph:
            if paragraph[word] > maxWordCount and word not in banned and word != "":
                maxWord = word
                maxWordCount = paragraph[word]
        
        return maxWord