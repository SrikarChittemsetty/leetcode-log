# Alternate Solutions

## Iterative Binary Exponentiation

Idea:

Use the binary representation of the exponent. Keep a running result and repeatedly square the base while halving the exponent.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result
```

Complexity:

- Time: `O(log n)`
- Space: `O(1)`

Why it is useful:

- Avoids recursion stack space.
- Often preferred when recursion depth or stack usage matters.
- Same core mental model: use exponent halving and only multiply into the answer when the current exponent bit is active.

