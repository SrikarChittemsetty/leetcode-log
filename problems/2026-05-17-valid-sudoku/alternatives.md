# Alternatives

## Separate Passes

One readable approach is to validate:

1. all rows
2. all columns
3. all boxes

This mirrors the Sudoku rules directly but requires multiple logical passes.

The one-pass solution keeps the same constraints but checks them together.

## Encoded Seen Set

Another concise approach stores encoded facts in one set:

```python
("row", r, val)
("col", c, val)
("box", r // 3, c // 3, val)
```

If any encoded fact already exists, the board is invalid.

Separate dictionaries are a little more verbose but easier to explain.
