# 150. Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for v in tokens:
            if v not in ['+', '-', '*', '/']:
                s.append(int(v))
            else:
                b, a = s.pop(), s.pop()
                res = 0
                if v == '+':
                    res = a + b
                elif v == '-':
                    res = a - b
                elif v == '*':
                    res = a * b
                elif v == '/':
                    flag = -1 if any([a < 0, b < 0]) and not all([a < 0, b < 0]) else 1
                    res = flag * int(abs(a) / abs(b))
                s.append(res)
        return s[0]
