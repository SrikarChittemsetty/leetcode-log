class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1

        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1
    assert s.strStr("hello", "ll") == 2
    assert s.strStr("a", "a") == 0
