# Alternatives

## Kahn's Algorithm

Topological sorting with indegrees is the other standard solution:

1. Build edges from `prereq -> dependent course`.
2. Count each course's indegree.
3. Add all courses with indegree `0` to a queue.
4. Pop from the queue, append to the answer, and decrement neighbor indegrees.
5. If all courses are processed, return the ordering.
6. Otherwise, a cycle exists and return `[]`.

This is also `O(V + E)` and can be easier to explain as "take all currently
available courses first."

## DFS Colors

The `path` / `safe` approach can also be written with color states:

- `0` = unvisited
- `1` = currently visiting
- `2` = fully processed

When DFS reaches a `visiting` course, a cycle exists. When DFS finishes a course,
mark it processed and append it to the ordering.
