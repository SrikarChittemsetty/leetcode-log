# LeetCode 74: Search a 2D Matrix

## Metadata

- Difficulty: Medium
- Topic: Binary Search / Matrix / Divide and Conquer
- Time: ~18 minutes
- Result: Solved after minor boundary fix
- Link: https://leetcode.com/problems/search-a-2d-matrix/

## Problem Summary

Given a 2D matrix where each row is sorted in non-decreasing order and the first element of each row is greater than the last element of the previous row, determine whether a target value exists in the matrix.

Goal: achieve `O(log(m * n))` time complexity.

## Key Insight

The matrix is not truly 2D in terms of ordering. It is a flattened sorted 1D array in disguise.

Instead of searching row by row:

1. Treat the matrix as a virtual array of size `m * n`.
2. Apply binary search on index space.
3. Convert each virtual index back to matrix coordinates.

Mapping:

```python
row = mid // cols
col = mid % cols
```

This allows standard binary search logic to work in `O(log(m * n))`.

## Breakthroughs

- Recognized the matrix can be treated as a flattened sorted array.
- Identified binary search applicability on virtual index space.
- Derived correct index-to-coordinate mapping using division and modulo.
- Understood that midpoint is dynamic and must be recomputed each iteration.
- Fixed boundary update logic in binary search: `right = mid - 1`.

## Pitfalls

- Attempting to use a geometric middle like `(row // 2, col // 2)` instead of an index-based middle.
- Misunderstanding binary search condition by focusing on `mid` instead of moving `left` and `right`.
- Making an off-by-one boundary error such as `right = mid + 1` instead of `right = mid - 1`.
- Treating the matrix as a 2D structure instead of a linear sorted order.

## Final Solution

```python
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // cols, mid % cols
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

## Complexity

- Time: `O(log(m * n))`
- Space: `O(1)`

## Mental Model

Think of the matrix as a sorted 1D array split into rows.

Binary search is performed on the virtual index space, not the 2D structure.

## Interview Trigger

If you see:

- sorted rows
- next row always larger than the previous row
- need `O(log(m * n))` search

Immediately ask:

> Can I flatten this into a virtual 1D array and run binary search on indices instead of rows or columns?

