# LeetCode 21: Merge Two Sorted Lists

## Metadata

- Difficulty: Easy
- Topic: Linked List / Dummy Node / Tail Pointer
- Result: Solved
- Link: https://leetcode.com/problems/merge-two-sorted-lists/

## Problem Summary

Given the heads of two sorted linked lists, merge them into a single sorted
linked list and return its head.

Example:

```text
list1: 1 -> 3 -> 5
list2: 2 -> 4 -> 6

output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

## Pattern Recognition

This is the classic:

```text
Dummy Node + Tail Pointer
```

pattern.

Because:

- we are building a linked list
- we need to keep appending nodes
- we want to avoid special-casing the first node

## Key Observation

Both input lists are already sorted.

Therefore:

```text
The next node in the merged list must always be the smaller of list1.val and list2.val.
```

At every step, compare the two front nodes and take the smaller one.

## Linked List Mental Model

These variables are pointers:

```python
list1
list2
tail
```

They are not arrays.

Example:

```text
list1
 ↓
5 -> 7 -> 9 -> None
```

After:

```python
list1 = list1.next
```

we get:

```text
5 -> 7 -> 9 -> None
     ↑
   list1
```

The node still exists. Only the pointer moved.

## Dummy Node

Instead of worrying about:

```python
if head is None:
```

for the first insertion, create:

```python
dummy = ListNode()
tail = dummy
```

Visualized:

```text
dummy
  ↑
tail
```

The dummy node is fake. Its only purpose is to simplify construction.

## Tail Pointer

Invariant:

```text
dummy -> merged list built so far
                 ↑
               tail
```

`tail` always points to the final node of the merged list.

Every new node gets attached after it.

## Algorithm

While both lists still contain nodes:

1. Compare values.
2. Take the smaller node.
3. Attach it to `tail`.
4. Advance that list.
5. Advance `tail`.

## Example Walkthrough

Initial:

```text
list1: 1 -> 3 -> 5
list2: 2 -> 4 -> 6

dummy
 ↑
tail
```

Compare:

```text
1 vs 2
```

Take:

```text
1
```

Now:

```text
dummy -> 1
          ↑
        tail

list1 -> 3 -> 5
list2 -> 2 -> 4 -> 6
```

Compare:

```text
3 vs 2
```

Take:

```text
2
```

Now:

```text
dummy -> 1 -> 2
               ↑
             tail
```

Continue until one list runs out.

## Important Insight

Suppose:

```text
1 -> 2 -> 3
          ↑
        tail

list1
 ↓
5 -> 7 -> 9 -> None
```

Then:

```python
tail.next = list1
```

produces:

```text
1 -> 2 -> 3 -> 5 -> 7 -> 9 -> None
```

We do not need:

```python
while list1:
```

because linked list nodes are already chained together.

One pointer assignment attaches the entire remaining list.

This is the biggest insight from the problem.

## Final Solution

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

## Complexity

- Time: `O(n + m)`
- Space: `O(1)`

Where:

- `n = len(list1)`
- `m = len(list2)`

Every node is visited exactly once, and no extra linked list is created.

## Pattern Takeaways

### Dummy Node Pattern

Use when:

- building a linked list
- repeatedly appending nodes
- wanting to avoid special-casing the first insertion

### Tail Pointer Pattern

Invariant:

```text
tail = last node of output list
```

Every insertion happens through:

```python
tail.next = node
tail = tail.next
```

## Major Insight Learned

Linked list variables are pointers into chains.

This means:

```python
tail.next = list1
```

attaches an entire remaining linked list instantly.

It does not attach just one node.

That realization appears repeatedly in linked list problems.

## Retention Card

- Problem: 21. Merge Two Sorted Lists
- Difficulty: Easy
- Time Spent: ___
- Pattern: dummy node + tail pointer
- Trigger: building a linked list by repeatedly appending nodes
- Core Insight: compare front nodes; append smaller; attach remainder once one list ends
- Template: `dummy`, `tail`, while both lists, then `tail.next = remaining`
- Complexities: `O(n + m)` time, `O(1)` space

Mistakes:

- Return `dummy.next`, not `dummy`.
- Advance `tail` after attaching a node.
- Do not loop through the entire remaining list manually.
