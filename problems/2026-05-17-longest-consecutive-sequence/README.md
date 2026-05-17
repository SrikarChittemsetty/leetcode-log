# LeetCode 128: Longest Consecutive Sequence

## Metadata

- Difficulty: Medium
- Topic: Arrays & Hashing / Set Membership / Sequence Starts
- Result: Solved
- Link: https://leetcode.com/problems/longest-consecutive-sequence/

## Problem Summary

Given an unsorted integer array `nums`, return the length of the longest
consecutive sequence.

Important realization:

```text
the sequence does not need to appear consecutively in the array itself
only the values matter
```

Example:

```python
[100, 4, 200, 1, 3, 2]
```

contains the consecutive run:

```text
1, 2, 3, 4
```

despite the values being scattered.

## Initial Understanding

Defined consecutive sequence as:

```text
each next value is exactly 1 greater than the previous value
```

Goal:

```text
find the longest such run
```

## Brute Force Thought Process

Initial instinct:

- attempt to start a run from every number
- repeatedly check:
  - `num + 1`
  - `num + 2`
  - and so on

Naively, if membership checking required scanning the list, runtime becomes too
expensive.

This motivates fast existence checking.

## Key Data Structure Insight

Use a hash set:

```python
elements = set(nums)
```

Major realization:

- converting to a set costs `O(n)`
- but enables average `O(1)` membership checks

This is what makes the linear-time solution possible.

## Critical Conceptual Correction

Initially drifted toward thinking in terms of:

```text
adjacent positions in the array
```

Key correction:

```text
input order is irrelevant
```

The sequence is determined purely by value existence in the set.

This was the major conceptual unlock.

## Avoiding Recounting

Important optimization insight:

If we expand sequences from every number, runs get recounted repeatedly.

Example:

```text
1, 2, 3, 4
```

would be expanded:

- from `1`
- from `2`
- from `3`
- from `4`

That is wasteful.

## Start-Of-Sequence Insight

A number is only the start of a sequence if:

```python
num - 1 not in elements
```

Meaning:

```text
no smaller consecutive predecessor exists
```

So:

- `1` starts the run
- `2`, `3`, and `4` do not

This ensures every sequence is expanded exactly once.

## Sequence Expansion

Once a valid start is found:

```python
length = 1
```

Then repeatedly check:

```python
num + length
```

If it exists:

- extend the streak
- increment `length`

Update the global maximum afterward.

## Complexity Insight

At first glance:

```text
nested while loop appears expensive
```

Key realization:

Even though expansion happens inside a loop, each number participates in
sequence expansion only once overall.

Why?

```text
Only sequence starts trigger expansion.
```

Thus total work remains linear.

## Breakthroughs

- Recognized that array order does not matter.
- Used a set for `O(1)` average existence checks.
- Identified duplicate expansion as the real inefficiency.
- Derived the start-of-sequence condition.
- Understood why the nested loop is still linear overall.

## Pitfalls

- Treating neighboring array positions as meaningful.
- Starting expansion from every number.
- Sorting even though the target is `O(n)`.
- Misreading the nested loop as automatically `O(n^2)`.

## Final Solution

```python
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for num in elements:
            if num - 1 not in elements:
                length = 1

                while num + length in elements:
                    length += 1

                longest = max(longest, length)

        return longest
```

## Complexity Analysis

Let:

```text
n = number of elements
```

### Time Complexity

`O(n)`

Reasoning:

- set construction -> `O(n)`
- each sequence is expanded once overall
- each number is effectively processed a constant number of times

### Space Complexity

`O(n)`

for the hash set.

## Key Takeaways

Patterns reinforced:

- hashing for fast existence lookup
- avoiding repeated work
- recognizing start conditions

Major conceptual lesson:

```text
The optimization came not from making expansion faster, but from preventing duplicate expansion entirely.
```

## Important Mental Shift

Transitioned from:

```text
thinking about neighboring array positions
```

to:

```text
thinking about value existence globally
```

This is the core abstraction behind the solution.

## Interview Notes

Strong reasoning progression:

- identified brute-force sequence expansion
- recognized need for fast membership checking
- introduced hash set
- identified duplicate work issue
- derived start-of-sequence condition independently
- understood why nested loop still remains linear

## Interview Trigger

If you see:

- unsorted array
- consecutive values
- order in input does not matter
- need `O(n)`

Think:

```text
hash set + only expand from sequence starts
```
