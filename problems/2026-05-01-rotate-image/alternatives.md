# Alternate Solutions

## Direct Four-Way Swap

Idea:

Rotate each layer of the matrix by moving four coordinates at a time:

```text
top -> right -> bottom -> left -> top
```

Why it works:

It applies the coordinate transform directly, but the bookkeeping is easier to get wrong than transpose + reverse.

Complexity:

- Time: `O(n^2)`
- Space: `O(1)`

Why I prefer transpose + reverse:

- Easier to explain.
- Easier to verify visually.
- Less index-heavy.
- Better reusable pattern for other matrix transforms.

