# Alternate Solutions

## Two-Stage Binary Search

Idea:

1. Binary search over rows to find the only row that could contain `target`.
2. Binary search inside that row.

Complexity:

- Time: `O(log m + log n)`
- Space: `O(1)`

Why I prefer virtual flattening:

- One binary search instead of two.
- Directly matches the `O(log(m * n))` target.
- Reinforces the mental model that the matrix is a sorted 1D array in disguise.

