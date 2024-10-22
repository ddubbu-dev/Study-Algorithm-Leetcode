import math

class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        x = abs(x)

        result = int(str(x)[::-1])

        if negative:
            result = -result

        if not (-2147483648 <= result <= 2147483647):
            return 0
        else:
            return result
