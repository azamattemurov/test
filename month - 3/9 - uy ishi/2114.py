class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        uzun = 0
        count = 0
        for sentence in sentences:
            words = sentence.split()
            count = len(words)
            if count > uzun:
                uzun = count
        return uzun