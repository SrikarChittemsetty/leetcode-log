# LeetCode 210: Course Schedule II

## Metadata

- Difficulty: Medium
- Topic: Graphs / DFS / Cycle Detection / Dependency Ordering
- Time: ~40 minutes
- Result: Solved by extending Course Schedule I logic to construct a valid ordering
- Link: https://leetcode.com/problems/course-schedule-ii/

## Problem Summary

We are given:

- `numCourses`
- prerequisite pairs:

```text
[a, b]
```

This means:

```text
to take course a, you must first complete course b
```

Unlike Course Schedule I, we are no longer only checking whether completion is
possible.

Now we must:

- detect whether any logical inconsistencies exist
- construct a valid ordering containing all courses

If no valid ordering exists, return an empty list.

## Key Insight

This problem is essentially:

```text
Course Schedule I + recording the dependency resolution order
```

The prerequisite relationships form a directed dependency graph.

A cycle represents a logical impossibility:

```text
0 -> 1 -> 2 -> 0
```

If any cycle exists:

- no valid ordering exists
- return `[]`

Otherwise, a course can only be added to the answer after all prerequisites
beneath it are fully resolved.

## Graph Representation

The prerequisite list is reshaped into an adjacency list:

```text
course -> prerequisites
```

Example:

```python
[[1, 0], [2, 0], [3, 1], [3, 2]]
```

becomes:

```python
{
    0: [],
    1: [0],
    2: [0],
    3: [1, 2],
}
```

This allows efficient recursive traversal of dependency chains.

## DFS Meaning

The recursive function:

```python
dfs(course)
```

represents:

```text
Can this course's dependency graph be resolved without cycles?
```

If successful, the DFS also appends courses to the final ordering.

## Core DFS State

### `path`

Tracks the current active recursion chain.

If DFS revisits a course already in `path`, a cycle exists.

Example:

```text
0 -> 1 -> 2 -> 0
```

During DFS:

```python
path = {0, 1, 2}
```

Revisiting `0` means a contradiction was found.

### `safe`

Tracks courses already fully processed safely.

If a course is already in `safe`, we immediately return `True` and avoid
recomputation.

This also prevents duplicate insertions into the final ordering.

### `order`

The final valid course ordering.

Unlike `path`, this persists permanently across DFS calls.

Courses are appended only after all prerequisites are resolved.

## Critical Ordering Insight

A course is added to `order` only after DFS finishes exploring all prerequisite
branches.

This naturally guarantees:

```text
prerequisites appear before the course that depends on them
```

Example:

```text
1 depends on 0
```

DFS flow:

```text
dfs(1)
    dfs(0)
        append 0
    append 1
```

Result:

```python
[0, 1]
```

The recursion stack itself constructs the dependency ordering automatically.

## Base Cases

Cycle detected:

```python
if course in path:
    return False
```

Already processed safely:

```python
if course in safe:
    return True
```

## Recursive Flow

1. Add current course to `path`.
2. DFS through all prerequisites.
3. If any prerequisite fails, propagate `False`.
4. After all prerequisites succeed:
   - remove the course from `path`
   - mark it safe
   - append it to the final ordering
   - return `True`

## Important Insight About Shared State

### `path`

Represents only the current active recursion chain.

It is temporary and shrinks as recursion unwinds.

### `order`

Represents the global final ordering.

It is intentionally shared across all top-level DFS calls so disconnected graph
components combine into one valid answer.

### `safe`

Acts as global memoization.

Once a course is processed:

- future DFS calls immediately return
- duplicate appends are avoided

## Breakthroughs

- Reused Course Schedule I cycle detection logic.
- Realized the answer is built by appending after dependency DFS completes.
- Separated temporary recursion state (`path`) from permanent result state (`order`).
- Used `safe` both for memoization and to prevent duplicate output.
- Initialized every course in `preMap`, including courses with no prerequisites.

## Pitfalls

- Appending a course before exploring prerequisites produces invalid ordering.
- Forgetting `safe` can duplicate courses in the result.
- Treating `path` like global visited state incorrectly marks valid shared dependencies as cycles.
- Returning a partial `order` when any cycle exists instead of returning `[]`.

## Final Solution

```python
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        safe = set()
        path = set()

        def dfs(course):
            if course in safe:
                return True

            if course in path:
                return False

            path.add(course)

            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False

            path.remove(course)
            safe.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return order
```

## Complexity

- Time: `O(V + E)`
- Space: `O(V + E)`

Where:

- `V` = number of courses
- `E` = prerequisite relationships

## Mental Model

Think of DFS as recursively resolving dependencies from the bottom upward.

A course enters the final ordering only after all courses beneath it are already
solved.

The recursion stack naturally builds:

```text
prerequisite-first ordering
```

## Interview Trigger

If you see:

- prerequisite chains
- dependency resolution
- "return a valid order"
- contradictions/cycles

Think:

```text
DFS dependency traversal with recursion path cycle detection and postorder insertion into the result list
```
