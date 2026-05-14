# Alternatives

## Kahn's Algorithm

Another standard solution is topological sort with indegrees:

1. Build `prereq -> courses unlocked` adjacency.
2. Count incoming prerequisites for each course.
3. Start with courses that have indegree `0`.
4. Remove courses from the queue and decrement their neighbors.
5. If all courses are processed, there is no cycle.

This is also `O(V + E)` and avoids recursion depth concerns.

## DFS State Colors

The `path` / `safe` approach can also be represented with colors:

- `0` = unvisited
- `1` = visiting
- `2` = safe / visited

Revisiting a `visiting` node means a cycle exists.
