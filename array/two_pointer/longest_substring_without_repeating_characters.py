# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                res = max(res, (r - l + 1))
                r += 1
            else:
                while s[l] != s[r]:
                    cur.discard(s[l])
                    l += 1
                l += 1
                r += 1
        return res