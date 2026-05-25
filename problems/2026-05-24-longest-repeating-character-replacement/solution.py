from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxFreq = 0
        best = 0

        for right, char in enumerate(s):
            count[char] += 1
            maxFreq = max(maxFreq, count[char])

            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("AAAA", 0) == 4
    assert s.characterReplacement("ABCDE", 1) == 2
