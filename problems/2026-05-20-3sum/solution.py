from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


def normalize(triplets: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(triplet) for triplet in triplets)


if __name__ == "__main__":
    s = Solution()
    assert normalize(s.threeSum([-1, 0, 1, 2, -1, -4])) == normalize(
        [[-1, -1, 2], [-1, 0, 1]]
    )
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert s.threeSum([]) == []
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
