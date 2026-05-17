# Alternatives

## Brute Force

Compare every pair:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False
```

This is `O(n^2)` and repeats work.

## Length Comparison

Python can solve this concisely:

```python
return len(nums) != len(set(nums))
```

This is short, but the explicit seen-set loop better demonstrates the
left-to-right membership invariant.
