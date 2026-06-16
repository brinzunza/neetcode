"""
BFS: for each word, find those that are one char difference and modify, then push into queue with updated step in tree
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord, 1))
        visited = set([beginWord])

        while queue:
            current, step = queue.popleft()
            if current == endWord:
                return step
            currChars = current

            for word in wordList:
                if word not in visited:
                    newChars = word
                    diff = 0
                    for a, b in zip(currChars, newChars):
                        if a != b:
                            diff += 1
                            if diff > 1:
                                break
                    if diff == 1:
                        queue.append((word, step + 1))
                        visited.add(word)

        return 0
