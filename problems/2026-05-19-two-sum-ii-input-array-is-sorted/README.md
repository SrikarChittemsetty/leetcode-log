# LeetCode 167: Two Sum II - Input Array Is Sorted

## Metadata

- Difficulty: Medium
- Topic: Two Pointers / Sorted Array
- Result: Solved
- Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Problem Summary

Given a sorted array `numbers` and a target value, return the indices of the
two numbers that add up to `target`.

Important detail:

```text
The returned indices are 1-indexed.
```

## Core Idea

Use opposite-end two pointers.

Because the array is sorted:

- moving the left pointer right increases the sum
- moving the right pointer left decreases the sum

This gives directional information that the unsorted Two Sum problem does not
have.

## Key Realization

A hash map would still work, but it ignores the sorted property and uses extra
space.

Sorted order lets each pointer move eliminate a whole set of impossible pairs.

For a current pair:

```python
current = numbers[left] + numbers[right]
```

If `current` is too small:

```text
numbers[left] is too small to pair with this right value
```

So move `left` rightward.

If `current` is too large:

```text
numbers[right] is too large to pair with this left value
```

So move `right` leftward.

## Pointer Logic

```python
left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        return [left + 1, right + 1]

    if total < target:
        left += 1
    else:
        right -= 1
```

The `+ 1` converts zero-indexed Python positions into the problem's 1-indexed
answer.

## Why This Works

Each move is justified by sorted order.

When the sum is too small, keeping the same `left` cannot work with any smaller
right-side value, so `left` must increase.

When the sum is too large, keeping the same `right` cannot work with any larger
left-side value, so `right` must decrease.

That means each pointer move discards impossible pairs safely.

## Pitfalls

- Returning zero-indexed positions.
- Using a hash map and missing the sorted-array optimization.
- Moving both pointers when the sum is only too small or too large.
- Forgetting that the array is already sorted.

## Final Solution

```python
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            if total < target:
                left += 1
            else:
                right -= 1

        return []
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Each pointer only moves inward, so the array is scanned at most once.

## Interview Trigger

If you see:

- sorted array
- pair sum target
- return two indices
- need better than hash-map space

Think:

```text
opposite-end two pointers
```

## Retention Card

- Problem: 167. Two Sum II - Input Array Is Sorted
- Difficulty: Medium
- Time Spent: ___
- Pattern: opposite-end two pointers
- Trigger: sorted array + pair sum target
- Core Insight: sorted order lets pointer movement eliminate possibilities
- Template: if sum too small -> `l++`, too large -> `r--`
- Complexities: `O(n)` time, `O(1)` space

Process:

- Hashmap works but ignores sorted property.
- Sortedness gives directional information.
- Each move eliminates impossible pairs.

Mistakes:

- Remember indices are 1-indexed.
