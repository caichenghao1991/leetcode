# 647. Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        l, res = len(s), 0
        dp = [[False] * l for _ in range(l)]

        for i in range(l - 1, -1, -1):
            for j in range(i, l):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        res += 1
                    elif dp[i + 1][j - 1] == True:
                        dp[i][j] = True
                        res += 1

        return res
