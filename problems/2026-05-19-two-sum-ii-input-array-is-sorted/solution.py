from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            if total < target:
                left += 1
            else:
                right -= 1

        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]
    assert s.twoSum([1, 2, 3, 4, 4, 9], 8) == [4, 5]
