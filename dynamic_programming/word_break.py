# 139. Word Break
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        lens, words = set(), set()
        sl = list(s)
        for w in wordDict:
            lens.add(len(w))
            words.add(w)
        lens = set(sorted(list(lens)))
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for wl in lens:
                if i >= wl and dp[i - wl] == True and ''.join(sl[i - wl:i]) in words:
                    dp[i] = True
        return dp[l]

        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for w in wordDict:
                dp[i] = dp[i] or (i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w)
        return dp[l]
