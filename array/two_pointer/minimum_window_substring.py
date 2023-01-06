# 76. Minimum Window Substring    need rework

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        req, win = {}, {}
        for c in t:
            req[c] = 1 if c not in req else req[c] + 1
        start, length = 0, len(s) + 1
        l, r = 0, 0
        valid = 0
        while r < len(s):
            c = s[r]
            if c in req:
                win[c] = 1 if c not in win else win[c] + 1
            if req.get(c) == win.get(c) and c in req:
                valid += 1
            r += 1
            while valid == len(req):
                if r - l < length:
                    start, length = l, r - l
                d = s[l]
                if d in req:
                    if req.get(d) == win.get(d) and d in req:
                        valid -= 1
                    win[d] -= 1
                l += 1

        return s[start:start + length] if length != len(s) + 1 else ""
