# Alternatives

## Set-Based Deduplication

A set can identify unique values, but it is not appropriate for this problem
because the task requires in-place modification and ordered output in the
original array.

## New Array

Building a separate list of unique values is straightforward, but it uses
`O(n)` extra space. The sorted input makes that unnecessary.
