# LeetCode 206: Reverse Linked List

## Metadata

- Difficulty: Easy
- Topic: Linked List / Pointer Manipulation
- Result: Solved
- Link: https://leetcode.com/problems/reverse-linked-list/

## Problem Summary

Given the head of a singly linked list, reverse the list and return the new
head.

Example:

```text
1 -> 2 -> 3 -> None

becomes

3 -> 2 -> 1 -> None
```

## Pattern Recognition

This is the fundamental linked list pointer manipulation problem.

Key challenge:

```text
When reversing a pointer, we risk losing access to the remainder of the list.
```

## Initial Thought

Suppose:

```text
1 -> 2 -> 3 -> None
```

and we are currently at node `1`.

If we immediately do:

```python
curr.next = prev
```

then:

```text
1 -> None
```

and we lose access to:

```text
2 -> 3 -> None
```

unless we saved it first.

This is the critical insight of the problem.

## Core Idea

Maintain three pointers:

```python
prev
curr
nxt
```

Where:

```text
prev = already reversed portion
curr = node currently being processed
nxt  = remainder of list
```

## Initialization

Initially:

```python
prev = None
curr = head
```

Visualized:

```text
prev = None

curr
 ↓
1 -> 2 -> 3 -> None
```

The reversed portion is empty.

## Reversal Step

For each node:

### Step 1: Save Remainder

```python
nxt = curr.next
```

Store the rest of the list before changing pointers.

### Step 2: Reverse Current Pointer

```python
curr.next = prev
```

Example:

Before:

```text
1 -> 2 -> 3
```

After:

```text
1 -> None
```

### Step 3: Advance `prev`

```python
prev = curr
```

The current node is now part of the reversed list.

### Step 4: Advance `curr`

```python
curr = nxt
```

Continue processing the remainder.

## Walkthrough

Initial state:

```text
prev = None
curr = 1

1 -> 2 -> 3 -> None
```

Iteration 1:

```python
nxt = 2
curr.next = None
prev = 1
curr = 2
```

Now:

```text
1 -> None

2 -> 3 -> None
```

Iteration 2:

```python
nxt = 3
curr.next = 1
prev = 2
curr = 3
```

Now:

```text
2 -> 1 -> None

3 -> None
```

Iteration 3:

```python
nxt = None
curr.next = 2
prev = 3
curr = None
```

Now:

```text
3 -> 2 -> 1 -> None
```

Loop terminates.

## Why Return `prev`?

At termination:

```python
curr = None
```

but:

```python
prev
```

points to:

```text
3 -> 2 -> 1 -> None
```

which is the new head.

Therefore:

```python
return prev
```

## Final Solution

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

Each node is visited exactly once, and only three pointers are maintained.

## Key Takeaways

- Linked list problems are pointer problems, not value problems.
- Always save the remainder of the list before modifying pointers.
- `prev` tracks the head of the reversed portion.
- `curr` tracks the node currently being processed.
- `nxt` prevents losing access to the rest of the list.
- At the end, `prev` becomes the new head.

## Mental Model

Before each iteration:

```text
prev -> reversed portion

curr -> current node

nxt -> remainder of list
```

Each iteration moves exactly one node from:

```text
unprocessed
```

to:

```text
reversed
```

until the entire list has been reversed.

## Retention Card

- Problem: 206. Reverse Linked List
- Difficulty: Easy
- Time Spent: ___
- Pattern: linked list pointer reversal
- Trigger: reverse links in a singly linked list
- Core Insight: save `curr.next` before rewiring `curr.next`
- Template: `nxt = curr.next`, `curr.next = prev`, advance both pointers
- Complexities: `O(n)` time, `O(1)` space

Mistakes:

- Do not overwrite `curr.next` before saving the remainder.
- Return `prev`, not `curr`.
