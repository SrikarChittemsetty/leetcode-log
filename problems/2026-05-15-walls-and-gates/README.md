# LeetCode 286: Walls and Gates

## Metadata

- Difficulty: Medium
- Topic: Graphs / Grid BFS / Multi-Source BFS
- Time:
- Result: Solved after recognizing gates as simultaneous BFS sources
- Link: https://leetcode.com/problems/walls-and-gates/

## Problem Summary

We are given a 2D grid of rooms:

- `-1` = wall or obstacle
- `0` = gate
- `INF` = empty room

For every empty room, fill it with the distance to its nearest gate.

If a gate cannot be reached, leave the room as `INF`.

The grid must be modified in-place.

## Core Insight

We need the minimum distance to a gate in an unweighted grid.

This is a shortest path problem, so BFS is the natural fit because:

- BFS explores by distance layers
- first visit to a cell guarantees shortest path

## Important Realization

A naive approach would be:

```text
BFS from every empty room toward gates
```

But this repeats huge amounts of work.

Better idea:

```text
start BFS from all gates simultaneously
expand outward once
```

This is multi-source BFS.

## Key Abstraction

Treat all gates as starting points with distance `0`.

Then:

- neighbors of gates become `1`
- their neighbors become `2`
- and so on

Propagation rule:

```python
neighbor_distance = current_distance + 1
```

## Core BFS Invariant

When a cell is popped from the queue:

```text
its value already equals the shortest distance to a gate
```

Therefore:

- we never need to revisit/update cells
- first write is optimal

This is why we only expand into:

```python
INF
```

cells.

## Important BFS Understanding

BFS is not a recursive function like DFS often is.

The queue-driven traversal itself is the BFS process:

```python
while queue:
    r, c = queue.popleft()

    for neighbor in neighbors:
        queue.append(neighbor)
```

The queue enforces level-order exploration.

## Reusable Grid Template

Directions:

```python
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
```

Typical grid BFS flow:

1. Initialize queue.
2. Add starting cells.
3. Pop cell.
4. Explore neighbors.
5. Validate bounds and state.
6. Update neighbor.
7. Push neighbor into queue.

## Breakthroughs

- Recognized the problem as shortest path in an unweighted grid.
- Replaced repeated room-to-gate BFS with one gate-to-room BFS.
- Used all gates as distance-`0` starting points.
- Understood why first write to an `INF` cell is already optimal.

## Pitfalls

- Starting BFS from each empty room, causing repeated work.
- Revisiting cells after they already have a shortest distance.
- Forgetting to skip walls.
- Treating BFS as recursion instead of queue-driven level traversal.

## Final Solution

```python
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0
                    or nr >= rows
                    or nc < 0
                    or nc >= cols
                    or rooms[nr][nc] != INF
                ):
                    continue

                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
```

## Complexity

- Time: `O(m * n)`
- Space: `O(m * n)`

Each cell is visited at most once.

## Mental Model

Imagine all gates sending out waves at the same time.

The first wave to reach an empty room gives that room its shortest distance to a
gate.

## Interview Trigger

If you see:

- shortest path
- unweighted graph or grid
- nearest source
- minimum number of moves or steps

Think:

```text
BFS
```

If there are multiple starting sources:

```text
multi-source BFS
```
