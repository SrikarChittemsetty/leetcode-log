# LeetCode 141: Linked List Cycle

## Metadata

- Difficulty: Easy
- Topic: Linked List / Fast and Slow Pointers
- Result: Solved
- Link: https://leetcode.com/problems/linked-list-cycle/

## Problem Summary

Given the head of a linked list, determine whether the list contains a cycle.

A cycle exists if following `next` pointers eventually leads back to a node that
was already visited.

## Core Idea

Use fast and slow pointers.

Move:

- `slow` one step at a time
- `fast` two steps at a time

If there is a cycle, the fast pointer eventually laps the slow pointer inside
the cycle.

If there is no cycle, the fast pointer reaches the end of the list.

## Key Realization

A hash set solution works:

```text
store every visited node
if a node repeats, cycle exists
```

But that uses extra memory.

The fast/slow pointer method detects the same repeated structure using pointer
speed instead of storage.

## Pointer Logic

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False
```

The loop condition is important:

```python
while fast and fast.next:
```

This ensures `fast.next.next` is safe to access.

## Why This Works

Inside a cycle, both pointers keep moving forever unless they meet.

Because `fast` moves one extra step per iteration compared to `slow`, the
distance between them inside the cycle changes by one each step.

Eventually that distance becomes zero, meaning both pointers are on the same
node.

No collision means the fast pointer reached the end, so no cycle exists.

## Pitfalls

- Forgetting to check `fast` and `fast.next` before advancing.
- Comparing node values instead of node objects.
- Moving both pointers at the same speed.
- Using extra memory when `O(1)` space is possible.

## Final Solution

```python
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Each pointer moves through the list structure a bounded number of times before
either meeting or reaching the end.

## Interview Trigger

If you see:

- linked structure
- cycle detection
- repeated node through pointers
- need constant space

Think:

```text
fast/slow pointers, slow += 1 and fast += 2
```

## Retention Card

- Problem: 141. Linked List Cycle
- Difficulty: Easy
- Time Spent: ___
- Pattern: fast/slow pointers
- Trigger: cycle detection in linked structure
- Core Insight: fast pointer eventually laps slow pointer inside cycle
- Template: `slow += 1`, `fast += 2`
- Complexities: `O(n)` time, `O(1)` space

Process:

- Set solution works with extra memory.
- Pointer speeds create inevitable collision if cycle exists.
- No collision means no cycle.

Mistakes:

- Check `fast` and `fast.next` before advancing.
