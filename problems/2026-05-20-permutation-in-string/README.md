# LeetCode 567: Permutation in String

## Metadata

- Difficulty: Medium
- Topic: Sliding Window / Frequency Counting
- Result: Solved
- Link: https://leetcode.com/problems/permutation-in-string/

## Problem Summary

Given two strings `s1` and `s2`, return whether `s2` contains a permutation of
`s1`.

In other words, some substring of `s2` must be an anagram of `s1`.

## Core Idea

Use a fixed-size sliding window.

Every permutation of `s1` has:

- the same length as `s1`
- the same character frequencies as `s1`

So we slide a window of size `len(s1)` across `s2` and check whether the window's
frequency counts match `s1`'s frequency counts.

## Pattern Recognition

A permutation must:

- contain the exact same characters
- contain them with the exact same frequencies
- have the exact same length as `s1`

That immediately signals:

```text
fixed-size sliding window
```

## Brute Force Progression

### Naive

Generate every permutation of `s1` and check whether it exists in `s2`.

This is too expensive:

```text
O(n!)
```

### Better Brute Force

Check every substring of `s2` with length `len(s1)`:

- build a frequency map
- compare it against `s1`'s frequency map

This is still inefficient because the frequency map is rebuilt repeatedly.

## Optimization Insight

Instead of rebuilding a frequency map for every window:

- maintain one running frequency map for the current window
- when the window slides:
  - add the new right character
  - remove the old left character

This converts repeated recomputation into incremental updates.

## Fixed Vs Dynamic Sliding Window

### Fixed Window

- window size predetermined
- maintain size
- add right
- remove left

### Dynamic Window

- expand right greedily
- shrink left until valid again

This problem is fixed-size because:

```python
len(window) == len(s1)
```

## Key Realization

A valid window is not about character order.

It is about exact frequency equality:

```text
window_count == need_count
```

This is the same anagram idea, but applied to every fixed-size substring of
`s2`.

## Sliding Window Update

Instead of recounting each substring from scratch:

1. Add the new right character.
2. If the window is too large, remove the left character.
3. When the window size equals `len(s1)`, compare frequency maps.

This keeps the window moving in `O(n)` time.

## Pointer Logic

```python
need = Counter(s1)
window = Counter()
left = 0

for right in range(len(s2)):
    window[s2[right]] += 1

    if right - left + 1 > len(s1):
        window[s2[left]] -= 1

        if window[s2[left]] == 0:
            del window[s2[left]]

        left += 1

    if right - left + 1 == len(s1) and window == need:
        return True
```

## Important Window-Size Detail

Maintain the exact window size.

If the window is larger than `len(s1)`, it cannot represent a permutation of
`s1`.

The remove-left step keeps the comparison meaningful.

## Why This Works

Each window represents one candidate substring of length `len(s1)`.

If its frequency map matches `s1`'s frequency map, that substring is a
permutation.

If no fixed-size window matches, no permutation exists in `s2`.

## Pitfalls

- Letting the window grow beyond `len(s1)`.
- Recounting every substring from scratch.
- Comparing sorted substrings repeatedly.
- Forgetting to remove zero-count keys before comparing maps.
- Treating order as important when only frequency matters.

## Final Solution

```python
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()
        left = 0

        for right in range(len(s2)):
            window[s2[right]] += 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if right - left + 1 == len(s1) and window == need:
                return True

        return False
```

## Complexity

- Time: `O(n)`
- Space: `O(1)` for a fixed lowercase alphabet

More generally, space is `O(k)`, where `k` is the number of distinct characters
being tracked.

## Interview Trigger

If you see:

- permutation inside a string
- anagram substring
- fixed target length
- exact frequency match

Think:

```text
fixed-size sliding window + frequency counts
```

## Retention Card

- Problem: 567. Permutation in String
- Difficulty: Medium
- Time Spent: ___
- Pattern: fixed-size sliding window
- Trigger: substring permutation/anagram detection
- Core Insight: valid window must match frequency counts exactly
- Template: frequency maps + window size `len(s1)`
- Complexities: `O(n)` time, `O(1)` space fixed alphabet

Process:

- Every valid permutation has same character frequencies.
- Sliding window avoids recounting entire substring.
- Add right char, remove left char each step.

Mistakes:

- Maintain exact window size.
