import math

class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        if negative:
            x = -x
        
        digits = list(str(x))
        digits.reverse()

        start_idx = 0
        for i in range(len(digits)):
            if digits[i] == '0':
                continue
            else:
                start_idx = i
                break
        
        reverse_digits = digits[i:]
        result = int("".join(reverse_digits))

        if negative:
            result = -result

        if not (-2147483648 <= result <= 2147483647):
            return 0
        else:
            return result
