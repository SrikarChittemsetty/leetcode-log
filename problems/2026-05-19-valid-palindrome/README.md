# LeetCode 125: Valid Palindrome

## Metadata

- Difficulty: Easy
- Topic: Two Pointers / String Filtering
- Result: Solved
- Link: https://leetcode.com/problems/valid-palindrome/

## Problem Summary

Given a string `s`, determine whether it is a palindrome after:

- converting uppercase letters to lowercase
- removing or ignoring non-alphanumeric characters

A palindrome reads the same forward and backward.

## Core Idea

Use opposite-end two pointers.

The palindrome property is about mirrored characters:

```text
left side must match right side
```

So there is no need to build a reversed copy of the string. Compare from the
outside inward.

## Key Realization

Non-alphanumeric characters do not participate in the comparison.

That means each pointer should skip invalid characters before comparing.

The main loop becomes:

1. Move `left` rightward until it points at an alphanumeric character.
2. Move `right` leftward until it points at an alphanumeric character.
3. Compare lowercase versions of both characters.
4. If they differ, return `False`.
5. Otherwise, move both inward.

## Pointer Template

```python
left = 0
right = len(s) - 1

while left < right:
    while left < right and not s[left].isalnum():
        left += 1

    while left < right and not s[right].isalnum():
        right -= 1

    if s[left].lower() != s[right].lower():
        return False

    left += 1
    right -= 1
```

## Why This Works

Each comparison checks one mirrored pair.

If any mirrored pair differs, the string cannot be a palindrome.

If all valid mirrored characters match until the pointers cross, the string is
valid.

## Pitfalls

- Forgetting to lowercase before comparison.
- Forgetting to skip punctuation and spaces.
- Moving pointers after a mismatch instead of returning immediately.
- Using extra memory when the two-pointer scan is enough.

## Final Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Each pointer moves across the string at most once.

## Interview Trigger

If you see:

- palindrome
- mirrored comparison
- ignore punctuation/case
- can compare from both ends

Think:

```text
opposite-end two pointers
```

## Retention Card

- Problem: 125. Valid Palindrome
- Difficulty: Easy
- Time Spent: ___
- Pattern: opposite-end two pointers
- Trigger: compare mirrored characters while ignoring non-alphanumeric chars
- Core Insight: palindrome property can be checked from outside inward
- Template: move `l`/`r` inward, skipping invalid chars
- Complexities: `O(n)` time, `O(1)` space

Process:

- Brute force would reverse/filter string.
- Realized only paired comparisons matter.
- Two pointers shrink search space each iteration.

Mistakes:

- Forgetting to lowercase.
- Forgetting to skip punctuation.
