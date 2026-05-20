# LeetCode 1: Two Sum

## Metadata

- Difficulty: Easy
- Topic: Arrays & Hashing / Hash Map Lookup
- Time:
- Result: Solved
- Link: https://leetcode.com/problems/two-sum/

## Retention Card

- Pattern: hashmap lookup
- Trigger: need complement quickly
- Core Insight: for each `x`, check if `target - x` was already seen
- Template: `value -> index` map
- Complexity: `O(n)` time, `O(n)` space

Process:

- brute force checks every pair
- bottleneck is searching for complement
- hashmap makes complement lookup `O(1)`

Mistake to watch:

- check complement before inserting current value

## Problem Summary

Given an array `nums` and an integer `target`, return the indices of two numbers
that add up to `target`.

Each input has exactly one solution, and the same element cannot be used twice.

## Core Idea

Instead of checking every pair, use the target to determine the exact number
needed.

For each number `num`, compute:

```python
need = target - num
```

If `need` has already appeared, return:

```python
[index_of_need, current_index]
```

## Key Realization

The hash map should store:

```text
value -> index
```

not:

```text
needed_value -> index
```

because when checking:

```python
if need in seen:
```

`seen` must contain actual previous values.

## Important Invariant

Check for the complement before inserting the current number.

This avoids using the same index twice.

Example:

```python
nums = [3, 2, 4]
target = 6
```

At index `0`, `num = 3`.

If we inserted `3` first, then checked for `need = 3`, we could accidentally use
the same index twice.

The safe order is:

1. compute complement
2. check whether complement was previously seen
3. insert current value

## Breakthroughs

- Replaced nested pair checking with complement lookup.
- Stored previous values as keys and their indices as values.
- Checked the complement before inserting the current number.
- Used left-to-right traversal so every map entry represents an earlier index.

## Pitfalls

- Storing needed values instead of actual seen values.
- Inserting before checking and reusing the same index.
- Returning values instead of indices.
- Forgetting duplicate values can exist, so indices matter.

## Final Solution

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Mental Model

Each number asks:

```text
Have I already seen the exact value that would complete the target?
```

The hash map is memory of previous values and where they appeared.

## Interview Phrasing

I loop left to right and store previously seen values with their indices. For
each number, I compute the complement needed to reach the target. If that
complement has already been seen, I return both indices. Otherwise, I store the
current value and continue.

## Interview Trigger

If you see:

- pair sum
- target value
- return indices
- need better than `O(n^2)`

Think:

```text
hash map from value to index + complement lookup
```
