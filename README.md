# LeetCode Log

A public interview-prep journal for turning LeetCode practice into reusable
patterns, not just final answers.

Each problem entry includes the final Python solution, complexity analysis,
pitfalls, breakthroughs, and a short mental model to make the pattern easier to
recognize in interviews.

## Current Entries

| Problem | Difficulty | Pattern |
| --- | --- | --- |
| [Two Sum](problems/2026-05-17-two-sum) | Easy | Hash map lookup |
| [Contains Duplicate](problems/2026-05-17-contains-duplicate) | Easy | Hash set membership |
| [Valid Anagram](problems/2026-05-17-valid-anagram) | Easy | Frequency counting |
| [Remove Duplicates from Sorted Array](problems/2026-05-14-remove-duplicates-from-sorted-array) | Easy | Two pointers / in-place array |
| [Find the Index of the First Occurrence in a String](problems/2026-05-14-find-the-index-of-the-first-occurrence-in-a-string) | Easy | Fixed-size sliding window |
| [Group Anagrams](problems/2026-05-17-group-anagrams) | Medium | Frequency signature grouping |
| [Top K Frequent Elements](problems/2026-05-17-top-k-frequent-elements) | Medium | Frequency map / heap |
| [Product of Array Except Self](problems/2026-05-17-product-of-array-except-self) | Medium | Prefix/suffix products |
| [Rotate Image](problems/2026-05-01-rotate-image) | Medium | Matrix transforms |
| [Valid Sudoku](problems/2026-05-17-valid-sudoku) | Medium | Constraint tracking with sets |
| [Pow(x, n)](problems/2026-05-02-pow-x-n) | Medium | Divide and conquer |
| [Reorder List](problems/2026-05-02-reorder-list) | Medium | Linked lists / two pointers |
| [Search a 2D Matrix](problems/2026-05-02-search-a-2d-matrix) | Medium | Binary search |
| [Course Schedule](problems/2026-05-14-course-schedule) | Medium | Graph DFS / cycle detection |
| [Course Schedule II](problems/2026-05-14-course-schedule-ii) | Medium | Graph DFS / topological ordering |
| [Walls and Gates](problems/2026-05-15-walls-and-gates) | Medium | Multi-source grid BFS |
| [Word Ladder](problems/2026-05-16-word-ladder) | Hard | BFS / implicit graph |
| [Implement Trie (Prefix Tree)](problems/2026-05-15-implement-trie-prefix-tree) | Medium | Trie / prefix tree |
| [Find the Duplicate Number](problems/2026-05-15-find-the-duplicate-number) | Medium | Floyd's cycle detection |
| [Car Fleet](problems/2026-05-15-car-fleet) | Medium | Ordered sweep / monotonic state |
| [Best Time to Buy and Sell Stock with Cooldown](problems/2026-05-17-best-time-to-buy-and-sell-stock-with-cooldown) | Medium | DP / memoized state search |

## What This Shows

- Clear problem decomposition under interview constraints.
- Python implementations with time and space complexity.
- Notes on mistakes and boundary cases, not only polished final code.
- Small commits that show steady practice and reflection.

## Workflow

1. Create a new problem folder.
2. Start your timer.
3. Work in the problem folder and leave notes as you go.
4. Commit when you finish or hit a useful stopping point.

## Create A Problem Entry

```bash
python3 scripts/new_problem.py "Two Sum" easy
```

This creates a folder under `problems/` with:

- `README.md` for timing, notes, insights, and reflection.
- `solution.py` for the main solution.
- `alternatives.md` for other approaches you try later.

## Commit Style

Use small commits so your GitHub activity tells the story:

```bash
git add .
git commit -m "Solve two sum"
```

For partial progress:

```bash
git commit -m "Work through two sum brute force"
```
