# Alternatives

## BFS From Every Empty Room

One approach is to run BFS from each empty room until a gate is found.

That works logically, but it repeats exploration many times and is much slower
than starting from all gates at once.

## DFS

DFS can explore reachable cells, but it does not naturally guarantee shortest
path in an unweighted graph without extra distance checks and repeated updates.

BFS is cleaner because level-order traversal makes the first visit optimal.
