# Alternatives

## Sort By Frequency

After building the frequency map, sort items by frequency:

```python
items = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
return [num for num, freq in items[:k]]
```

This is straightforward but costs `O(m log m)` for `m` distinct values.

## Bucket Sort

Because a frequency can be at most `n`, another optimal approach creates buckets
where index = frequency.

This can achieve `O(n)` time, but the heap approach is a strong general top-k
pattern.

## Simulated Max-Heap

Use negative frequencies:

```python
heapq.heappush(heap, (-freq, num))
```

Then pop `k` times.

This works, but the heap may grow to size `m`; the size-`k` min-heap keeps only
the best candidates.
