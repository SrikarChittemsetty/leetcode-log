# Alternatives

## Set Of Words And Prefixes

One simple implementation is to keep two sets:

- one set for complete words
- one set for all prefixes

This makes lookup easy, but it duplicates prefix strings and does not model the
shared-prefix structure as directly as a trie.

## Nested Dictionaries

The trie can also be represented with nested dictionaries and a sentinel marker
for word endings.

That works, but an explicit `TrieNode` class makes the two responsibilities
clearer:

- `children` for traversal
- `end` for complete-word termination
