# 59. Spiral Matrix II
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        l, r = 0, n - 1
        t, b = 0, n - 1
        loop = 0
        val = 1
        res = [[n ** 2] * n for i in range(n)]
        while loop < n // 2:
            for i in range(l, r + 1):
                res[t][i] = val
                val += 1
            t += 1
            for i in range(t, b + 1):
                res[i][r] = val
                val += 1
            r -= 1
            for i in range(r, l - 1, -1):
                res[b][i] = val
                val += 1
            b -= 1
            for i in range(b, t - 1, -1):
                res[i][l] = val
                val += 1
            l += 1
            loop += 1
        return res
