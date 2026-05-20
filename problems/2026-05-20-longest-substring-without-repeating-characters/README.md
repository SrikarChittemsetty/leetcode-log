# LeetCode 3: Longest Substring Without Repeating Characters

## Metadata

- Difficulty: Medium
- Topic: Sliding Window / Hash Set
- Result: Solved
- Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem Summary

Given a string `s`, return the length of the longest substring without
repeating characters.

Important distinction:

```text
substring means contiguous
```

So the window must represent a continuous section of the string.

## Core Idea

Use a variable-size sliding window.

The window should always contain unique characters.

Expand the right pointer to include new characters. If adding a character makes
the window invalid, shrink from the left until the duplicate is gone.

## Key Realization

Brute force checks every substring:

```text
O(n^2) or worse
```

But duplicates define the invalid condition.

So instead of rebuilding/checking every substring, maintain a live window and a
set of characters currently inside it.

## Window Invariant

The set `seen` contains exactly the characters inside:

```python
s[left : right + 1]
```

After the duplicate-removal loop finishes, the window is valid again.

Then update the best length:

```python
best = max(best, right - left + 1)
```

## Why Shrink With `while`

Use a `while` loop, not a single `if`.

A duplicate may require removing multiple characters before the window becomes
valid again.

Example:

```python
s = "abba"
```

When the second `"b"` appears, the left pointer must remove `"a"` and the first
`"b"` before the window is valid.

## Pointer Logic

```python
left = 0
seen = set()
best = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    best = max(best, right - left + 1)
```

## Why This Works

The right pointer explores new characters.

The left pointer removes exactly enough old characters to restore the no-repeat
condition.

Because each character is added once and removed at most once, the total work is
linear.

## Pitfalls

- Shrinking with `if` instead of `while`.
- Forgetting that the substring must be contiguous.
- Updating the best length before restoring validity.
- Not removing characters from the set as `left` moves.

## Final Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        best = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            best = max(best, right - left + 1)

        return best
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`

Each character enters and leaves the sliding window at most once.

## Interview Trigger

If you see:

- longest substring/subarray
- validity changes as the window grows
- no duplicates allowed
- contiguous region

Think:

```text
variable sliding window with set/map
```

## Retention Card

- Problem: 3. Longest Substring Without Repeating Characters
- Difficulty: Medium
- Time Spent: ___
- Pattern: variable sliding window
- Trigger: longest valid subarray/substring without duplicates
- Core Insight: expand right until invalid, shrink left until valid
- Template: set/map + dynamic window
- Complexities: `O(n)` time, `O(n)` space

Process:

- Brute force checks every substring.
- Duplicates define invalid condition.
- Left pointer removes invalidity incrementally.

Mistakes:

- Shrink in `while` loop, not `if` statement.
