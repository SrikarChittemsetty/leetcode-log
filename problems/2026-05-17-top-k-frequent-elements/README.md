# LeetCode 347: Top K Frequent Elements

## Metadata

- Difficulty: Medium
- Topic: Arrays & Hashing / Heap / Priority Queue
- Result: Solved
- Link: https://leetcode.com/problems/top-k-frequent-elements/

## Problem Summary

Given an integer array `nums` and integer `k`, return the `k` most frequent
elements.

The answer is guaranteed to be unique, so no tie-breaking logic is required.

## Initial Understanding

Core realization:

```text
The problem is not about the largest numbers, but the numbers with the largest frequencies.
```

Therefore the first mandatory step is:

```text
compute frequencies
```

## Brute Force / Natural Progression

Initial instinct:

1. Count occurrences of every number.
2. Compare counts repeatedly.
3. Extract the top `k`.

This immediately suggested a frequency map:

```text
number -> count
```

using a dictionary.

## First Optimization: Sorting

After frequencies were available, the next natural observation:

```text
Full repeated scans are wasteful.
```

So the first improved solution idea:

```text
sort by frequency
take top k
```

This works because sorting places highest frequencies together.

However, deeper observation:

```text
We only need the top k, not a full ordering of everything.
```

This motivates heaps.

## Heap Insight

Key conceptual jump:

### Sorting

Fully orders all elements.

### Heap

Maintains access to the current minimum/maximum efficiently and avoids
unnecessary full ordering.

Mental rule:

```text
Full ranking -> sorting
Top k only -> heap
```

## Important Heap Realizations

### Python Heaps Are Min-Heaps

Python's `heapq` only directly implements min-heaps.

Two valid strategies:

## Strategy 1: Simulated Max-Heap

Store:

```python
(-freq, num)
```

because more negative values rise to the top of a min-heap.

The largest real frequency is popped first.

## Strategy 2: Min-Heap Of Size `k`

This is the final implemented approach.

Invariant:

```text
heap always contains the current best k candidates
```

Process:

1. Push `(freq, num)`.
2. If heap size exceeds `k`, pop the smallest frequency.
3. Remaining heap elements are the top `k`.

This avoids simulating a max-heap entirely.

## Heap Structure Understanding

A heap only guarantees ordering at the root/top.

It does not fully sort all elements.

For a min-heap:

```text
smallest element is always at index 0
```

The rest are only partially ordered.

Also learned:

- `heappush()` restructures the heap automatically
- `heappop()` removes the root and reheapifies afterward

## Python Heap Notes

### Initialization

```python
heap = []
```

A heap is fundamentally just a list.

### `heapify()`

Used only when converting an existing list into heap structure:

```python
heapq.heapify(arr)
```

Not needed when inserting incrementally with `heappush()`.

### Tuple Ordering

Tuples in heaps order lexicographically:

```text
first element first, then second element if needed
```

For this problem:

```python
(freq, num)
```

means frequency controls the heap priority.

## Important Frequency Map Syntax

Reinforced pattern:

```python
freq_map[num] = freq_map.get(num, 0) + 1
```

Meaning:

1. retrieve existing count if present
2. otherwise use `0`
3. increment
4. assign back into dictionary

## Breakthroughs

- Identified frequency counting as the mandatory first step.
- Recognized sorting works but over-solves the problem.
- Connected "top k only" to heap maintenance.
- Used a min-heap of size `k` instead of a full max-heap.
- Understood that a heap is partially ordered, not fully sorted.

## Pitfalls

- Sorting numbers by value instead of frequency.
- Building a full sorted order when only `k` elements are needed.
- Assuming Python `heapq` is a max-heap.
- Expecting the final heap list to be sorted.
- Forgetting to pop when heap size exceeds `k`.

## Final Solution

```python
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
```

## Complexity Analysis

Let:

- `n` = total numbers
- `m` = distinct numbers

### Time Complexity

Frequency counting:

```text
O(n)
```

Heap operations:

- performed for each distinct number
- each insertion/removal costs `O(log k)`

Total:

```text
O(n + m log k)
```

### Space Complexity

Frequency map:

```text
O(m)
```

Heap:

```text
O(k)
```

Overall:

```text
O(m)
```

because the frequency map dominates.

## Key Takeaways

Conceptual lessons:

- frequency problems often begin with hashing
- top `k` problems naturally suggest heaps
- heaps avoid unnecessary full sorting

Heap insight:

```text
Heap does not mean all top k are automatically sorted.
It means efficient maintenance of current best candidates.
```

Python lessons reinforced:

- `heapq` is min-heap only
- heaps are implemented as lists
- `heapify()` vs incremental insertion
- tuples in heaps order lexicographically by first element first

## Interview Communication Strengths

Successfully reasoned through:

- why sorting is wasteful
- why heaps improve top-k
- difference between max-heap simulation and min-heap maintenance
- heap invariants
- asymptotic comparison:
  - sorting: `O(m log m)`
  - heap: `O(m log k)`

## Interview Trigger

If you see:

- frequencies
- top `k`
- avoid full sorting
- repeated extraction of best candidates

Think:

```text
frequency map + heap of size k
```

## Retention Card

- Problem: 347. Top K Frequent Elements
- Difficulty: Medium
- Time Spent: ___
- Pattern: frequency counter + bucket/heap
- Trigger: need most frequent elements
- Core Insight: first count frequencies, then retrieve largest counts
- Template: count values, bucket by frequency, collect from highest bucket
- Complexities: `O(n)` time with bucket, `O(n)` space

Process:

- First step is ordinary frequency counting.
- Sorting counts works but costs `O(n log n)`.
- Bucket sort uses frequency range `0..n`.

Mistakes:

- Do not confuse this with stream top-k; static input can be bucketed.
