import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert sorted(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == [-1, 2]
