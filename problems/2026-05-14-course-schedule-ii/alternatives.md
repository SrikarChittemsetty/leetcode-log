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

## Relationship To Course Schedule I

Course Schedule I asks:

```text
Is there a cycle?
```

Course Schedule II asks:

```text
If there is no cycle, what is one valid topological ordering?
```

The DFS version answers both by using cycle detection plus postorder insertion.
