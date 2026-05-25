# LeetCode 239: Sliding Window Maximum

## Metadata

- Difficulty: Hard
- Topic: Monotonic Deque / Sliding Window
- Result: Solved
- Link: https://leetcode.com/problems/sliding-window-maximum/

## Problem Summary

Given an array `nums` and window size `k`, return the maximum value in each
contiguous sliding window of size `k`.

Example:

```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

output = [3, 3, 5, 5, 6, 7]
```

## Pattern Recognition

This is a fixed-size sliding window problem because:

```text
window size == k
```

The size never changes.

The challenge is not identifying the window boundaries. The challenge is
efficiently maintaining the maximum as the window slides.

## Brute Force

For every window:

1. Scan all `k` elements.
2. Compute the maximum.
3. Append the result.

Example:

```text
[1, 3, -1] -> 3
[3, -1, -3] -> 3
[-1, -3, 5] -> 5
```

Complexity:

```text
O(n * k)
```

because every window recomputes the max from scratch.

## Optimization Insight

When the window slides:

- one value enters
- one value leaves

Recomputing the maximum from scratch wastes work.

The real problem is:

```text
if the current max leaves the window, we need the next best candidate instantly
```

This motivates a data structure that:

- keeps the current max accessible
- removes permanently useless values

## Core Idea

Use a monotonic decreasing deque storing indices.

The deque stores candidate maximums where values decrease from front to back.

That means:

```text
front always contains the current maximum candidate
```

## Why Store Indices?

The deque stores indices, not raw values.

Why?

We need both:

- the value: `nums[dq[0]]`
- the position: to know when an element leaves the window

Without indices, we could not reliably remove expired elements.

## Key Realization

The front of the deque always stores the index of the current max.

Before reading the max:

- remove indices that fell out of the window from the front
- remove smaller values from the back

Store indices, not values, so window membership can be checked.

## Critical Greedy Observation

Suppose a smaller value appears before a larger value:

```text
..., 1, ..., 3
```

If `3` appears to the right of `1`, then `1` can never become the maximum again
while `3` remains in the window.

Why?

- windows only move right
- `1` will expire before `3`
- `3` is larger anyway

Therefore, `1` is permanently useless and can be removed forever.

This is the core monotonic-deque insight.

## Deque Rules

### Rule 1: Remove Smaller Values From Back

While:

```python
nums[dq[-1]] < nums[right]
```

remove from the back.

Those smaller values can never become max again.

### Rule 2: Remove Expired Indices From Front

If:

```python
dq[0] <= right - k
```

then the front index has left the window and must be removed.

### Rule 3: Front Always Stores Maximum

After cleanup:

```python
nums[dq[0]]
```

is the maximum for the current window.

## Algorithm

For each `right` index:

1. Remove smaller values from the back.
2. Add the current index.
3. Remove expired indices from the front.
4. Once the first full window forms, append `nums[dq[0]]`.

## Final Solution

```python
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
```

## Complexity

- Time: `O(n)`
- Space: `O(k)`

Each index is added and removed at most once.

## Key Takeaways

### Fixed Sliding Window

- window size is constant
- add right
- remove left/expired values

### Monotonic Queue Pattern

Maintain ordered candidates and discard permanently useless values.

Important:

```text
The deque does not represent the entire window.
```

It only stores surviving candidates that could still become, or currently are,
the maximum.

## Mental Model

Deque front:

```text
largest surviving candidate
```

Deque back:

```text
smallest still-useful candidate
```

Anything smaller than a newly arriving larger value becomes permanently
irrelevant and is greedily discarded.

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
