# LeetCode 208: Implement Trie (Prefix Tree)

## Metadata

- Difficulty: Medium
- Topic: Trie / Prefix Tree / Tree Traversal By Characters
- Time:
- Result: Solved after modeling each character as a tree edge
- Link: https://leetcode.com/problems/implement-trie-prefix-tree/

## Problem Summary

Design a Trie, also known as a prefix tree, with three operations:

- `insert(word)`
- `search(word)`
- `startsWith(prefix)`

The data structure must store words efficiently and support exact-word and
prefix lookups.

## Core Idea

A trie stores words character-by-character instead of as complete strings.

Shared prefixes reuse the same path in the tree structure.

Example:

```text
"app" and "apple" share:

a -> p -> p
```

This avoids duplicating prefixes and allows efficient prefix searching.

## Key Structure

Each `TrieNode` stores:

### `children`

A dictionary mapping:

```text
character -> next TrieNode
```

### `end`

A boolean indicating whether a complete word terminates at this node.

## Important Realization

A node can simultaneously:

- mark the end of a word
- still have children

Example:

```text
"app" can terminate while "apple" continues deeper
```

This is why `search()` must check `node.end` after traversal.

The prefix path existing is not enough to prove the complete word was inserted.

## Root Node

The trie begins with an empty root node.

The root does not represent a character itself.

All traversals begin from the root.

## Insert Logic

For each character:

1. Check whether the child node exists.
2. Create the node if missing.
3. Move the traversal pointer downward.

After processing the final character:

```python
node.end = True
```

## Search Logic

Traverse character-by-character through `children`.

If any character path does not exist:

```python
return False
```

After traversal completes:

```python
return node.end
```

This distinction matters because a prefix existing does not necessarily mean a
full word exists.

## `startsWith` Logic

Use the same traversal process as `search`, except:

- no need to check `node.end`
- only verify that the prefix path exists

If every prefix character can be followed, return `True`.

## Breakthroughs

- Recognized that words can share character paths.
- Separated node traversal from word termination.
- Understood why `end` is needed even when a path exists.
- Used an empty root node as the stable traversal starting point.

## Pitfalls

- Returning `True` from `search()` just because the path exists.
- Forgetting that a word-ending node can still have children.
- Storing complete words at every node instead of only edge relationships and termination flags.
- Reinitializing traversal state inside a loop instead of moving down the tree.

## Final Solution

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
```

## Complexity

Let `n` be the length of the input string.

- Insert: `O(n)`
- Search: `O(n)`
- `startsWith`: `O(n)`

Space is proportional to the total number of characters inserted across all
unique trie paths.

## Mental Model

A trie is a character graph/tree where traversal state matters more than storing
complete words directly.

Each character moves the pointer one level deeper.

`end` answers:

```text
Did a full word stop here?
```

## Interview Trigger

If you see:

- prefix lookup
- dictionary/autocomplete behavior
- many string insert/search operations
- shared string prefixes

Think:

```text
Trie with character-to-node children and explicit word-ending markers
```
