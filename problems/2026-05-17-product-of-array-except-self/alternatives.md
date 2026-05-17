# Alternatives

## Division

If division were allowed, one could compute the total product and divide by each
element.

The problem explicitly forbids division, and zeros make division-based logic
more complicated anyway.

## Output Array As Prefix Store

The extra `left` and `right` arrays can be compressed by storing prefix products
directly in the output array, then multiplying suffix products into it during a
right-to-left pass.

That reduces auxiliary space, excluding the output, to `O(1)`.

The explicit `left` / `right` version is easier to reason about first.
