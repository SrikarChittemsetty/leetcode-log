# LeetCode 271: Encode and Decode Strings

## Metadata

- Difficulty: Medium
- Topic: Arrays & Hashing / String Design / Length-Prefix Encoding
- Result: Solved
- Link: https://leetcode.com/problems/encode-and-decode-strings/

## Problem Summary

Design two functions:

```python
encode(strs) -> str
decode(s) -> List[str]
```

The encoded string must preserve the original list exactly, including:

- empty strings
- delimiters inside strings
- any ASCII characters

## Key Realization

A simple delimiter fails.

Example:

```python
["a,b", "c"]
```

If encoded with commas, decoding becomes ambiguous.

So the solution needs length information.

## Encoding Format

Use:

```text
length#string
```

Example:

```python
["Hi", "abc"]
```

becomes:

```text
2#Hi3#abc
```

The `#` only separates the length from the string.

Even if the string contains `#`, decoding still works because we read exactly
`length` characters after the separator.

## Decode Logic

Use a pointer `i`.

For each encoded string:

1. Set `j = i`.
2. Move `j` until it reaches `#`.
3. Parse `s[i:j]` as the length.
4. Read from `j + 1` to `j + 1 + length`.
5. Append that word.
6. Move `i` to the next unread position.

Important detail:

```python
while s[j] != "#":
    j += 1
```

stops with `j` positioned on the `#`.

So:

```python
s[i:j]
```

gives the length, and:

```python
s[j + 1 : j + 1 + length]
```

gives the word.

## Breakthroughs

- Recognized delimiter-only encoding is ambiguous.
- Added explicit length metadata before each string.
- Used pointer parsing instead of splitting.
- Understood why delimiters inside the payload do not matter once length is known.

## Pitfalls

- Using `.split("#")`, which fails when strings contain `#`.
- Forgetting empty strings must round-trip correctly.
- Moving `i` to the wrong next position.
- Treating the separator as part of the string payload.

## Final Solution

```python
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            decoded.append(word)

            i = j + 1 + length

        return decoded
```

## Complexity

Let `n` be the total number of characters across all strings.

- Time: `O(n)`
- Space: `O(n)`

Each character is processed linearly during encode/decode.

The encoded string and decoded output scale with total input size.

## Key Takeaways

The core pattern:

```text
When delimiters may appear inside data, use length-prefix encoding.
```

This avoids ambiguity and makes decoding deterministic.

## Interview Trigger

If you see:

- serialize/deserialize
- encode/decode
- delimiters can appear inside data
- exact round-trip required

Think:

```text
length-prefix encoding
```

## Retention Card

- Problem: 271. Encode and Decode Strings
- Difficulty: Medium
- Time Spent: ___
- Pattern: length-prefix encoding
- Trigger: need combine strings without ambiguity
- Core Insight: delimiters alone are unsafe because strings can contain any character
- Template: encode as `len + "#" + string`
- Complexities: `O(total characters)` time, `O(total characters)` space

Process:

- Simple join fails if delimiter appears inside strings.
- Length tells decoder exactly how many characters to read.
- Decode by reading digits until `"#"`, then taking length chars.

Mistakes:

- After reading length, move past `"#"`.
- Empty string works as `0#`.
