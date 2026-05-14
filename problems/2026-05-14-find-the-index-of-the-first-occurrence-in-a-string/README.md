# LeetCode 28: Find the Index of the First Occurrence in a String

## Metadata

- Difficulty: Easy
- Topic: Sliding Window / String Traversal
- Time: ~10 minutes
- Result: Solved using fixed-size sliding window
- Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Problem Summary

We are given:

- `haystack`
- `needle`

We must return:

- the index of the first occurrence of `needle` inside `haystack`
- or `-1` if it does not exist

## Initial Observation

Python already provides:

```python
haystack.find(needle)
```

which:

- returns the first matching index
- returns `-1` automatically if no match exists

So the trivial built-in solution is:

```python
return haystack.find(needle)
```

## Interview Consideration

Although `.find()` is acceptable unless forbidden, interviewers often want:

- manual indexing logic
- substring traversal reasoning
- sliding window understanding

A good interview response is:

```text
Python has a built-in .find(), but I will implement it manually.
```

## Key Insight

We know the substring length we are searching for:

```python
len(needle)
```

So we can slide a fixed-size window across `haystack`.

At each position:

1. extract the current substring window
2. compare it to `needle`

If equal:

```text
return the current left index
```

Otherwise:

```text
slide the window forward by 1
```

## Sliding Window Setup

### `left`

Start index of the current window.

### `right`

End index, exclusive.

Initial:

```python
left = 0
right = len(needle)
```

## Walkthrough

Input:

```python
haystack = "sadbutsad"
needle = "sad"
```

Initial window:

```python
haystack[0:3] = "sad"
```

Matches immediately:

```python
return 0
```

Another example:

```python
haystack = "leetcode"
needle = "leeto"
```

Sliding windows checked:

```text
"leetc"
"eetco"
"etcod"
...
```

No match found:

```python
return -1
```

## Breakthroughs

- Recognized the fixed target length as a fixed-size window.
- Used `right` as an exclusive bound to match Python slicing.
- Returned immediately on the first match to satisfy "first occurrence."
- Kept the manual solution simple instead of reaching for a more advanced string algorithm.

## Pitfalls

- Forgetting that `right` must be allowed to equal `len(haystack)`.
- Moving only one pointer instead of keeping the window size fixed.
- Returning the substring instead of its starting index.
- Overcomplicating an Easy problem with unnecessary preprocessing.

## Final Solution

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1

        return -1
```

## Complexity

- Time: `O(n * m)` worst case
- Space: `O(1)`

Where:

- `n` = `haystack` length
- `m` = `needle` length

## Mental Model

Think of a fixed-size comparison window sliding through the string.

At each step:

1. compare the current substring slice
2. if mismatch, shift the window one character right

Because the window size never changes, this becomes a straightforward
fixed-window traversal problem.

## Interview Trigger

If you see:

- substring search
- first occurrence
- fixed target length

Think:

```text
fixed-size sliding window over the larger string
```
