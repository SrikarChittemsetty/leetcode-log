# Alternatives

## Built-In `.find()`

Python's built-in string method solves the problem directly:

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

This is concise and valid unless the interviewer asks for a manual
implementation.

## KMP

Knuth-Morris-Pratt can solve substring search in `O(n + m)` time by preprocessing
the pattern. For this Easy problem, the fixed-window approach is usually enough
unless the interviewer asks for optimal string matching.
