# LeetCode Log

A public interview-prep journal for turning LeetCode practice into reusable
patterns, not just final answers.

Each problem entry includes the final Python solution, complexity analysis,
pitfalls, breakthroughs, and a short mental model to make the pattern easier to
recognize in interviews.

## Current Entries

| Problem | Difficulty | Pattern |
| --- | --- | --- |
| [Rotate Image](problems/2026-05-01-rotate-image) | Medium | Matrix transforms |
| [Pow(x, n)](problems/2026-05-02-pow-x-n) | Medium | Divide and conquer |
| [Reorder List](problems/2026-05-02-reorder-list) | Medium | Linked lists / two pointers |
| [Search a 2D Matrix](problems/2026-05-02-search-a-2d-matrix) | Medium | Binary search |
| [Course Schedule](problems/2026-05-14-course-schedule) | Medium | Graph DFS / cycle detection |
| [Course Schedule II](problems/2026-05-14-course-schedule-ii) | Medium | Graph DFS / topological ordering |

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
