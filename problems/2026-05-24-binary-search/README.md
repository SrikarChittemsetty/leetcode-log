# LeetCode 704: Binary Search

## Metadata

- Difficulty: Easy
- Topic: Binary Search
- Result: Solved
- Link: https://leetcode.com/problems/binary-search/

## Problem Summary

Given a sorted array `nums` and a target, return the target's index or `-1` if
it does not exist.

## Core Idea

Use binary search.

Sorted order lets each midpoint comparison discard half of the remaining search
space.

## Final Solution

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Retention Card

- Problem: 704. Binary Search
- Difficulty: Easy
- Time Spent: ___
- Pattern: binary search
- Trigger: sorted array lookup
- Core Insight: sorted order lets half of search space be discarded each step
- Template: compare mid to target and shrink accordingly
- Complexities: `O(log n)` time, `O(1)` space

Process:

- Linear search wastes sorted property.
- Mid comparison determines impossible half.
- Repeatedly halve search space.

Mistakes:

- Use `while l <= r`.
- Update with `mid +/- 1`.
