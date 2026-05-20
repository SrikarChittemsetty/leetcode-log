# LeetCode 36: Valid Sudoku

## Metadata

- Difficulty: Medium
- Topic: Arrays & Hashing / Constraint Tracking
- Result: Solved
- Link: https://leetcode.com/problems/valid-sudoku/

## Problem Summary

Determine whether a partially filled Sudoku board is valid.

Important clarification learned:

The board:

- does not need to be complete
- does not need to be solvable

A board is valid if:

- no row contains duplicate digits
- no column contains duplicate digits
- no `3 x 3` sub-box contains duplicate digits

Empty cells `"."` are ignored.

## Initial Confusion / Clarification

At first, the wording:

```text
Each row must contain digits 1-9 without repetition
```

seemed to imply every row had to be fully populated.

Key clarification:

For this problem:

- only existing digits matter
- missing digits are allowed
- duplicates are forbidden

So validity means:

```text
No currently placed number violates Sudoku constraints.
```

## Brute Force Thought Process

Natural initial approach:

- scan every row with a set
- scan every column with a set
- scan every sub-box with a set

Core idea:

```text
detect duplicates efficiently via membership checking
```

This naturally suggests hash sets.

## Optimization Insight

Rather than:

- separate row pass
- separate column pass
- separate box pass

the checks can all happen simultaneously during one traversal of the board.

This led to maintaining:

- row sets
- column sets
- box sets

all at once.

## Data Structure Design

Use:

```python
rows[r]
cols[c]
boxes[(r // 3, c // 3)]
```

Each maps to a set of digits already seen.

## Why Separate Dictionaries?

Rows, columns, and boxes represent distinct Sudoku constraints.

Keeping separate structures:

- improves clarity
- avoids key collisions
- mirrors the problem definition directly

## Sub-Box Insight

Major realization:

```python
(r // 3, c // 3)
```

partitions the board into `3 x 3` sections.

Examples:

```text
(0, 0) -> top-left box
(1, 2) -> still top-left box
(4, 7) -> middle-right box
```

Integer division cleanly groups coordinates into thirds.

## `defaultdict` Insight

Learned that:

```python
defaultdict(set)
```

passes the constructor itself, not an actual set object.

Meaning:

```text
missing key automatically creates set()
```

without manual initialization.

Equivalent manual approach would require:

```python
if key not in rows:
    rows[key] = set()
```

## Important Bug Encountered

Initial implementation forgot to skip `"."`.

This caused:

```text
multiple empty cells to appear as duplicates
```

Fix:

```python
if board[r][c] == ".":
    continue
```

Important lesson:

```text
Empty cells are placeholders, not Sudoku values.
```

## Breakthroughs

- Clarified that validity only checks currently placed digits.
- Used sets for duplicate detection.
- Combined row, column, and box checks into one traversal.
- Used `(r // 3, c // 3)` as a clean sub-box key.
- Fixed the empty-cell bug by skipping `"."`.

## Pitfalls

- Treating `"."` as a real value.
- Thinking rows/columns/boxes must contain all digits.
- Forgetting that sub-boxes need their own duplicate checks.
- Using one shared set for all constraints.
- Miscomputing box identity without integer division.

## Final Solution

```python
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True
```

## Complexity Analysis

### Exact Problem Constraints

Board size is fixed:

```text
9 x 9
```

So:

- maximum 81 cells
- runtime is bounded by a constant

Therefore:

- Time: `O(1)`
- Space: `O(1)`

### Generalized Complexity Discussion

For an `n x n` board:

```text
traversing all cells -> O(n^2)
```

This clarified an important interview principle:

```text
Complexity depends on how the input is allowed to scale.
```

If dimensions are fixed constants, asymptotically the work becomes constant
time/space.

## Key Takeaways

Patterns reinforced:

- hashing for duplicate detection
- simultaneous constraint tracking
- coordinate partitioning via integer division

Python concepts reinforced:

- `defaultdict(set)`
- nested traversal
- tuple dictionary keys

Important conceptual lesson:

```text
Sometimes the most elegant optimization is not reducing asymptotic complexity, but combining multiple logical passes into a single coherent traversal.
```

## Interview Trigger

If you see:

- grid validation
- duplicate constraints
- rows/columns/regions
- fixed coordinate partitions

Think:

```text
sets for each constraint group
```

## Retention Card

- Problem: 36. Valid Sudoku
- Difficulty: Medium
- Time Spent: ___
- Pattern: constraint tracking with sets
- Trigger: need validate uniqueness across multiple regions
- Core Insight: each number must be unique in its row, column, and `3 x 3` box
- Template: rows, cols, boxes sets
- Complexities: `O(1)` time and space technically because board is fixed `9 x 9`

Process:

- Every filled cell creates three constraints.
- If value already exists in any relevant set, invalid.
- Box key is `(r // 3, c // 3)`.

Mistakes:

- Skip `"."`.
- Box indexing is the main detail.
