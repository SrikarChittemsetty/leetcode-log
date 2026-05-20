# LeetCode 42: Trapping Rain Water

## Metadata

- Difficulty: Hard
- Topic: Two Pointers / Running Maximums
- Result: Solved
- Link: https://leetcode.com/problems/trapping-rain-water/

## Problem Summary

Given an array `height`, each value represents the height of a bar.

Return how much rain water can be trapped after raining.

At any index, trapped water depends on the tallest boundary to the left and the
tallest boundary to the right:

```python
water_at_i = min(leftMax, rightMax) - height[i]
```

Only positive values contribute water.

## Core Idea

Use two pointers with running maximums.

The brute force version recomputes:

- maximum height to the left
- maximum height to the right

for every index.

Instead, maintain those maximums while shrinking inward from both ends.

## Key Realization

Water is limited by the smaller side maximum.

If:

```python
leftMax < rightMax
```

then the left side is the limiting boundary.

That means the amount of water at `left` can be finalized using `leftMax`,
because the right side already has a boundary at least as tall.

Similarly, if `rightMax <= leftMax`, the right side can be finalized.

## Pointer Logic

Initialize:

```python
left = 0
right = len(height) - 1
leftMax = 0
rightMax = 0
water = 0
```

Then:

```python
while left < right:
    if height[left] < height[right]:
        leftMax = max(leftMax, height[left])
        water += leftMax - height[left]
        left += 1
    else:
        rightMax = max(rightMax, height[right])
        water += rightMax - height[right]
        right -= 1
```

## Important Implementation Detail

Update the running max before calculating trapped water.

This keeps the subtraction non-negative:

```python
leftMax = max(leftMax, height[left])
water += leftMax - height[left]
```

If the current bar becomes the new maximum, it traps `0` water.

## Why This Works

At each step, process the side with the smaller current boundary.

That smaller side determines the maximum possible water level for that index.

The opposite side has enough height to act as a boundary, so the current side's
water amount is final and does not need to be revisited.

## Pitfalls

- Forgetting to update the max before calculating trapped water.
- Using brute force repeated left/right max scans.
- Confusing this with Container With Most Water.
- Moving pointers without maintaining `leftMax` and `rightMax`.
- Calculating water from raw pointer heights instead of running maximums.

## Final Solution

```python
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
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Each pointer moves inward at most once per index.

## Interview Trigger

If you see:

- trapped water
- bars/elevation map
- depends on tallest left and right boundaries
- repeated max-left/max-right work

Think:

```text
two pointers with running maximums
```

## Retention Card

- Problem: 42. Trapping Rain Water
- Difficulty: Hard
- Time Spent: ___
- Pattern: two pointers with running maximums
- Trigger: water trapped depends on tallest boundaries
- Core Insight: trapped water at index determined by smaller side max
- Template: maintain `leftMax`/`rightMax` while shrinking inward
- Complexities: `O(n)` time, `O(1)` space

Process:

- Brute force recomputes max left/right repeatedly.
- Water limited by `min(leftMax, rightMax)`.
- Whichever side has smaller max can be finalized safely.

Mistakes:

- Update max before calculating trapped water.
