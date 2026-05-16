# LeetCode 853: Car Fleet

## Metadata

- Difficulty: Medium
- Topic: Ordered Sweep / Monotonic State / Stack Reasoning
- Time:
- Result: Solved after reducing movement simulation to arrival-time comparison
- Link: https://leetcode.com/problems/car-fleet/

## Problem Summary

We are given:

- `target`
- `position`
- `speed`

Each car starts at `position[i]` and moves toward `target` at `speed[i]`.

Cars cannot pass each other. If a faster car catches a slower car ahead, they
merge into one fleet and move at the slower fleet's pace.

Return the number of fleets that reach the target.

## Core Insight

A car only interacts with the nearest fleet ahead because cars cannot pass.

Instead of simulating movement, compute:

```python
time_to_target = (target - position) / speed
```

If a car behind would arrive earlier than or at the same time as the fleet
ahead, it must eventually catch up and merge into that fleet.

## Key Abstraction

Process cars in road order, not arrival order.

So:

1. Pair each car as `(position, speed)`.
2. Sort by position.
3. Iterate from closest-to-target backward.

While sweeping backward:

- maintain the latest fleet arrival time seen so far
- if the current car's time is greater, it forms a new fleet
- otherwise it merges into the fleet ahead

## Important Conceptual Insight

We do not care about:

- exact collision point
- which cars belong to each fleet
- simulating movement

We only care about:

```text
Can this car catch the fleet ahead before target?
```

This collapses into comparing arrival times.

## Subtle Realization

Even if a car is faster than multiple fleets ahead, it can only merge into the
nearest one because:

- cars cannot pass
- once merged, it inherits that fleet's slower arrival behavior

The nearest fleet acts like a barrier.

## Python Reminders Learned

### `zip(position, speed)`

Produces tuples lazily:

```python
(position[i], speed[i])
```

Usually converted via:

```python
pairs = list(zip(position, speed))
```

### Tuple Sorting

Tuple sorting defaults to the first element:

```python
pairs.sort()
```

So positions sort automatically.

### Reverse Iteration

```python
for i in range(len(pairs) - 1, -1, -1):
```

This walks from the car closest to the target back toward the start.

## Breakthroughs

- Reframed the problem as an ordered sweep rather than simulation.
- Used arrival time as the representative value for each fleet.
- Recognized that a car behind merges when its arrival time is less than or equal to the fleet ahead.
- Understood that the nearest fleet ahead blocks all passing.

## Pitfalls

- Sorting by speed or arrival time instead of road position.
- Iterating from the start of the road forward, which loses the "fleet ahead" state.
- Simulating collisions unnecessarily.
- Counting a new fleet when `time <= last_time`; that car actually catches the fleet ahead.

## Final Solution

```python
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()

        fleets = 0
        last_time = 0

        for i in range(len(pairs) - 1, -1, -1):
            pos, spd = pairs[i]
            time = (target - pos) / spd

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets
```

## Complexity

- Time: `O(n log n)` because of sorting
- Space: `O(n)` for the paired list

## Mental Model

This is an ordered sweep maintaining a monotonic blocking state.

`last_time` represents the arrival time of the nearest fleet ahead.

If the current car arrives later, it cannot catch that fleet, so it starts a new
fleet.

If it arrives earlier or at the same time, it merges.

## Interview Trigger

If you see:

- entities moving in one direction
- no passing allowed
- faster objects catching slower objects
- groups collapsing into fleets

Think:

```text
sort by position, sweep from front to back, compare arrival times
```
