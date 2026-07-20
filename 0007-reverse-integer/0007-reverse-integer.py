class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)

        ans = 0
        while x > 0:
            num = x % 10
            ans = ans * 10 + num
            x = x // 10

        ans *= sign

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans           
        