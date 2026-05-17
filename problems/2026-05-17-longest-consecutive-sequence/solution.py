from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for num in elements:
            if num - 1 not in elements:
                length = 1

                while num + length in elements:
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    assert s.longestConsecutive([1, 2, 0, 1]) == 3
