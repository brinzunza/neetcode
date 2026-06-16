class WordDictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        currentMap = self.words
        for i in word:
            if i not in currentMap:
                currentMap[i] = {}
            currentMap = currentMap[i]
        currentMap['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '#' in node
            if word[i] == '.':
                for child in node:
                    if child != '#' and dfs(node[child], i + 1):
                        return True
                return False
            if word[i] not in node:
                return False
            return dfs(node[word[i]], i + 1)
        return dfs(self.words, 0)
