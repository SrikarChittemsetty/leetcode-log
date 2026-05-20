# LeetCode 19: Remove Nth Node From End of List

## Metadata

- Difficulty: Medium
- Topic: Linked List / Fast and Slow Pointers
- Result: Solved
- Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Problem Summary

Given the head of a linked list, remove the `n`th node from the end of the list
and return the updated head.

The challenge is that linked lists do not support direct indexing, and the
target is described relative to the end.

## Core Idea

Use fast and slow pointers with a fixed gap of `n`.

If `fast` is always `n` nodes ahead of `slow`, then when `fast` reaches the end,
`slow` is positioned right before the node that must be removed.

## Key Realization

A first instinct is to count the list length, compute:

```text
length - n
```

and then make a second pass to remove the node.

That works, but the fixed-gap trick removes the need for a separate length
calculation.

## Dummy Node Insight

Use a dummy node before `head`:

```python
dummy = ListNode(0, head)
```

This simplifies removal when the head itself must be deleted.

Without a dummy node, head removal needs special-case logic.

With a dummy node, every removal becomes:

```python
slow.next = slow.next.next
```

## Pointer Flow

Start both pointers at `dummy`:

```python
fast = dummy
slow = dummy
```

Advance `fast` exactly `n` steps:

```python
for _ in range(n):
    fast = fast.next
```

Then move both pointers until `fast.next` reaches the end:

```python
while fast.next:
    fast = fast.next
    slow = slow.next
```

At that point, `slow.next` is the node to remove.

## Why This Works

The gap between `fast` and `slow` is maintained at `n` nodes.

When `fast` reaches the last node, `slow` is exactly one node before the target.

That position is what linked-list deletion needs, because deleting a node
requires changing the previous node's `next` pointer.

## Pitfalls

- Forgetting to use a dummy node.
- Moving `fast` and `slow` together before creating the `n`-node gap.
- Stopping the loop at the wrong time.
- Returning `head` instead of `dummy.next`.
- Losing access to the previous node before deletion.

## Final Solution

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

The list is traversed with pointers, and no extra data structure is needed.

## Interview Trigger

If you see:

- linked list
- node relative to the end
- remove in one pass
- no length known upfront

Think:

```text
fast/slow pointers with a fixed gap
```

## Retention Card

- Problem: 19. Remove Nth Node From End of List
- Difficulty: Medium
- Time Spent: ___
- Pattern: fast/slow pointers
- Trigger: need node relative to end without knowing length
- Core Insight: keep fixed gap of `n` between pointers
- Template: advance fast `n` steps, move both until fast ends
- Complexities: `O(n)` time, `O(1)` space

Process:

- First instinct may be count length first.
- Gap trick removes need for second pass.
- Dummy node simplifies head removal.

Mistakes:

- Use dummy node.
- Move fast `n` times before moving both.
