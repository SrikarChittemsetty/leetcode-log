from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()

        fleets = 0
        last_time = 0

        for i in range(len(pairs) - 1, -1, -1):
            pos, spd = pairs[i]
            time = (target - pos) / spd

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets


if __name__ == "__main__":
    s = Solution()
    assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert s.carFleet(10, [3], [3]) == 1
    assert s.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert s.carFleet(10, [6, 8], [3, 2]) == 2
