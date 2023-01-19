# 738. Monotone Increasing Digits
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10: return n
        start, digits = -1, []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        for i in range(len(digits)):
            if i + 1 < len(digits) and digits[i] < digits[i + 1]:
                start = i
                digits[i] = 9
                digits[i + 1] -= 1

        for i in range(start):
            digits[i] = 9

        res = 0
        for i in range(len(digits)):
            res += 10 ** i * digits[i]
        return res
