# LeetCode 238: Product of Array Except Self

## Metadata

- Difficulty: Medium
- Topic: Arrays / Prefix Products / Suffix Products
- Result: Solved
- Link: https://leetcode.com/problems/product-of-array-except-self/

## Problem Summary

Given an integer array `nums`, return an array `answer` where:

```python
answer[i] = product of every element except nums[i]
```

Constraints:

- must run in `O(n)` time
- cannot use division

## Initial Understanding

### Brute Force Intuition

Natural brute force:

1. For every index.
2. Multiply every other number.
3. Store result.

Complexity:

```text
O(n^2)
```

because for each index we scan the array again.

## Key Observation

For any index `i`:

```python
answer[i] =
    (product of everything left of i)
    *
    (product of everything right of i)
```

This transforms the problem from:

```text
repeated full-array multiplication
```

into:

```text
reusable prefix/suffix products
```

## Prefix Product Insight

Define:

```python
left[i] = product of all elements before index i
```

Example:

```python
nums = [1, 2, 3, 4]
left = [1, 1, 2, 6]
```

Reasoning:

- nothing before index `0` -> `1`
- before `2` -> `1 * 2`
- before `3` -> `1 * 2 * 3`

Key realization:

1. maintain a running product
2. assign current running product before multiplying current element
3. "lag behind" one index

## Suffix Product Insight

Mirror idea from the right side.

Define:

```python
right[i] = product of all elements after index i
```

Built by:

- traversing right to left
- maintaining running product
- assigning before multiplying current element

## Final Combination

For every index:

```python
answer[i] = left[i] * right[i]
```

This reconstructs:

- all elements before `i`
- multiplied by all elements after `i`

thus excluding `nums[i]`.

## Traversal Details Reinforced

### Left Traversal

```python
for i in range(n):
```

### Right Traversal

```python
for i in range(n - 1, -1, -1):
```

Important understanding:

- start at last index
- stop before `-1`
- move backward by `-1`

## Array Alignment Insight

Important realization:

```text
left
right
answer
nums
```

all share the same index structure.

Thus:

```python
left[i]
right[i]
nums[i]
answer[i]
```

all correspond to the same logical position.

## Running Product Invariant

At every step:

```text
assign current running product first
then multiply current value
```

This correctly excludes the current index itself.

## Breakthroughs

- Identified brute force and its repeated work.
- Decomposed each answer into left and right contributions.
- Derived prefix and suffix products independently.
- Correctly implemented reverse traversal.
- Maintained `O(n)` time without division.

## Pitfalls

- Multiplying the current value before assigning the running product.
- Forgetting that the empty product on either side is `1`.
- Getting reverse traversal bounds wrong.
- Trying to use division despite the constraint.

## Final Solution

```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        answer = [0] * len(nums)

        product = 1

        for i in range(len(left)):
            left[i] = product
            product *= nums[i]

        product = 1

        for i in range(len(left) - 1, -1, -1):
            right[i] = product
            product *= nums[i]

        for i in range(len(nums)):
            answer[i] = left[i] * right[i]

        return answer
```

## Complexity Analysis

Let:

```text
n = length of array
```

### Time Complexity

Three linear passes:

```text
O(n)
```

- build left products
- build right products
- combine results

### Space Complexity

Three auxiliary arrays:

```text
O(n)
```

for:

- `left`
- `right`
- `answer`

## Important Conceptual Takeaways

### Prefix/Suffix Technique

Major pattern:

Problems involving:

```text
everything except current index
```

often decompose naturally into:

- left contribution
- right contribution

This is a foundational array pattern.

## Interview Notes

Strong reasoning progression:

- identified brute force
- recognized repeated work
- decomposed answer into left/right contributions
- derived prefix and suffix products independently
- correctly implemented reverse traversal
- maintained `O(n)` without division

## Interview Trigger

If you see:

- product/sum except self
- all elements except current
- no division
- repeated full-array work

Think:

```text
prefix contribution * suffix contribution
```
