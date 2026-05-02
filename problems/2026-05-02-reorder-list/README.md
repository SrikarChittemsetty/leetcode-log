# LeetCode 143: Reorder List

## Metadata

- Difficulty: Medium
- Topic: Linked List / Two Pointers / In-Place Manipulation
- Time: ~16 minutes
- Result: Solved, final weaving bug corrected conceptually
- Link: https://leetcode.com/problems/reorder-list/

## Problem Summary

Given a singly linked list:

```text
L0 -> L1 -> ... -> Ln-1 -> Ln
```

Reorder it into:

```text
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
```

Constraints:

- Must modify the list in-place.
- Cannot change node values.

## Key Insight

The problem breaks naturally into three phases:

1. Find the middle of the list using fast and slow pointers.
2. Reverse the second half of the list.
3. Merge, or weave, the two halves alternately.

This transforms a hard pointer-rewiring problem into three standard linked list operations.

## Breakthroughs

- Recognized the need to split the problem into structural subproblems.
- Used fast and slow pointers to find the midpoint efficiently.
- Understood the importance of breaking the list at the midpoint with `slow.next = None`.
- Applied standard iterative linked list reversal.
- Identified the alternating merge pattern for weaving two lists.
- Learned that pointer safety requires storing `next` references before rewiring.

## Pitfalls

- Initially confusing the role of the fast pointer after midpoint detection.
- Forgetting to store the second half head before breaking the list.
- Incorrectly assuming weaving can be done in a single step.
- Overwriting pointers without preserving next references first.
- Missing the loop in the final merge step.

## Final Solution

```python
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: find middle.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: split and reverse second half.
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: merge two halves.
        l1, l2 = head, prev
        while l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Mental Model

Break the linked list into three independent transformations:

```text
find midpoint -> reverse second half -> weave two lists
```

Each step is a standard pattern. The difficulty is recognizing the decomposition.

## Interview Trigger

If you see:

- reorder or rearrange linked list
- alternating front/back pattern
- in-place constraint

Immediately ask:

> Can I split the list, reverse one half, and merge them alternately?

