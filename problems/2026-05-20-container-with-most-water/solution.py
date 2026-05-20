from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            best = max(best, width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([4, 3, 2, 1, 4]) == 16
    assert s.maxArea([1, 2, 1]) == 2
