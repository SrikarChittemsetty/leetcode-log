class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        if n == 0:
            return 1

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half

        return half * half * x


if __name__ == "__main__":
    solution = Solution()
    assert abs(solution.myPow(2.0, 10) - 1024.0) < 1e-9
    assert abs(solution.myPow(2.0, -2) - 0.25) < 1e-9
    assert abs(solution.myPow(2.1, 3) - 9.261) < 1e-9
    assert abs(solution.myPow(5.0, 0) - 1.0) < 1e-9

