# Alternatives

## Sorted String Key

A simpler canonical key is the sorted word:

```python
key = "".join(sorted(word))
```

All anagrams sort to the same string.

This is easier to write, but sorting each word costs `O(k log k)`.

## Frequency Dictionary

A frequency dictionary captures the right information, but dictionaries are
mutable and not hashable.

To use frequency data as a dictionary key, convert it into an immutable form,
such as a tuple of fixed-position counts.
