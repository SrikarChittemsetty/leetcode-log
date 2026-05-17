# Alternatives

## Bottom-Up DP

The same state can be converted into iterative DP with states such as:

- holding
- not holding / resting
- cooldown

This avoids recursion stack usage but can be harder to derive at first.

## Greedy

Greedy approaches are risky because cooldown means a profitable sale today can
block a better buy tomorrow.

The local best action is not always globally optimal.
