# LeetCode 48: Rotate Image

## Metadata

- Difficulty: Medium
- Topic: Matrix / Geometry / In-Place Mutation
- Time: ~28 minutes
- Result: Solved
- Link: https://leetcode.com/problems/rotate-image/

## Problem Summary

Rotate an `n x n` matrix 90 degrees clockwise in-place. No extra matrix allowed.

## Key Insight

This problem is not really about "moving values." It is about applying a geometric coordinate transformation.

A matrix index `(i, j)` represents a point in grid space. A 90-degree clockwise rotation maps:

```text
(i, j) -> (j, n - 1 - i)
```

Instead of doing that mapping directly, we can decompose the rotation into two simpler in-place operations:

1. Transpose the matrix across the main diagonal.
2. Reverse each row.

## Breakthroughs

- Realized this needed coordinate-based reasoning, not value-based iteration.
- Understood that transpose only swaps the upper triangle where `j > i`.
- Saw that transpose alone changes orientation but does not complete the rotation.
- Recognized row reversal as the second transform that fixes the direction.
- Caught the in-place mutation distinction: `row = row[::-1]` does not mutate the matrix row, but `row.reverse()` does.

## Pitfalls

- Iterating over values instead of indices loses position information.
- Forgetting `j > i` causes double swaps and undoes the transpose.
- Mistaking transpose alone for rotation.
- Reassigning `row` instead of mutating it in place.

## Final Solution

```python
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: transpose across the main diagonal.
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: reverse each row.
        for row in matrix:
            row.reverse()
```

## Complexity

- Time: `O(n^2)`
- Space: `O(1)`

## Mental Model

Rotation = transpose + row reversal.

More generally:

> Matrix rotation is a geometric transform that can often be decomposed into simpler in-place reflections.

## Interview Trigger

If you see:

- square matrix
- rotation, flip, or image transform
- in-place constraint

Immediately ask:

> Can this be decomposed into transpose + reversal?

