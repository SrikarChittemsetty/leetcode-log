# Alternatives

## Two Frequency Maps

Build one map for each string and compare them:

```python
return count_s == count_t
```

This is very readable and maps directly to the definition of an anagram.

## Sorting

Sort both strings and compare:

```python
return sorted(s) == sorted(t)
```

This is concise, but it costs `O(n log n)` time because of sorting.

## Fixed-Size Array

If the character set is known to be only lowercase English letters, a list of
26 counts can replace the dictionary.

The hash map version is more general.
