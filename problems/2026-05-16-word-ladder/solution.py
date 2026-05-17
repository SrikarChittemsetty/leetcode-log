import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in alphabet:
                    newWord = word[:i] + ch + word[i + 1:]

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, length + 1))

        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert s.ladderLength("a", "c", ["a", "b", "c"]) == 2
