# LeetCode 50: Pow(x, n)

## Metadata

- Difficulty: Medium
- Topic: Math / Recursion / Divide and Conquer / Fast Exponentiation
- Time:
- Result:
- Link: https://leetcode.com/problems/powx-n/

## Problem Summary

Compute `x^n` efficiently, where `x` is a float and `n` is an integer that can be negative.

Naive repeated multiplication takes `O(n)` time, which is too slow for large exponents. The goal is to reduce the amount of work by reusing powers.

## Key Insight

Exponentiation can be broken down with divide and conquer.

For any exponent `n`:

```text
if n is even:
    x^n = (x^(n / 2))^2

if n is odd:
    x^n = (x^(n // 2))^2 * x
```

This cuts the exponent roughly in half on every recursive call, which gives `O(log n)` time.

## Handling Negative Exponents

If `n < 0`, invert the base and make the exponent positive:

```text
x^n = 1 / x^(-n)
```

So normalize first:

```python
if n < 0:
    x = 1 / x
    n = -n
```

## Breakthroughs

- Realized the speedup comes from shrinking the exponent exponentially, not from caching.
- Saw that each recursive call follows one chain: `n -> n // 2 -> n // 4 -> ...`.
- Understood why memoization is unnecessary: there are no overlapping subproblems.
- Separated the negative exponent case from the main recursive logic.
- Used the parity of `n` to decide whether the extra `* x` is needed.

## Pitfalls

- Using naive multiplication creates an `O(n)` solution.
- Forgetting to handle negative exponents causes incorrect results.
- Recomputing `myPow(x, n // 2)` twice would destroy the benefit of divide and conquer.
- Confusing `n / 2` with integer division. The recursive exponent should use `n // 2`.
- Missing the `n == 0` base case.

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
- Space: `O(log n)` due to the recursion stack.

## Mental Model

Repeatedly halve the exponent and reuse the computed half-power to build the final result efficiently.

Fast exponentiation is divide and conquer:

> Compute the half once, square it, and only multiply by the base when the exponent is odd.

## Interview Trigger

If you see:

- exponentiation
- very large `n`
- repeated multiplication that seems too slow
- recursive or divide-and-conquer framing

Immediately ask:

> Can I halve the exponent and reuse the half-power?

