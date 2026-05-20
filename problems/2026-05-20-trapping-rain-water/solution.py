from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1

        return water


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
    assert s.trap([]) == 0
    assert s.trap([1, 2, 3]) == 0
    assert s.trap([3, 2, 1]) == 0
    assert s.trap([2, 0, 2]) == 2
