# Alternate Solutions

## Array Of Nodes

Idea:

Store all nodes in an array, then use two pointers from the front and back to reconnect them in the desired order.

Complexity:

- Time: `O(n)`
- Space: `O(n)`

Why it is less ideal:

- Easier to implement, but violates the spirit of the in-place constraint.
- Does not practice the linked list patterns this problem is designed to test.

## Recursive Reordering

Idea:

Use recursion to reach the end of the list and reconnect front/back nodes while unwinding.

Complexity:

- Time: `O(n)`
- Space: `O(n)` due to recursion stack.

Why I prefer split + reverse + weave:

- Fully in-place with `O(1)` extra space.
- Built from reusable linked list patterns.
- Easier to reason about pointer safety one phase at a time.

