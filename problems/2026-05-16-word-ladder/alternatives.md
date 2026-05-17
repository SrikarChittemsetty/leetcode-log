# Alternatives

## Pattern Map

Another common optimization precomputes wildcard patterns:

```text
hot -> *ot, h*t, ho*
```

Then words sharing a pattern are neighbors.

This avoids trying all 26 letters at each position during BFS, but it requires
extra preprocessing and a pattern-to-words map.

## Bidirectional BFS

Bidirectional BFS expands from both `beginWord` and `endWord`.

This can be much faster because the search frontier grows from both ends and may
meet in the middle.

The core idea remains the same: shortest path in an unweighted implicit graph.
