# LeetCode 309: Best Time to Buy and Sell Stock with Cooldown

## Metadata

- Difficulty: Medium
- Topic: Dynamic Programming / Recursion / Memoization / State Machine
- Time:
- Result: Solved by modeling future profit from `(day, holding)` state
- Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

## Problem Summary

We are given stock prices over days.

We may:

- buy
- sell
- do nothing

Restrictions:

- cannot hold more than one stock at a time
- after selling, must wait one day before buying again

Goal:

```text
maximize total profit
```

## Main Realization

This is not a greedy problem.

A locally good sale may block a better future opportunity because of cooldown.

So instead of asking:

```text
What should I do right now?
```

we ask:

```text
What is the best future profit possible from this situation?
```

## Core Idea

At every day there are different possible situations:

1. currently holding a stock
2. currently not holding a stock

The future choices depend entirely on:

- current day
- whether we own a stock

So the recursive function becomes:

```python
dfs(i, holding)
```

meaning:

```text
maximum future profit starting from day i
given whether we currently hold a stock
```

## Important DP Insight

We do not store:

```text
what price we bought at
```

because buying already subtracts the cost immediately:

```python
-prices[i]
```

So the running profit already mathematically encodes the purchase price.

This is an important DP modeling principle:

```text
Only store information that changes future decisions.
```

## Branching Logic

### If Not Holding

Two choices:

#### Buy

Spend money and become holding:

```python
buy = -prices[i] + dfs(i + 1, True)
```

#### Skip

Do nothing:

```python
skip = dfs(i + 1, False)
```

Take the better option:

```python
return max(buy, skip)
```

### If Holding

Two choices:

#### Sell

Gain money and trigger cooldown:

```python
sell = prices[i] + dfs(i + 2, False)
```

Important:

```python
i + 2
```

because after selling on day `i`, day `i + 1` is cooldown.

#### Hold

Keep the stock:

```python
hold = dfs(i + 1, True)
```

Take the better option:

```python
return max(sell, hold)
```

## Base Case

If we run out of days:

```python
if i >= len(prices):
    return 0
```

No future profit is possible.

## Memoization Insight

Different decision paths can reach the same situation:

```python
(day, holding)
```

So we cache answers to avoid recomputing them repeatedly.

## Breakthroughs

- Rejected greedy selling because cooldown changes future options.
- Modeled the problem around state instead of transaction history.
- Realized buy price does not need to be stored separately.
- Used `i + 2` after selling to encode the cooldown day.
- Cached `(i, holding)` states to collapse repeated recursion.

## Pitfalls

- Trying to greedily take every profitable sale.
- Storing unnecessary state like buy price.
- Advancing to `i + 1` after selling and accidentally ignoring cooldown.
- Forgetting that skipping while not holding and holding while holding are both valid choices.

## Final Solution

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding == False:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)

                memo[(i, holding)] = max(buy, skip)

            else:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)

                memo[(i, holding)] = max(sell, hold)

            return memo[(i, holding)]

        return dfs(0, False)
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`

There are `n` days and two possible holding states per day.

## Mental Model

This is recursive decision exploration over a small state:

```text
(day, holding) -> best future profit
```

Buying subtracts value.

Selling adds value and skips the cooldown day.

Memoization turns the decision tree into a linear number of states.

## Interview Trigger

If you see:

- maximize profit over time
- buy/sell/skip choices
- cooldown or transaction constraints
- future decisions depend on a small current state

Think:

```text
DP over (day, state)
```

## One-Line Memory Hook

When future choices depend on a small current situation:

```text
(day, state) -> best future result
```

think recursive decision exploration plus memoization.
