# Alternatives

## Brute Force

Check every pair:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

This is simple but costs `O(n^2)` time.

## Sorting

Sorting plus two pointers can find values that sum to the target, but the
problem asks for original indices. Keeping index information makes this more
awkward than the hash map approach.
