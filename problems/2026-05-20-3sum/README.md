# LeetCode 15: 3Sum

## Metadata

- Difficulty: Medium
- Topic: Sorting / Two Pointers
- Result: Solved
- Link: https://leetcode.com/problems/3sum/

## Problem Summary

Given an integer array `nums`, return all unique triplets:

```python
[nums[i], nums[j], nums[k]]
```

such that:

```text
i != j != k
nums[i] + nums[j] + nums[k] == 0
```

The answer must not contain duplicate triplets.

## Core Idea

Sort the array, then fix one number and reduce the remaining problem to Two Sum
II on the right side of the array.

For each index `i`:

```text
fixed = nums[i]
need two numbers after i that sum to -fixed
```

Because the remaining subarray is sorted, use opposite-end two pointers.

## Key Realization

Brute force checks every triplet:

```text
O(n^3)
```

Sorting creates directional information:

- if the triplet sum is too small, move `left` right
- if the triplet sum is too large, move `right` left
- if the triplet sum is zero, record it and skip duplicates

This turns the inner search into linear two-pointer work.

## Duplicate Skipping

Duplicates are the main implementation detail.

Skip duplicate fixed values:

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

After finding a valid triplet, move both pointers, then skip repeated pointer
values:

```python
left += 1
right -= 1

while left < right and nums[left] == nums[left - 1]:
    left += 1

while left < right and nums[right] == nums[right + 1]:
    right -= 1
```

This prevents repeated triplets in the answer.

## Pointer Logic

```python
nums.sort()
result = []

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
```

## Why This Works

Once `nums[i]` is fixed, the remaining task is:

```text
find two values in a sorted subarray that sum to -nums[i]
```

That is the same directional movement as Two Sum II.

Sorting also groups duplicate values together, which makes duplicate skipping
local and deterministic.

## Pitfalls

- Forgetting to skip duplicate `i` values.
- Forgetting to skip duplicate pointer values after recording a valid triplet.
- Starting `left` at `0` instead of `i + 1`.
- Returning duplicate triplets.
- Trying brute force and timing out.

## Final Solution

```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

## Complexity

- Time: `O(n^2)`
- Space: `O(1)` extra space, or `O(n)` depending on sorting implementation

Sorting costs `O(n log n)`, then each fixed `i` runs a linear two-pointer scan,
so the total is dominated by `O(n^2)`.

## Interview Trigger

If you see:

- triplet sum
- unique combinations
- pair search inside a larger sum problem
- duplicate avoidance

Think:

```text
sort, fix one number, run Two Sum II on the remaining subarray
```

## Retention Card

- Problem: 15. 3Sum
- Difficulty: Medium
- Time Spent: ___
- Pattern: sorting + two pointers
- Trigger: triplet sum problem
- Core Insight: fix one number, reduce remainder to Two Sum II
- Template: sort, iterate `i`, two-pointer search on remaining subarray
- Complexities: `O(n^2)` time, `O(1)`/`O(n)` space depending on sorting

Process:

- Brute force is `O(n^3)`.
- Sorting enables directional pointer movement.
- Duplicate skipping avoids repeated triplets.

Mistakes:

- Skip duplicate `i` values.
- After finding valid triplet, skip duplicate pointer values.
