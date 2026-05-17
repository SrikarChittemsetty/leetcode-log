# Alternatives

## Delimiter-Only Encoding

Joining strings with a delimiter is tempting:

```python
",".join(strs)
```

But this fails when the delimiter appears inside a string.

## Escaping Delimiters

Another design is to escape delimiters inside strings.

This can work, but it adds more parsing complexity. Length-prefix encoding is
simpler because the decoder always knows exactly how many characters to read.

## JSON

In production code, JSON or another established serialization format may be
better. For this interview problem, the goal is to design the encoding logic
directly.
