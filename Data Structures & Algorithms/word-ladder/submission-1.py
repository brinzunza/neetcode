class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nodes = {}
        nodes[beginWord] = []

        for word in wordList:
            nodes[word] = []

        def difference(word1, word2):
            different = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    different += 1
            return different

        for word1 in nodes:
            for word2 in nodes:
                if word1 != word2 and difference(word1, word2) == 1:
                    nodes[word1].append(word2)

        queue = deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            current, count = queue.popleft()

            if current == endWord:
                return count

            for i in nodes[current]:
                if i not in visited:
                    queue.append((i, count + 1))
                    visited.add(i)

        return 0