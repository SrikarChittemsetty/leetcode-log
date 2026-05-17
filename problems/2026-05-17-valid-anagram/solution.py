class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = {}

        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        for c in t:
            if c not in freq_map:
                return False

            freq_map[c] -= 1

            if freq_map[c] < 0:
                return False

        return all(val == 0 for val in freq_map.values())


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    assert s.isAnagram("aacc", "ccac") is False
    assert s.isAnagram("", "") is True
