# LeetCode Log

A lightweight repo for tracking LeetCode practice, solve time, breakthroughs, mistakes, and alternate approaches.

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

