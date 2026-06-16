class PrefixTree:
    def __init__(self):
        self.levels = {}
        self.END = "#" 

    def insert(self, word: str) -> None:
        curr = self.levels
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr[self.END] = True

    def search(self, word: str) -> bool:
        curr = self.levels
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return self.END in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.levels
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
