# LeetCode 50: Pow(x, n)

## Metadata

- Difficulty: Medium
- Topic: Math / Recursion / Divide and Conquer
- Time: ~12 minutes
- Result: Solved
- Link: https://leetcode.com/problems/powx-n/

## Problem Summary

Compute `x^n`, where `x` is a float and `n` is an integer that can be negative. Must avoid naive `O(n)` multiplication and handle large constraints efficiently.

## Key Insight

Exponentiation can be reduced using divide and conquer.

Even exponent:

```text
x^n = (x^(n / 2))^2
```

Odd exponent:

```text
x^n = (x^(n // 2))^2 * x
```

This reduces the problem size by half each step, giving logarithmic time complexity.

Negative exponents are handled by inverting the base:

```text
x^(-n) = 1 / x^n
```

## Breakthroughs

- Rejected naive `O(n)` repeated multiplication.
- Recognized exponentiation can be split recursively.
- Understood even vs odd decomposition of the exponent.
- Identified the need to normalize negative exponents early.
- Realized reuse comes from structure, not memoization.
- Built a correct recursive divide-and-conquer solution.

## Pitfalls

- Confusing binary or halving logic with bitwise operations, which are not required.
- Overthinking memoization, which is unnecessary because there are no overlapping subproblems.
- Misunderstanding odd exponent handling: must multiply by one extra `x`.
- Thinking recursion branches overlap. They do not; this follows a single path.

## Final Solution

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        if n == 0:
            return 1

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half

        return half * half * x
```

## Complexity

- Time: `O(log n)`
- Space: `O(log n)`

## Mental Model

Think of exponentiation as repeatedly halving the exponent and reusing computed results instead of recomputing from scratch.

## Interview Trigger

If you see:

- large exponentiation problem
- need to compute powers efficiently
- `x^n` with large constraints

Immediately ask:

> Can I reduce exponent size using divide and conquer or binary decomposition instead of linear multiplication?

