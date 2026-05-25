from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have = 0
        required = len(need)
        left = 0
        best = float("inf")
        best_range = (0, 0)

        for right, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < best:
                    best = right - left + 1
                    best_range = (left, right)

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best == float("inf"):
            return ""

        start, end = best_range
        return s[start : end + 1]


if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    assert s.minWindow("ab", "b") == "b"
