# Alternatives

## Hash Set

A hash set can find the duplicate by tracking seen values:

```python
seen = set()
for num in nums:
    if num in seen:
        return num
    seen.add(num)
```

This is simple, but it uses `O(n)` extra space, which violates the intended
constraint.

## Sorting

Sorting would place duplicate values next to each other, but sorting the array
modifies the input unless a copy is made.

- in-place sort violates the "do not modify the array" constraint
- copied sort uses `O(n)` extra space

## Binary Search On Value Range

Another valid `O(1)` space approach is binary searching over the value range and
counting how many values are `<= mid`.

This runs in `O(n log n)` time. Floyd's cycle detection improves that to `O(n)`.
