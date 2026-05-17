# Alternatives

## Sorting

Sort the array, then scan for consecutive runs.

This is intuitive, but sorting costs `O(n log n)`, which misses the required
linear-time target.

## Expand From Every Number

Using a set but expanding from every number still repeats work.

The key improvement is not just fast membership checking. It is only expanding
from numbers that have no predecessor.
