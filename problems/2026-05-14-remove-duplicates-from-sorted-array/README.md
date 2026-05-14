# LeetCode 26: Remove Duplicates from Sorted Array

## Metadata

- Difficulty: Easy
- Topic: Two Pointers / In-Place Array Manipulation
- Time: ~15 minutes
- Result: Solved after recognizing sorted-order optimization
- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Problem Summary

We are given a sorted array:

```python
nums
```

We must:

- remove duplicates in-place
- keep only unique values at the front of the array
- return the number of unique elements `k`

Everything beyond index:

```text
k - 1
```

can be ignored.

## Initial Observation

A naive instinct is to use:

```python
set(nums)
```

because sets naturally remove duplicates.

However, this fails for two reasons.

### 1. The problem requires in-place modification

The original array itself must be rewritten.

Creating:

```python
unique = set(nums)
```

creates a new structure instead of modifying `nums`.

### 2. Sets do not preserve ordering guarantees

The problem explicitly requires:

- relative ordering preserved
- unique values packed at the front

So a direct set conversion is not the intended solution.

## Key Insight

The array is already sorted.

This means:

```text
duplicates always appear next to each other
```

Example:

```python
[0, 0, 1, 1, 1, 2, 2, 3]
```

Because duplicates are adjacent, we do not need:

- a hash set
- global duplicate tracking
- nested loops

We only need to compare each element with the previous one.

## Two Pointer Strategy

### `i`

Scans through the array.

### `left`

Tracks:

```text
where the next unique value should be written
```

The front of the array gradually becomes compressed into:

```text
[unique unique unique ...]
```

## Core Logic

Whenever:

```python
nums[i] != nums[i - 1]
```

we found a new unique value.

So:

1. write it into the next unique slot
2. advance `left`

## Walkthrough

Input:

```python
[0, 0, 1, 1, 2]
```

Initial:

```python
left = 1
```

At `i = 1`:

```text
0 == 0
```

Duplicate, so ignore it.

At `i = 2`:

```text
1 != 0
```

New unique value:

```python
nums[left] = 1
left += 1
```

Array becomes:

```python
[0, 1, 1, 1, 2]
```

At `i = 4`:

```text
2 != 1
```

Write:

```python
nums[2] = 2
```

Final useful portion:

```python
[0, 1, 2]
```

Return:

```python
3
```

## Breakthroughs

- Rejected the `set` shortcut because the problem requires in-place ordered output.
- Used the sorted property to avoid extra memory.
- Recognized that adjacent comparison is enough to identify new unique values.
- Separated scanning (`i`) from writing (`left`).

## Pitfalls

- Forgetting that only the first `k` elements matter after returning.
- Starting `left` at `0`, which would overwrite the first valid value unnecessarily.
- Using extra memory even though sorted adjacency gives all needed information.
- Comparing against `nums[left]` after writes instead of the original previous scanned value.

## Final Solution

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1

        return left
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Mental Model

Think of the array as being compressed in-place.

`i` explores the original array.

`left` builds the compacted unique section at the front.

The sorted ordering removes the need for extra memory because duplicates can
only appear adjacent to each other.

## Interview Trigger

If you see:

- sorted array
- remove duplicates
- in-place modification

Think:

```text
two pointers + overwrite unique values forward
```
