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


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([1, 2, 3, 0, 2]) == 3
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([2, 1, 4]) == 3
    assert s.maxProfit([6, 1, 6, 4, 3, 0, 2]) == 7
