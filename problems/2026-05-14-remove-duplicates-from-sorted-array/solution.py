from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1

        return left


if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]

    nums = [1]
    k = s.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [1]
