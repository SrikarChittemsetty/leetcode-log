# LeetCode 49: Group Anagrams

## Metadata

- Difficulty: Medium
- Topic: Arrays & Hashing / Frequency Signatures
- Platform: NeetCode / LeetCode-style
- Result: Solved
- Link: https://leetcode.com/problems/group-anagrams/

## Problem Summary

Given a list of strings, group the anagrams together.

Two words are anagrams if they contain the exact same characters with the exact
same frequencies.

## Core Idea

Group words by a shared anagram signature.

Instead of comparing strings directly, compute a canonical signature for each
word.

Words with the same signature belong in the same group.

## Key Realization

A frequency dictionary like:

```python
{"a": 1, "c": 1, "t": 1}
```

represents the right idea, but dictionaries are mutable and not hashable.

That means they cannot be used as keys in another dictionary.

Since all characters are lowercase English letters, use a fixed 26-length count
array:

```python
[0] * 26
```

Each index represents a letter:

```text
0 -> a
1 -> b
...
25 -> z
```

Then convert the final list into a tuple:

```python
key = tuple(count)
```

Tuples are immutable and hashable, so they can be dictionary keys.

## Grouping Structure

The dictionary shape is:

```text
signature -> list of words with that signature
```

Example:

```python
{
    (1, 0, 1, ...): ["act", "cat"],
    ...: ["stop", "pots", "tops"],
}
```

## Important Python Notes

Use ASCII/Unicode offset to find the character index:

```python
idx = ord(c) - ord("a")
```

Return only the grouped lists, not the dictionary:

```python
return list(groups.values())
```

`groups.values()` is a dictionary view, so casting gives the expected list of
lists.

## Breakthroughs

- Reused the anagram frequency-counting idea.
- Recognized that groups need a canonical hashable key.
- Replaced mutable dictionaries/lists with tuple signatures.
- Used `defaultdict(list)` so each signature naturally accumulates words.

## Pitfalls

- Trying to use a dictionary or list directly as a dictionary key.
- Returning the dictionary instead of its grouped values.
- Forgetting to reset the count array for each word.
- Sorting each word unnecessarily when a fixed count signature is available.

## Final Solution

```python
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())
```

## Complexity

Let:

- `n` = number of strings
- `k` = maximum string length

### Time

`O(n * k)`

We process every word and scan each character to build its signature.

### Space

`O(n * k)`

The output stores all words. The tuple keys are fixed size `26`, so they are
effectively constant per group.

## Takeaways

This problem extends Valid Anagram:

- Valid Anagram checks if two signatures match.
- Group Anagrams uses signatures as dictionary keys to collect matching words.

Main lesson:

```text
When objects share a property, turn that property into a canonical key and group by it.
```

## Interview Trigger

If you see:

- group similar strings
- anagrams
- same character frequencies
- collect items by shared structure

Think:

```text
canonical frequency signature -> dictionary grouping
```
