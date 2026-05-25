# LeetCode 424: Longest Repeating Character Replacement

## Metadata

- Difficulty: Medium
- Topic: Sliding Window / Frequency Counting
- Result: Solved
- Link: https://leetcode.com/problems/longest-repeating-character-replacement/

## Problem Summary

Given a string `s` and integer `k`, return the length of the longest substring
that can be turned into all one repeated character using at most `k`
replacements.

## Core Idea

Use a variable sliding window with character frequencies.

Inside a window, the best character to keep is the most frequent character. All
other characters would need replacement.

So the number of replacements needed is:

```python
window_size - max_frequency
```

The window is invalid when:

```python
window_size - max_frequency > k
```

## Key Realization

The most frequent character anchors the window.

If a window has length `10` and its most frequent character appears `7` times,
then `3` characters must be replaced.

If `3 <= k`, the window is valid.

## Stale `maxFreq` Insight

`maxFreq` may stay stale when the left pointer moves, and this still works.

Why?

`maxFreq` is used to decide whether the current window is too large. A stale
larger value may delay shrinking, but it never causes the algorithm to miss the
true maximum length. It represents the best frequency seen for a window size we
were able to reach.

## Final Solution

```python
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxFreq = 0
        best = 0

        for right, char in enumerate(s):
            count[char] += 1
            maxFreq = max(maxFreq, count[char])

            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
```

## Complexity

- Time: `O(n)`
- Space: `O(1)` for uppercase English letters

## Retention Card

- Problem: 424. Longest Repeating Character Replacement
- Difficulty: Medium
- Time Spent: ___
- Pattern: variable sliding window
- Trigger: longest window with limited modifications
- Core Insight: invalid when `window_size - max_frequency > k`
- Template: frequency map + dynamic window
- Complexities: `O(n)` time, `O(1)` space

Process:

- Most frequent char anchors the window.
- All other chars would need replacement.
- Shrink only when replacements exceed `k`.

Mistakes:

- `maxFreq` may stay stale and still works.
