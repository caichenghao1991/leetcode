# 69. Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            if m ** 2 > x:
                r = m - 1
            else:
                res = m
                l = m + 1
        return res
