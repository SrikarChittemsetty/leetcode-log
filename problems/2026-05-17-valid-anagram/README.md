# LeetCode 242: Valid Anagram

## Metadata

- Difficulty: Easy
- Topic: Arrays & Hashing / Frequency Counting
- Primary Pattern: Frequency counting with hash maps
- Secondary Pattern: Net-difference frequency tracking
- Result: Solved
- Link: https://leetcode.com/problems/valid-anagram/

## Retention Card

- Pattern: frequency counter
- Trigger: compare whether two strings have identical character counts
- Core Insight: anagrams have the same frequency distribution
- Template: count chars in `s`, subtract chars in `t`, check all zero
- Complexity: `O(n)` time, `O(1)` space for fixed alphabet / `O(k)` general

Process:

- sorting works but costs `O(n log n)`
- counting preserves exact character distribution faster
- compare counts instead of order

Mistake to watch:

- length mismatch can return `False` immediately

## Problem Summary

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Definition used during solve:

```text
Two strings are anagrams if every character appears the same number of times in both strings.
```

## Initial Observations

### Key Early Observation

If the strings have different lengths, they cannot possibly be anagrams.

Immediate filter:

```python
if len(s) != len(t):
    return False
```

This was identified before deeper logic.

## Brute Force Thought Process

Initial conceptual direction:

```text
For each character, determine how many times it appears in both strings.
Compare frequencies.
```

Naive implementation instinct:

- repeatedly scan strings to count characters
- repeated passes / recounting
- inefficient due to redundant work

Important transition:

```text
Repeatedly scanning for counts is unnecessary if counts can be stored as they are encountered.
```

## Core Optimization Realization

Major abstraction:

```text
How many times does this character appear?
```

becomes:

```text
Can I maintain character frequencies incrementally?
```

This naturally leads to:

```text
hash maps / dictionaries
character -> count
```

## First Optimized Solution

Initial optimized architecture:

1. Build frequency map for `s`.
2. Build frequency map for `t`.
3. Compare dictionaries directly with `==`.

Key insight:

Python dictionary equality checks:

- identical keys
- identical associated values

So frequency equality maps perfectly onto the problem definition.

## Deeper Refinement

### Single-Map Optimization

While naming the dictionaries, a deeper realization occurred:

```text
We do not actually need two maps if we track net differences.
```

New abstraction:

- increment counts for characters in `s`
- decrement counts for characters in `t`

Then:

```text
all final counts must equal 0
```

This reduced the conceptual model from:

```text
compare two distributions
```

to:

```text
ensure all frequency differences cancel out
```

This is the interview-level refinement.

## Important Implementation Insights

### Using `.get()`

Correct pattern:

```python
freq_map[c] = freq_map.get(c, 0) + 1
```

Key realization:

```python
.get(key, default)
```

not:

```python
.get(default, key)
```

### Generator Expression + `all(...)`

Important Python syntax:

```python
all(val == 0 for val in freq_map.values())
```

Understanding:

- `val == 0` is a single comparison
- `val == 0 for ...` is a generator expression producing many booleans
- `all(...)` collapses them into one boolean

Also clarified:

```python
freq_map.values()
```

returns a dictionary view / iterable, not a list.

## Breakthroughs

- Began from brute force naturally.
- Identified repeated scanning inefficiency.
- Derived the frequency abstraction independently.
- Refined from two maps to one net-difference map.
- Added early negative-count short-circuit.
- Reasoned carefully about Python syntax instead of memorizing it.

## Pitfalls

- Forgetting the early length mismatch check.
- Repeatedly scanning strings instead of storing counts.
- Reversing `.get(key, default)` arguments.
- Forgetting that a negative count means `t` has too many of that character.
- Misreading generator expression syntax inside `all(...)`.

## Final Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = {}

        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        for c in t:
            if c not in freq_map:
                return False

            freq_map[c] -= 1

            if freq_map[c] < 0:
                return False

        return all(val == 0 for val in freq_map.values())
```

## Complexity Analysis

### Time Complexity

`O(n)`

Reasoning:

- one pass through `s`
- one pass through `t`
- final validation over map values

Linear overall.

### Space Complexity

`O(n)`

Worst case:

- every character is distinct
- frequency map grows proportionally to input size

## Interview Communication Notes

Strong elements demonstrated during solve:

- began from brute force naturally
- identified repeated scanning inefficiency
- derived frequency abstraction independently
- refined from two maps to one net-difference map
- introduced early negative-count short-circuit
- reasoned carefully about Python syntax instead of memorizing

## Key Takeaways For Future Review

Patterns reinforced:

- Arrays & Hashing
- Frequency counting
- Hash maps for incremental state tracking
- "seen/count" transformations

Important conceptual move:

```text
Many hashing problems become simpler when reframed from searching repeatedly into maintaining state incrementally during traversal.
```

Python concepts reinforced:

- `.get(key, default)`
- generator expressions
- `all(...)`
- dictionary views with `.values()`

## Estimated Solve Progression

- Problem understanding: fast
- Core frequency-map insight: fast
- One-map refinement: strong independent realization
- Python syntax debugging around generator expressions: main learning section
- Final solution quality: interview-ready

## Interview Trigger

If you see:

- character counts
- same elements/frequencies
- permutation/anagram wording
- repeated scanning temptation

Think:

```text
frequency map or net-difference count map
```
