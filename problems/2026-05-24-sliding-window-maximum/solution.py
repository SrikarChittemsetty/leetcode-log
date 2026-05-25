from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for right, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(right)

            if dq[0] <= right - k:
                dq.popleft()

            if right >= k - 1:
                result.append(nums[dq[0]])

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([9, 11], 2) == [11]
    assert s.maxSlidingWindow([4, -2], 2) == [4]
