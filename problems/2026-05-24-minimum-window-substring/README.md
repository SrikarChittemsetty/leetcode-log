# LeetCode 76: Minimum Window Substring

## Metadata

- Difficulty: Hard
- Topic: Sliding Window / Hash Maps
- Result: Solved
- Link: https://leetcode.com/problems/minimum-window-substring/

## Problem Summary

Given strings `s` and `t`, return the smallest substring of `s` that contains
all characters from `t`, including duplicate counts.

## Core Idea

Use a variable sliding window.

Expand right until the window contains everything needed. Once valid, shrink
left as much as possible while preserving validity.

## Key Realization

Validity is based on satisfied character counts, not raw length.

For each required character, the window must have at least the needed count.

Track:

- `need`: required character frequencies
- `window`: current window frequencies
- `have`: how many required characters are currently satisfied
- `required`: how many distinct required characters must be satisfied

## Final Solution

```python
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have = 0
        required = len(need)
        left = 0
        best = float("inf")
        best_range = (0, 0)

        for right, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < best:
                    best = right - left + 1
                    best_range = (left, right)

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best == float("inf"):
            return ""

        start, end = best_range
        return s[start : end + 1]
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Retention Card

- Problem: 76. Minimum Window Substring
- Difficulty: Hard
- Time Spent: ___
- Pattern: variable sliding window
- Trigger: smallest valid covering substring
- Core Insight: expand until valid, shrink while preserving validity
- Template: need/have hashmap tracking
- Complexities: `O(n)` time, `O(n)` space

Process:

- Brute force checks all substrings.
- Right pointer acquires needed chars.
- Left pointer minimizes valid window.

Mistakes:

- Validity based on satisfied character counts, not raw length.
