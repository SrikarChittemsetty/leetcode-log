# LeetCode 239: Sliding Window Maximum

## Metadata

- Difficulty: Hard
- Topic: Monotonic Deque / Sliding Window
- Result: Solved
- Link: https://leetcode.com/problems/sliding-window-maximum/

## Problem Summary

Given an array `nums` and window size `k`, return the maximum value in each
sliding window.

## Core Idea

Use a monotonic decreasing deque storing indices.

The deque stores candidate maximums. Values smaller than the new right value are
useless because the newer larger value will stay in the window longer.

## Key Realization

The front of the deque always stores the index of the current max.

Before reading the max:

- remove indices that fell out of the window from the front
- remove smaller values from the back

Store indices, not values, so window membership can be checked.

## Final Solution

```python
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for right, num in enumerate(nums):
            while dq and dq[0] <= right - k:
                dq.popleft()

            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(right)

            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
```

## Complexity

- Time: `O(n)`
- Space: `O(k)`

Each index is added and removed at most once.

## Retention Card

- Problem: 239. Sliding Window Maximum
- Difficulty: Hard
- Time Spent: ___
- Pattern: monotonic deque
- Trigger: repeated max over moving window
- Core Insight: remove useless smaller elements because they can never become max
- Template: decreasing deque storing indices
- Complexities: `O(n)` time, `O(k)` space

Process:

- Brute force recomputes max each window.
- Deque maintains candidates in decreasing order.
- Front always stores current max.

Mistakes:

- Remove out-of-window indices from front.
- Store indices, not values.
