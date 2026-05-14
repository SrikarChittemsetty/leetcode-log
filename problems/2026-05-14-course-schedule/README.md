# LeetCode 207: Course Schedule

## Metadata

- Difficulty: Medium
- Topic: Graphs / DFS / Cycle Detection
- Time: ~45 minutes
- Result: Solved after reasoning through recursion state tracking
- Link: https://leetcode.com/problems/course-schedule/

## Problem Summary

We are given `numCourses` total courses and a list of prerequisite pairs:

```text
[a, b]
```

This means:

```text
to take course a, you must first take course b
```

The task is to determine whether it is possible to complete all courses.

## Key Insight

This problem reduces to cycle detection in a directed graph.

Each course is a node. Each prerequisite relationship is a directed edge:

```text
b -> a
```

A cycle represents a logical inconsistency:

```text
0 requires 1
1 requires 0
```

or more generally:

```text
0 -> 1 -> 2 -> 0
```

In these cases, no valid starting point exists.

Because there is no limit on how many courses can be taken over time, the only
thing preventing completion is a cyclic dependency chain.

## Graph Representation

The prerequisite list is reshaped into an adjacency list for efficient lookup.

Instead of repeatedly scanning the prerequisites array, we map:

```text
course -> list of prerequisites
```

Example:

```python
[[2, 0], [2, 1], [3, 2]]
```

becomes:

```python
{
    2: [0, 1],
    3: [2],
}
```

This allows efficient DFS traversal of dependency chains.

## DFS Meaning

The recursive function:

```python
dfs(course)
```

represents:

```text
Does the dependency graph flowing from this course contain a cycle?
```

It returns:

- `True` if the dependency chain is valid.
- `False` if a cycle is found.

## Core DFS State

### `path`

Tracks the current active recursion chain.

If DFS revisits a course already in `path`, then we found a cycle.

Example:

```text
0 -> 1 -> 2 -> 0
```

During exploration:

```python
path = {0, 1, 2}
```

Revisiting `0` means a logical inconsistency exists.

### `safe`

Tracks courses already proven valid.

If a course's dependency graph has already been explored safely, we can
immediately return `True` without recomputing the subtree.

This acts as DFS memoization.

## Base Cases

Cycle detected:

```python
if course in path:
    return False
```

Already verified safe:

```python
if course in safe:
    return True
```

No prerequisites:

```python
if course not in preMap:
    return True
```

A course with no prerequisites safely terminates the dependency chain.

## Recursive Flow

After surviving base cases:

1. Add the course to the current recursion path.
2. DFS through all prerequisites.
3. If any prerequisite returns `False`, propagate failure upward immediately.
4. If all prerequisite chains succeed:
   - remove the course from `path`
   - add the course to `safe`
   - return `True`

## Important Recursion Insight

`path` must be shared across recursive calls.

Initializing `path` inside `dfs()` would incorrectly reset the recursion chain at
every call and prevent cycle detection.

The recursion stack itself defines the active dependency route.

## Breakthroughs

- Recognized that the prerequisite list is a directed graph.
- Reduced the question "can all courses be completed?" to "does any dependency chain contain a cycle?"
- Separated active recursion state (`path`) from memoized safe state (`safe`).
- Understood that `path` must persist across nested recursive calls.
- Used `safe` to avoid recomputing dependency subtrees.

## Pitfalls

- Building the graph in the wrong direction and confusing course-to-prerequisite with prerequisite-to-course.
- Resetting `path` inside each DFS call, which hides cycles.
- Forgetting to remove a course from `path` after its dependencies are verified.
- Returning too early without memoizing safe courses.

## Final Solution

```python
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}

        for course, prereq in prerequisites:
            if course not in preMap:
                preMap[course] = []
            preMap[course].append(prereq)

        safe = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course not in preMap or course in safe:
                return True

            path.add(course)

            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False

            path.remove(course)
            safe.add(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True
```

## Complexity

- Time: `O(V + E)`
- Space: `O(V + E)`

Where:

- `V` = number of courses
- `E` = number of prerequisite relationships

## Mental Model

Think of prerequisites as dependency chains.

A course is valid only if every dependency route beneath it eventually
terminates without revisiting an active course.

`path` tracks:

```text
What am I currently exploring?
```

`safe` tracks:

```text
What have I already proven valid?
```

## Interview Trigger

If you see:

- prerequisite chains
- dependency ordering
- "can this all be completed?"
- contradictions in requirements

Immediately think:

```text
directed graph + cycle detection with DFS recursion state tracking
```
