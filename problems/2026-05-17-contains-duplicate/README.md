# LeetCode 217: Contains Duplicate

## Metadata

- Difficulty: Easy
- Topic: Arrays & Hashing / Hash Set Membership
- Time:
- Result: Solved
- Link: https://leetcode.com/problems/contains-duplicate/

## Retention Card

- Pattern: seen set
- Trigger: need to know if a value appeared before
- Core Insight: a set gives `O(1)` average membership checks
- Template: iterate `nums`; if `x in seen`, return `True`; otherwise add `x`
- Complexity: `O(n)` time, `O(n)` space

Process:

- brute force would compare every pair
- bottleneck is repeated searching
- set removes repeated search

Mistake to watch:

- check before adding; adding first can hide the "previously seen" invariant

## Problem Summary

Given an integer array `nums`, return `True` if any value appears at least twice.

Return `False` if every value is distinct.

## Core Idea

The brute force approach compares every element with every other element.

That is unnecessary because we only care whether a value has appeared before.

Instead of repeatedly scanning the array, maintain a set of previously seen
values.

For each number:

- if it is already in `seen`, duplicate found, return `True`
- otherwise add it to `seen`

If iteration finishes, all values were distinct.

## Key Realization

Transform the problem from:

```text
Does this number appear later?
```

into:

```text
Have I already seen this number before?
```

This converts repeated scanning into constant-time membership checks using a
hash set.

## Important Invariant

`seen` contains every value encountered before the current index.

Thus:

- `num in seen` implies a duplicate exists
- otherwise, it is safe to add the current value

## Breakthroughs

- Started from nested-loop brute force.
- Recognized repeated scanning inefficiency.
- Reframed the question into "seen before?"
- Identified hash set as ideal because indices are unnecessary.

## Pitfalls

- Using a hash map when only existence matters.
- Waiting until after the loop to compare lengths without explaining the tradeoff.
- Forgetting to return `False` after scanning all values.

## Final Solution

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

## Complexity

- Time: `O(n)`
- Space: `O(n)` worst case if all values are distinct

## Mental Model

The set is memory of everything already passed.

Each new number asks:

```text
Have I appeared earlier in the scan?
```

## Useful Distinction From Two Sum

Two Sum requires a hash map:

```text
value -> index
```

because the answer must return indices.

Contains Duplicate only requires a hash set because existence alone matters.

## Interview Trigger

If you see:

- duplicate detection
- no need for indices
- repeated membership checks

Think:

```text
hash set of seen values
```
