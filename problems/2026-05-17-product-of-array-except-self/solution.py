from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        answer = [0] * len(nums)

        product = 1

        for i in range(len(left)):
            left[i] = product
            product *= nums[i]

        product = 1

        for i in range(len(left) - 1, -1, -1):
            right[i] = product
            product *= nums[i]

        for i in range(len(nums)):
            answer[i] = left[i] * right[i]

        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([2, 3]) == [3, 2]
