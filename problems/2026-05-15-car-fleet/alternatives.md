# Alternatives

## Stack Framing

Some solutions explicitly store fleet arrival times in a stack.

After sorting by position, each new time is compared with the stack top:

- if it is greater, push it as a new fleet
- if it is less than or equal, it merges with the fleet ahead

The `last_time` solution is the same idea compressed into one variable because
only the nearest fleet ahead matters during the backward sweep.

## Simulation

Simulating movement or collision points is unnecessary and much harder to reason
about. The arrival-time comparison fully captures whether a car catches the
fleet ahead before the target.
