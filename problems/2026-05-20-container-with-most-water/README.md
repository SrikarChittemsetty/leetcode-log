# LeetCode 11: Container With Most Water

## Metadata

- Difficulty: Medium
- Topic: Two Pointers / Greedy Boundary Movement
- Result: Solved
- Link: https://leetcode.com/problems/container-with-most-water/

## Problem Summary

Given an array `height`, choose two vertical lines that form a container with
the x-axis.

Return the maximum amount of water the container can hold.

For two pointers `left` and `right`, the area is:

```python
area = (right - left) * min(height[left], height[right])
```

## Core Idea

Use opposite-end two pointers.

Start with the widest possible container:

```python
left = 0
right = len(height) - 1
```

Then repeatedly compute the current area and move one pointer inward.

## Key Realization

The smaller wall limits the current container.

If:

```python
height[left] < height[right]
```

then the left wall is the bottleneck.

Keeping the same smaller wall while moving the taller wall inward cannot improve
the area, because:

- width gets smaller
- height is still limited by the same smaller wall

So the only move that can possibly help is moving the smaller wall inward and
hoping to find a taller one.

## Pointer Logic

```python
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
```

## Why This Works

Each step keeps the only pointer movement that could improve the bottleneck.

The larger wall is not limiting the current area. Moving it inward only reduces
width without addressing the limiting height.

Moving the smaller wall sacrifices width, but creates the possibility of a
taller limiting wall.

## Pitfalls

- Forgetting that width is `right - left`.
- Moving the taller wall instead of the smaller wall.
- Trying every pair with brute force.
- Comparing only heights instead of area.

## Final Solution

```python
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
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Each pointer moves inward at most `n` times total.

## Interview Trigger

If you see:

- maximize area
- two boundaries
- width between indices
- limiting smaller height

Think:

```text
opposite-end two pointers, move the smaller wall
```

## Retention Card

- Problem: 11. Container With Most Water
- Difficulty: Medium
- Time Spent: ___
- Pattern: opposite-end two pointers
- Trigger: maximize area using two boundaries
- Core Insight: smaller wall limits area, so only moving smaller wall can help
- Template: compute area, move smaller pointer inward
- Complexities: `O(n)` time, `O(1)` space

Process:

- Brute force checks all pairs.
- Area determined by `min(height[l], height[r])`.
- Larger wall is not current bottleneck.

Mistakes:

- Width is `r - l`.
