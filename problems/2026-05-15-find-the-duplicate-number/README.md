# LeetCode 287: Find the Duplicate Number

## Metadata

- Difficulty: Medium
- Topic: Floyd's Cycle Detection / Array as Linked List
- Time:
- Result: Solved after recognizing the array-as-linked-list abstraction
- Link: https://leetcode.com/problems/find-the-duplicate-number/

## Problem Summary

We are given an array `nums` containing `n + 1` integers.

Each value is in the range:

```text
1 through n
```

There is exactly one repeated number, and we must return that duplicate.

The constraints matter:

- do not modify the array
- use only `O(1)` extra space

## Key Insight

Instead of treating the array normally, reinterpret it as a linked structure:

- indices are nodes
- values are pointers to the next node

The relationship is:

```text
i -> nums[i]
```

Since there are `n + 1` indices but only values from `1` through `n`, some value
must be pointed to more than once.

That duplicate pointer creates a cycle.

## Why This Is A Cycle Problem

Example:

```python
nums = [1, 3, 4, 2, 2]
```

Think of each index as pointing to the next index:

```text
0 -> nums[0] = 1
1 -> nums[1] = 3
3 -> nums[3] = 2
2 -> nums[2] = 4
4 -> nums[4] = 2
```

The path becomes:

```text
0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> ...
```

The cycle entrance is `2`, which is the duplicate number.

## Phase 1: Find An Intersection

Use Floyd's slow and fast pointers to detect an intersection inside the cycle.

- `slow` moves one step
- `fast` moves two steps

Transition:

```python
slow = nums[slow]
fast = nums[nums[fast]]
```

Eventually they must meet if a cycle exists.

## Phase 2: Find The Cycle Entrance

Create a second pointer starting at index `0`.

Move both pointers one step at a time:

```python
slow = nums[slow]
slow2 = nums[slow2]
```

The position where they meet is the cycle entrance.

That entrance corresponds to the duplicate number.

## Important Realization

This problem initially looks like a duplicate-searching array problem, but the
constraints force a completely different abstraction:

- cannot use a hash set because of the `O(1)` space requirement
- cannot sort in-place because the array cannot be modified

The intended leap is recognizing that the value range allows the array to be
modeled as a linked structure.

## Breakthroughs

- Reframed values as pointers instead of data to count.
- Connected the pigeonhole principle to cycle formation.
- Used Floyd's algorithm to satisfy both constraints: no mutation and constant space.
- Understood that the cycle entrance, not just any meeting point, is the duplicate.

## Pitfalls

- Treating the first slow/fast meeting point as the answer.
- Using a set despite the constant-space constraint.
- Sorting the array even though the input must not be modified.
- Forgetting that `nums[nums[fast]]` is the two-step move.

## Final Solution

```python
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Mental Model

Think of the array as a linked list encoded by indices and values.

The duplicate number is not found by scanning for equal values directly. It is
found by locating where the pointer chain loops back into itself.

## Interview Trigger

If you see:

- duplicate number
- values constrained to `1..n`
- array length `n + 1`
- cannot modify array
- `O(1)` extra space required

Think:

```text
Floyd's cycle detection with array values as next pointers
```
