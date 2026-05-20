# LeetCode 121: Best Time to Buy and Sell Stock

## Metadata

- Difficulty: Easy
- Topic: Sliding Window / Running Minimum
- Result: Solved
- Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem Summary

Given an array `prices`, where `prices[i]` is the stock price on day `i`, choose
one day to buy and a later day to sell.

Return the maximum possible profit.

If no profitable trade exists, return `0`.

Important constraint:

```text
buy day must come before sell day
```

## Core Idea

Track the minimum price seen so far.

For each day, ask:

```text
If I sold today, what is the best earlier buy price?
```

That best earlier buy price is the running minimum.

## Key Realization

Brute force checks every buy/sell pair:

```text
O(n^2)
```

But for any sell day, only one previous value matters:

```text
the smallest price before or at today
```

So we can scan once, updating:

- `min_price`
- `max_profit`

## Running Minimum Logic

For each `price`:

1. Update the best buy price so far.
2. Compute profit if selling today.
3. Update the best profit.

```python
min_price = min(min_price, price)
profit = price - min_price
max_profit = max(max_profit, profit)
```

Because `min_price` only comes from days already visited, the buy-before-sell
rule is preserved.

## Why This Works

The best sell today always pairs with the lowest price from the past.

There is no reason to remember every previous price, because any higher buy
price produces a worse profit for the same sell day.

The scan keeps exactly the state future days need.

## Pitfalls

- Allowing the sell day to come before the buy day.
- Tracking the maximum price instead of the minimum previous price.
- Returning negative profit instead of `0`.
- Using nested loops when a running minimum is enough.

## Final Solution

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

The array is scanned once and only two variables are maintained.

## Interview Trigger

If you see:

- maximize profit
- buy before sell
- future value compared to past minimum
- one transaction

Think:

```text
running minimum + max profit
```

## Retention Card

- Problem: 121. Best Time to Buy and Sell Stock
- Difficulty: Easy
- Time Spent: ___
- Pattern: sliding window / running minimum
- Trigger: maximize future profit
- Core Insight: best sell today uses minimum previous buy price
- Template: track min price so far and max profit
- Complexities: `O(n)` time, `O(1)` space

Process:

- Brute force checks all buy/sell pairs.
- Only smallest previous price matters.
- Update running minimum dynamically.

Mistakes:

- Buy must occur before sell.
